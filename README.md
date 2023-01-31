#create-model.ipynb

This code creates the model.
The image is converted to RGB data and the image is resized to lighten the processing load.
The rest of the code is created by assembling the CNN code.

#predict file

The model assembled above is used to produce the judgment results.
The expected value as a percentage is also shown.
The def test() function is used to input the letters of the judgment result into the input image.

Execution command
python predict.py {image of pathname}


#training tage $ test-data

I mean it as it is.

The model .h5 file could not be uploaded because the amount of data was too large and exceeded the github limit.


use library

・python
・tensorflow
・Keras
・PIL
・OpenCV
・numpy
・
