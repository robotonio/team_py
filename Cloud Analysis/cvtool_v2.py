import cv2
import numpy as np
import os


def map(value, in_min, in_max, out_min, out_max):
    scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return int(scaled_value)

class CVTool:
    def __init__(self, main_folder="imgs"):
        self.classes = ["blanket", "parasol", "none"]
        self.main_folder = main_folder
        self.bar = None
        self.init_bar()

    def init_bar(self):
        self.bar = {}
        
        for class_name in self.classes:
            folder = "imgs/" + class_name
            folder_list = os.listdir(folder)
            self.bar[class_name] = len(folder_list)
        print(self.bar)

    def cloud_coverage(self, image, K=3, scale=0.15, show=False):
        img = image.copy()
        width = int(img.shape[1] * scale)
        height = int(img.shape[0] * scale)
        dim = (width, height)
        # resize image
        if scale != 1:
            img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        s, thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY_INV)
        contour_img = cv2.dilate(cv2.Canny(thresh, 0, 255), None)
        contours = cv2.findContours(contour_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours[-2], key=cv2.contourArea)
        mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
        # masked
        masked_img = cv2.drawContours(mask, [contours[-1]], -1, 255, -1)
        frame_pixels = np.count_nonzero(masked_img == 0)
        img_pixels = np.count_nonzero(masked_img == 255)
        clear_image = cv2.bitwise_and(img, img, mask=masked_img)
        twoDimage = clear_image.reshape((-1,3))
        twoDimage = np.float32(twoDimage)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        attempts=10
        ret,label,center = cv2.kmeans(twoDimage,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        result_image = res.reshape((img.shape))
        gray_result = cv2.cvtColor(result_image, cv2.COLOR_BGR2GRAY)
        _, thresh_result = cv2.threshold(gray_result, np.max(gray_result)-20, 255, cv2.THRESH_BINARY_INV)
        cloud_pixels = np.count_nonzero(thresh_result == 0)
        cloud_percent = round((cloud_pixels * 100)/img_pixels, 2)
        if show:
            print("Original image size:", img.shape[0] * img.shape[1])
            print("Size of perimeter frame:", frame_pixels)
            print("Size on inner image, without the frame:", img_pixels)
            print("Size of clouds detected:", cloud_pixels)
            print("Percent of detected clouds:", cloud_percent, "%")
            cv2.imshow("img_or", img)
            cv2.imshow("thresh_result", thresh_result)
            cv2.imshow("masked_image", masked_img)
            cv2.waitKey(0)
        return cloud_percent

    def print_bar(self, counter=100):
        for i in range(100):
            print(" ", end="")
        print("", end='\r')
        for i in range(counter):
            print("#", end="")
        print("", end='\r')
 
    def scan(self, K=8, scale=0.15, debug=False):
        classify_clouds_percents = {}
        for class_name in self.classes:
            
            folder = "imgs/" + class_name
            sum_clouds = 0
            images = 0
            folder_list = os.listdir(folder)
            print("Process " + class_name + ": ")
            self.print_bar(counter=100)
            for image_name in folder_list:
                img = cv2.imread(os.path.join(folder, image_name))
                if img is not None:
                    images += 1
                    sum_clouds += self.cloud_coverage(img, K=K, scale=scale, show=debug)
                    per = map(images, 0, len(folder_list), 0, 100)
                    #print("per:" + str(per))
                    counter = 100 - per
                    self.print_bar(counter=counter)
            classify_clouds_percents[class_name] = round(sum_clouds/images, 2)
        return classify_clouds_percents


def main():
    cvtool = CVTool()
    print(cvtool.scan(K=8, scale=0.15, debug=False))

if __name__=="__main__":
    main()