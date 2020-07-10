import os
import json
import cv2
import codecs
import requests
import numpy as np
import pandas as pd 
from PIL import Image
from tqdm import tqdm
from io import BytesIO

path='C:\\VIT\\SET\\CODE\\darkflow-master\\new_model_data\\Images'
jsonData = []
JSONPATH = 'C:\\VIT\\SET\\CODE\\darkflow-master\\new_model_data\\face_detection.json'
with codecs.open(JSONPATH, 'rU', 'utf-8') as js:
    for line in js:
        jsonData.append(json.loads(line))

print(f"{len(jsonData)} image found!")

print("Sample row:")
print(jsonData[0]['annotation'])
k=0
for data in tqdm(jsonData):
    response = requests.get(data['content'])
    img = np.asarray(Image.open(BytesIO(response.content)))
    rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imwrite('Images\\img{:>05}.jpg'.format(k),rgb_img)
    k=k+1
    #cv2.imshow('img',rgb_img)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()  