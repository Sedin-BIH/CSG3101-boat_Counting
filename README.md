# CSG3101-boat_Counting
The Repository involves the yolov8 algorithm developed by Ultralytics, connected to the deepsort algorithm. A python notebook containing steps for training, a GUI and the SIngapore Maritime Dataset in YOLO format.

One of the key deliverables of the Project is: A compressed file of labelled data and dataset for either the Fisheries Dataset or Singapore Maritime Dataset.
Below is a link to a Google Drive containing the Compressed file of the Singapore Maritime Dataset.
https://drive.google.com/drive/folders/13iedvAj6RTGr7j9CryArhS_Se16AD-AZ?usp=sharing

The training, validation and Testing components are split into the following:
70% for training, 20% for validation and 10% for testing. If you are looking to use your own dataset i.e the Recreational Boat Fishing Dataset it must be in YOLO format with Frames seperated and labels in a seperate .txt file as seen in the Compressed Zip File of the Singapore Maritime Dataset.

Deep-SORT will need to be installed using this link due to the large size of the file: https://drive.google.com/drive/folders/17cNkHHhImjZ2-mnd8XfYnCSFeh8pCvkf?usp=share_link

The trained weights on the dataset can also be found in this link: https://drive.google.com/file/d/1G4ek_D5-cZJsxySJsetkGfgbGHGVW2kD/view?usp=sharing

Quick start guide: 
1. Download and extract the repository, the "Yolov8-DeepSORT-Object-Tracking" folder along with the "gui.py" file should be placed seperated in your default user file system (for example: C:\Users\admin).
2. Install deep-Sort from the above link.
3. In CMD run "cd YOLOv8-DeepSORT-Object-Tracking", then "pip install -r requirements.txt"
4. Download the weights from the above link and place them in the folder: "YOLOv8-DeepSORT-Object-Tracking\ultralytics\yolo\v8\detect"
5. Double click the gui.py file in your file stystem to launch the GUI. Here you can select whether to show a live input or not.
6. A TXT file of the results (vessel_counts.txt) can be found in: "YOLOv8-DeepSORT-Object-Tracking\ultralytics\yolo\v8\detect" once processing is complete. A MP4 file of the processed video can be found in "YOLOv8-DeepSORT-Object-Tracking\runs\detect" in the relevant sub folder (train1, train2, etc...)

If an error occurs, troubleshooting can be done by opening CMD and running: "cd YOLOv8-object-tracking-blurring-counting/ultralytics/yolo/v8/detect" then place a video named "test1.mp4" in that folder for testing purposes.
Run "python predict.py model=best.pt source="test1.mp4" show=True"
If an error occurs it will generally be due to packages not installed or packages being out of date. Identify the problem packages in the error read out and rectify the issue with "pip install ...".
