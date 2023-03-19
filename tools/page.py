from tools.line import Line
from tools.global_info import GlobalInfo
import cv2
from math import floor

class Page:
    def __init__(self, num_lines: int, predictions, img_path: str, global_info: GlobalInfo):
        self.num_lines = num_lines
        self.predictions = predictions
        self.img_path = img_path
        self.img = cv2.imread(self.img_path)
        self.height, self.width, _ = self.img.shape
        self.global_info = global_info
        self.lines = {i: Line(i, self.width, self.line_height, self.img) for i in range(1, num_lines + 1)}
        self.sort_ayaat_into_lines()

    @property
    def line_height(self) -> int:
        return int(self.height / self.num_lines)

    def sort_ayaat_into_lines(self):
        # Place ayah boxes into lines first
        for prediction in self.predictions:
            midy = (prediction["ymin"] + prediction["ymax"]) / 2
            lineNum = floor(midy / self.line_height) + 1
            if prediction["name"] == "basmalah":    # Skip Basmalah line
                self.lines[lineNum].skip_line()
                self.lines[lineNum].is_basmalah = True
                if lineNum > 1:     # Skip surah box line
                    self.lines[lineNum - 1].skip_line()
            else:
                self.lines[lineNum].ayaat.append(prediction)

        # Sort within each line
        for i in range(1, self.num_lines + 1):
            self.lines[i].sort_ayaat_in_line()

        # Check if last line needs to be skipped (surah box)
        if len(self.lines[self.num_lines].ayaat) == 0:
            self.lines[self.num_lines].skip_line()

    def generate_boxes(self):
        boxes = []
        for line_num in range(1, self.num_lines + 1):
            line_boxes, is_new_surah = self.lines[line_num].generate_boxes()
            if is_new_surah:
                self.global_info.new_surah()
            else:
                for box in line_boxes:
                    boxes.append({"box": box["box"],
                                  "ayah_number": self.global_info.ayah_num})
                    if box["ayah_ended"]:
                        self.global_info.next_ayah()
        return boxes