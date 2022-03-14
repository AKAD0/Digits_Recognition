from django.http import HttpResponse
from django.shortcuts import render #Allows to render html
#Model creating
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
#Model exploitation
import imageio as io
#Modules
from ..model_init_response import model_init_response
from ..img_load import img_load

def img_recognition(request):
    
    if (model_init_response.model.flag == 1):
        #load image
        img = img_load.img.data

        #prediction
        mlp = model_init_response.model.mlp
        if (img.shape[0] == 784):
            y_predict = mlp.predict(img.reshape(1,-1))
            print( y_predict)
        else:
            print('Images size isnt 28x28')

        return HttpResponse("""
        <html>
        <script>
        alert("The digit on the image is: {}");
        window.location.replace('/app');
        </script>
        </html>
        """.format( y_predict))
    else:
        return HttpResponse("""
        <html>
        <script>
        alert("Image wasn't loaded and/or model wasn't initialized. Try it first.");
        window.location.replace('/app');
        </script>
        </html>
        """)