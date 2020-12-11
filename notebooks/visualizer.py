from detectron2 import detectron2
from detectron2.detectron2.utils.visualizer import Visualizer
from detectron2.detectron2.data import MetadataCatalog
import cv2


def visalize_img(img,outputs,cfg):
    v = Visualizer(img[:,:,::-1],MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    cv2.imshow(v.get_image()[:,:,::-1])