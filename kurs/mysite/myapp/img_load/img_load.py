from django.http import HttpResponse
from django.shortcuts import render #Allows to render html
import tkinter
from tkinter import filedialog
import numpy as np
import imageio as io
#Modules
from ..model_init_response import model_init_response

class img:
    flag = 0
    data = 0

    def load_response(request):
        img.data = img.load()

        if ((img.data != 'cancelled') and
            (not np.all((img.data == 1))) and
            (not np.all((img.data == 0))) and
            (model_init_response.model.flag == 1) and
            (np.sqrt(img.data.shape[0]) == 28)):
            img.flag = 1
            return HttpResponse("""
            <html>
            <script>
            alert("Image loaded!");
            window.location.replace('/app');
            </script>
            </html>
            """)
        elif (img.data == 'cancelled'):
            img.flag = 0
            return HttpResponse("""
            <html>
            <script>
            alert("Image load was cancelled.");
            window.location.replace('/app');
            </script>
            </html>
            """)          
        elif (np.sqrt(img.data.shape[0]) != 28):
            img.flag = 0
            return HttpResponse("""
            <html>
            <script>
            alert("Error. Image isn't 28x28. Try again.");
            window.location.replace('/app');
            </script>
            </html>
            """)
        elif (np.all((img.data == 1))) or (np.all((img.data == 0))):
            img.flag = 0
            return HttpResponse("""
            <html>
            <script>
            alert("Error. Image is all white/black. Try again.");
            window.location.replace('/app');
            </script>
            </html>
            """)
        elif (model_init_response.model.flag != 1):
            img.flag = 0
            return HttpResponse("""
            <html>
            <script>
            alert("Error. Model wasn't initialized. Try it first.");
            window.location.replace('/app');
            </script>
            </html>
            """)

    def load():  
        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
        file = filedialog.askopenfilename()
        if file:
            src = io.imread( str( file))
            img_src = np.array(src)
            data = np.abs((np.ndarray.flatten(img_src)/255)-1)
            return(data)
        else:
            return('cancelled')