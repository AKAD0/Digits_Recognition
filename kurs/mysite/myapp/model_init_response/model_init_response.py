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
from ..img_load import img_load

class model:
    flag = 0
    mlp = 0
    X_train = 0
    y_train = 0
    X_test = 0
    y_test = 0

    def model_init_response(request):
        model.mlp, model.X_train, model.y_train, model.X_test, model.y_test = model.model_init()
        score = model.model_val(model.mlp,
                                model.X_train,
                                model.y_train,
                                model.X_test,
                                model.y_test)
        model.flag = 1

        return HttpResponse("""
        <html>
        <script>
        alert("Model initialized! Test set score: {:.3f}");
        window.location.replace('/app');
        </script>
        </html>
        """.format(score))


    def model_init():
        
        #loading dataset and splitting data to train and test sets
        X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
        X = X/255
        X_train, X_test, y_train, y_test = train_test_split(X,y, stratify=y, random_state=42)

        #model initialization and building
        mlp = MLPClassifier(hidden_layer_sizes=(50, ), max_iter=10, alpha=1e-4, 
                        solver='sgd', verbose=True, random_state=1, learning_rate_init=.1)
        mlp.fit(X_train, y_train)

        return(mlp, X_train, y_train, X_test, y_test)


    def model_val(mlp, X_train, y_train, X_test, y_test):
        #model validation
        print("Training set score: {:.3f}".format( mlp.score(X_train, y_train)))
        score = mlp.score(X_test, y_test)
        print("Test set score: {:.3f}".format(score))
        return(score)