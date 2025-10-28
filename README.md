## Dataset
- Make directory "datasets" in the working directory to store datasets
- Download dataset "blind-assistance-system" from Roboflow (https://universe.roboflow.com/yolov4-lcs89/blind-assistance-system/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)
- Decompress, name as "blind-assistance-system" and place it under directory "datasets"


## Environment Setup

```bash
conda create -n yolo python=3.11
conda activate yolo
pip install torch ultralytics onnx ipykernel

```



## Run code 

Open `train.ipynb` and run it.

