# ✋ Hand Raise Detection with YOLOv8

This project detects raised hands in a video and identifies the person based on their position. It uses a **fine-tuned YOLOv8 model** and overlays the corresponding name on the video when someone raises their hand.

---

## 📸 Demo

![demo](demo.gif)

---

## 🔧 Features

- 🎯 Real-time hand raise detection
- 🧠 Uses Ultralytics YOLOv8 (fine-tuned for hand detection)
- 👤 Name mapping based on screen position
- 📹 Works with prerecorded video files
- 💾 Saves annotated video output

---

## 🗂️ Folder Structure

```

├── hand\_raise\_detection/
│   ├── input/                                                         # Input videos
│   ├── output/                                                       # Processed videos with name overlays
│   ├── yolov8\_hand_raise.pt                                         # Fine-tuned YOLOv8 model
│   ├── main.py                                                        # Main detection script
│   ├── Finetune YOOv8 on handraised dataset.ipynb                    # Finetuning YOLOv8 script
│   ├── names.jpg                                                     # Names
│   └── README.md                                                    # Project description

````

---

## 🚀 How to Run

### 🔨 1. Install Dependencies

```bash
pip install ultralytics opencv-python
````

### 🧠 2. Run Detection on Video

```bash
python main.py --input video/input_video.mp4 --output outputs/output_with_names.mp4
```

Or directly modify paths in `main.py`:

```python
VIDEO_PATH = 'video/input_video.mp4'
OUTPUT_PATH = 'outputs/output_with_names.mp4'
MODEL_PATH = 'yolov8_hand_raise.pt'
```

---

## 🧪 Example Output

When a hand is raised in the video, the corresponding person's name is shown in the **top-right** of the frame:

```
[ ✓ ] Detected raised hand
[ 👤 ] Identified: MUFRAD
```

---

## 🧠 Model Training (YOLOv8 Fine-Tuning)

Want to train your own model?

```bash
yolo task=detect mode=train model=yolov8n.pt data=handraised/data.yaml epochs=50 imgsz=640 batch=16
```

> Ensure your dataset is in YOLO format with annotated hand positions.

---

## 👁️ Person-Name Mapping Strategy

Names are assigned based on the position (X and Y) of the hand in the frame:

```python
position_to_name = [
    (600, 630, 550, 580, 'TANVIR'),
    (750, 780, 530, 590, 'SHAFAYET'),
    ...
]
```

You can customize this based on your frame layout or automate name mapping with face recognition.

---

## 🙌 Acknowledgements

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
