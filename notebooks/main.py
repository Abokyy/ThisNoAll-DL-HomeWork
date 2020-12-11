# pip install cython pyyaml==5.1
# git clone https://github.com/facebookresearch/detectron2.git
# pip install torch===1.7.0 torchvision===0.8.1 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
# python -m pip install -e detectron2
# pip install opencv-python

import detectron2.detectron2
from detectron2.detectron2 import model_zoo
from detectron2.detectron2.utils.logger import setup_logger
from detectron2.detectron2.engine import DefaultPredictor
from detectron2.detectron2.config import get_cfg
from detectron2.detectron2.utils.visualizer import Visualizer
from detectron2.detectron2.data import MetadataCatalog
setup_logger()
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
import sys,os

#sys.path.append(os.path.abspath('../notebooks'))
import image_predictor
import video_reader
import visualizer


def main():
    detector,cfg = image_predictor.download_model('B:/BME/github/ThisNoAll-DL-HomeWork/detectron2/configs')
    video_reader.read_video('B:/BME/github/ThisNoAll-DL-HomeWork/input/threemincut.mp4')


if __name__ == "__main__":
    main()