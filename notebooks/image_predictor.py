from detectron2 import detectron2
from detectron2.detectron2 import model_zoo
from detectron2.detectron2.utils.logger import setup_logger
from detectron2.detectron2.engine import DefaultPredictor
from detectron2.detectron2.config import get_cfg
import os


def download_model(path):
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file(os.path.join(path,"COCO-Detection/faster_rcnn_R_50_C4_3x.yaml")))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.9
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(os.path.join(path,"COCO-Detection/faster_rcnn_R_50_C4_3x.yaml"))
    return DefaultPredictor(cfg),cfg