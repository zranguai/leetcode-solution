import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img = "zidane.jpg"


# Inference
results = model(img)
results.print()  # or .show(), .save()












