# %%
from pathlib import Path

# os.makedirs(pretrainedDir,exist_ok=True)

# # Set custom cache directory
# settings.update({'weights_dir': pretrainedDir})

from ultralytics import YOLO


# %%
# import pretrained model from cache

# ==============================
#           Parameters
# ==============================
pretrainedDir = 'pretrained/' #  directory for pretrained model
model_name = 'yolo11n' # model name
datasetYaml = 'datasets/blind_detect/data.yaml' # config file of dataset

# %%
# load pretrianed model

model_path = Path(pretrainedDir) / f'{model_name}.pt'
model = YOLO(model=model_path)

# %%

# ==============================
#             Train
# ==============================

# train with data from Roboflow Universe - Blind assistance system Dataset 

result = model.train(
    data=Path(datasetYaml),
    epochs=10,
    imgsz=640,
    batch=16,
    name='testing'
)


# %%
# load best model
best_model_path = result.save_dir / 'weights' / 'best.pt'
model = YOLO(best_model_path)

# export to onnx model 
# fix model input size to 640
model.export(format="onnx", imgsz=640, dynamic=False)



