import PySimpleGUI as sg
import subprocess
import os
##import torch

##device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
##print(torch.cuda.get_device_name(device))

def run_yolov8(model, source, show):
    cmd = f'python predict.py model={model} source="{source}" show={show}'
    yolov8_folder = os.path.join(os.getcwd(), 'YOLOv8-DeepSORT-Object-Tracking/ultralytics/yolo/v8/detect')  # Replace 'yolov8' with the folder containing your 'predict.py'
    process = subprocess.Popen(cmd, shell=True, cwd=yolov8_folder, creationflags=subprocess.CREATE_NEW_CONSOLE)
    return process



# Layout
layout = [
    [sg.Text('Video Source:'), sg.InputText(key='source', default_text='Select video', disabled=True), sg.FileBrowse(file_types=(("Video Files", "*.mp4"),))],
    [sg.Checkbox('Show Output', default=True, key='show')],
    [sg.Button('Run YOLOv8'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('Automatic Maritime Vessel Counter', layout)

# Event loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Run YOLOv8':
        model = 'best.pt'
        source = values['source']
        show = 'True' if values['show'] else 'False'
        print ("Loading Predict model...")
        run_yolov8(model, source, show)
        
        print ("Done, output video saved to files")
        

window.close()
