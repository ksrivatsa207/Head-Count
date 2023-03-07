import sys
from subprocess import call
def run_cmd(command):
        try:
            call(command, shell=True)
        except KeyboardInterrupt:
            print("Process interrupted")
            sys.exit(1)
#for detection
cmd="python ./yolo/detect.py --weights ./yolo/runs/train/exp37/weights/best.pt --classes 0 --project ./yolo/runs/detect/ --iou-thres 0.25 --source ./sdf.jpg --imgsz 800 --line-thickness 1 --hide-conf"
#for training
# cmd="python yolo/train.py --data coco128.yaml --weights '' --cfg yolov5s.yaml --img 640 --project ./yolo/runs/train/clg_ds --epochs 150 --batch 4 --device cpu"  # from scratch
# cmd="python yolo/export.py --weights ./mod.pth --include tflite --img 416"
run_cmd(cmd)