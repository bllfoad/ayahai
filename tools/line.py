import cv2
import numpy as np

class Line:
    def __init__(self, line_num, page_width, line_height, page_img):
        self.skip = False
        self.ayaat = []
        self.line_num = line_num
        self.is_basmalah = False
        self.height = line_height
        self.width = page_width
        self.start_y = self.height * (self.line_num - 1)
        self.start_x = page_width - 1
        self.end_x = 0
        self.line_img = page_img[self.start_y: self.start_y + self.height, 0: self.width, ]
        self.update_start_end_x()

    def skip_line(self):
        self.skip = True

    def sort_ayaat_in_line(self):
        self.ayaat.sort(key=lambda pred: -pred['xmin'])

    def update_start_end_x(self) -> int:
        if len(self.line_img.shape) == 3:
            img = self.line_img[:, :, 0]
        else:
            img = self.line_img
        # Crop top and bottom to avoid stuff from other lines
        # midy = self.height // 2
        crop_amount = int(0.2 * self.height)
        img = img[crop_amount: -crop_amount, :]
        segmentation = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

        i = self.start_x
        while np.sum(segmentation[:, i]) == 0:
            i -= 1
        self.start_x = min(self.start_x, int(i + 0.01 * self.width))

        i = self.end_x
        while np.sum(segmentation[:, i]) == 0:
            i += 1
        self.end_x = max(self.end_x, int(i - 0.01 * self.width))

        # contours, hierarchy = cv2.findContours(segmentation,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #
        # start_x = self.end_x
        # end_x = self.start_x
        # for cnt in contours:
        #     leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
        #     rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
        #     if rightmost > start_x:
        #         start_x = rightmost
        #     if leftmost < end_x:
        #         end_x = leftmost

        # segmentation = segmentation[:, self.end_x: self.start_x]
        # cv2.imshow("a", segmentation[:, :, None]); cv2.waitKey(0)


    def generate_boxes(self):
        # Generates boxes for each line in format: ([{"box": [x, y, w, h], "ayah_ended": Bool}], is_new_surah: Bool)
        if self.skip:
            return ([], True) if self.is_basmalah else ([], False)
        boxes = []
        curr_x = self.start_x
        for ayah in self.ayaat:
            ayah_x = ayah["xmin"]
            boxes.append({"box": [ayah_x, self.start_y, curr_x - ayah_x, self.height],
                          "ayah_ended": True})
            curr_x = ayah_x
        if not (curr_x - self.end_x) / self.width < 0.02:
            boxes.append({"box": [0, self.start_y, curr_x, self.height],
                          "ayah_ended": False})
        return boxes, False
