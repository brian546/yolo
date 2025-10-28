
## Environment Setup

```bash
conda create -n yolo python=3.12
conda activate yolo
pip install torch ultralytics ipykernel

```

## Dataset
- Download dataset from Roboflow (https://universe.roboflow.com/yolov4-lcs89/blind-assistance-system/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)
- Name it as "blind_detect", 
- And place it under directory datasets



## Run code 

```bash
python train.py

```