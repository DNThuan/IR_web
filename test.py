from unittest.mock import patch
import numpy as np


path = "/home/thuan/Desktop/IR_web/data/dataset/oxford5k/ResNet101_features.npy"
with open(path,"rb") as f:
    data = np.load(f)

print(data.shape)