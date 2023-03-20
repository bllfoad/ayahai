import json
import cv2
import torch
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from tools.page import Page
from tools.global_info import GlobalInfo

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model1.pt')
model.conf = 0.4
model.iou = 0.1

root = tk.Tk()
root.withdraw()

global_info = GlobalInfo()

# Ask the user to select a folder
folder_path = filedialog.askdirectory()

lines_each_page = int(input("How many lines in each page? "))
lines_first_page = int(input("How many lines in the first page? "))
lines_last_page = int(input("How many lines in the last page? "))

# Get all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
numpages = len(image_files)

# Initialize the arrange counter
arrange_counter = 0

for i, image_file in enumerate(image_files):
    # Load the image
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)

    # Perform inference
    results = model(image, size=1200)
    # add pgui progress bar
    print(f'Processing image {i + 1} of {len(image_files)}')

    # Post-process the results)
    predictions = results.pandas().xyxy[0].to_dict(orient="records")
    for prediction in predictions:
        prediction['xmin'] = round(prediction['xmin'])
        prediction['ymin'] = round(prediction['ymin'])
        prediction['xmax'] = round(prediction['xmax'])
        prediction['ymax'] = round(prediction['ymax'])
        prediction['confidence'] = round(prediction['confidence'], 2)

    if i == 0 or i == 1:
        numlines = lines_first_page
    elif i == (numpages - 1):
        numlines = lines_last_page
    else:
        numlines = lines_each_page
    pg = Page(numlines, predictions, image_path, global_info)
    boxes = pg.generate_boxes()

    # Show the image with predictions and save it
    img = cv2.imread(image_path)
    print(f'naming image {i + 1} of {len(image_files)}')

    for box in boxes:
        x, y, w, h = box["box"]
        arrange = box['ayah_number']
        # red color
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, f'arrange:{arrange}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 255, 0), 2)

    print(f'saving image {i + 1} of {len(image_files)}')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # create output directory in folder path thn save the image
    if not os.path.exists(os.path.join(folder_path, 'output_full')):
        os.makedirs(os.path.join(folder_path, 'output_full'))
    cv2.imwrite(os.path.join(folder_path, 'output_full', f'{i}.jpg'), img)

    # # Update the arrange counter for the next image
    # if sorted_predictions:
    #     last_prediction = sorted_predictions[-1]
    #     arrange_counter = last_prediction['arrange']

print('صلي الله عليه وسلم')