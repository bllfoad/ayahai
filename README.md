<img src="https://i.imgur.com/fG6jyQT.png" width="300">

# Ayah**Ai** VER 1.0,

## Quran Ayah Detection and Annotation using YOLOv5

#### By Mushafalummah© 

## English: [ENGLISH DOC](https://drive.google.com/file/d/1bjlEN76qC1Qzi_3Zd0N04nYMKycSMUuV/view?usp=share_link "ENGLISH DOC")
## Arabic: [عربي](https://drive.google.com/file/d/1wvMPx9cpcXDkMdIrvoLLuf21uKRgx3pb/view?usp=share_link "عربي")
## Turkish: [TURKISH](https://drive.google.com/file/d/1DwHovIt0UrqZJ23FcppWiOHUrDpJ7LAV/view?usp=share_link "TURKISH")
## Malaysian: [MALAYSIAN](https://drive.google.com/file/d/1ronQZ8nTSBPSD7Trgyy05Kstk8ONqwJj/view?usp=share_link "MALAYSIAN")

### **This document provides a detailed tutorial on how to use a Python project that detects and annotates ayahs in images of Quran pages using the YOLOv5 object detection model. The project comprises multiple files, including base\_utils.py, global\_info.py, line.py, page.py, and ayahai.py.**

# **Requirements**

To use this project, you need to have the following installed:

- Python 3.10
- OpenCV (opencv-python)
- Pillow
- PyTorch
- Torchvision
- Tkinter
- Pandas

**Install the Tkinter manually `pip install tkinter` and ,**
**You can install the rest  required packages using the following command:**

`pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt`


**Additionally**, you will need the pre-trained YOLOv5 with **Pytorch** **format** model weights within a file named **model1.pt**.


**Setting up the development environment**

I recommend using PyCharm for the development environment. To set up the project in PyCharm, follow these steps:

- Download and install PyCharm.
- Create a new PyCharm project with a virtual environment using Python 3.10 as the interpreter.
- Open the terminal in PyCharm and run the following command to install the required packages:

`pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt`


# **Project Structure**

The project is organized into the following files:

- **base_utils.py**: Contains utility functions for the project.
- **global_info.py**: Defines a class that keeps track of the surah and ayah numbers throughout the processing.
- **line.py**: Defines a class representing a single line in a Quran page.
- **page.py**: Defines a class representing an entire Quran page.
- **ayahai.py**: The main script that ties everything together and processes images.



# **Usage**

To use the project, follow these steps:

- Prepare a folder containing images of Quran pages in JPEG, JPG, or PNG format.
- Run ayahai.py in PyCharm.
- When prompted, select the folder containing the images.
- Enter the number of lines on **each page**, the **first page**, and the **last page** when prompted.

The script will process each image, detect and annotate ayahs, and save the annotated images in an output\_full folder within the selected folder.




# **Sneak Peek and Explanation of Each File**


- Base\_utils.py 

This file contains utility functions to be used in the project.


- Global_info.py

This file defines the GlobalInfo class, which is responsible for maintaining the surah and ayah numbers throughout the processing of the images.



- line.py

This file defines the Line class, which represents a single line in a Quran page. It contains methods to skip a line, sort ayahs within a line









- Page.py

This file defines the Page class, which represents an entire Quran page. It contains methods to sort ayahs into lines and generate bounding boxes for the detected ayahs, This class initializes a Page object with the given number of lines, predictions, image path, and global information object. It then creates the lines, sorts the predictions into the appropriate lines, and generates bounding boxes for the ayahs detected on the page.

- ayahai.py

This file is the main entry point of the Quran Ayah detection and numbering application. It loads the model, processes the images, and generates the output images with the detected ayahs and their numbers.



We hope you find this tool helpful in your Quranic studies. If you need any assistance or have any questions, please don't hesitate to contact us. We are always happy to help and support your journey.

May Allah bless you and guide you on the right path.

Best regards,


# **Bllfoad**, **Mushafalummah**

<img src="https://i.imgur.com/Vez4oz4.png" width="200">


