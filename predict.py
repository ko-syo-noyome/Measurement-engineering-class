from keras.models import Sequential,load_model
import numpy as np
#import tensorflow
import keras ,sys
from PIL import Image
from sklearn import model_selection
import time
import cv2 
import numpy as np


classes=["ten","onehundred","fivehundred"]
num_classes=len(classes)
image_size=100


def text(text):
    path=sys.argv[1]
    img = cv2.imread(path)
    height, width = img.shape[:2]
    img = cv2.resize(img,(round(width/4), round(height/4)))
    imageText = img.copy()
    org = (0,30)
    cv2.putText(imageText, text, org, fontFace = cv2.FONT_ITALIC, fontScale = 1.2, color = (255,255,255))
    cv2.imshow("Image Text",imageText)
    cv2.imwrite('risult.jpg', imageText)
    cv2.waitKey(0)


def main():

    image=Image.open(sys.argv[1])
    image=image.convert('RGB')
    image=image.resize((image_size,image_size))
    data=np.asarray(image)
    X=[]
    X.append(data)
    X=np.array(X)
    model=load_model('./mefa-model.h5')
    result=model.predict([X])[0]
    predicted=result.argmax()
    print(predicted)
    precentage=int(result[predicted])*100
    print("{0} ({1} %)".format(classes[predicted],precentage))
    text(classes[predicted])
    


if __name__ == "__main__":
    
    main()


