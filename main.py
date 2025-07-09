# from ultralytics import YOLO

# # === CONFIG ===
# MODEL_NAME = 'yolov8n.pt'  # You can also try 'yolov8s.pt', 'yolov8m.pt', etc.
# DATASET_PATH = './Waiter/handraised/data.yaml'  # Your dataset YAML file path
# EPOCHS = 50
# BATCH_SIZE = 16
# DEVICE = '0'  # GPU 0, or 'cpu' if no GPU
# SAVE_PATH = 'yolov8_hand_raise.pt'

# # === LOAD PRE-TRAINED YOLO MODEL ===
# model = YOLO(MODEL_NAME)

# # === TRAIN ===
# model.train(
#     data=DATASET_PATH,
#     epochs=EPOCHS,
#     batch=BATCH_SIZE,
#     device=DEVICE
# )

# # === SAVE THE MODEL ===
# model.save(SAVE_PATH)

# print(f"Fine-tuned model saved as {SAVE_PATH}")
import torch
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

