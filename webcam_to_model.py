from ultralytics import YOLO
#from ultralytics import DetectionPredictor
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2


model = YOLO(r"C:\Users\ssica\Documents\coding shit\black_jack_v1\black_jack_models\best_new.pt")
#model = YOLO(r"C:\Users\ssica\Documents\coding shit\black_jack_v1\black_jack_models\best_old.pt")

model.predict(source="0", show=True, conf=0.3)