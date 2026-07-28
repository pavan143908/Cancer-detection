from django.shortcuts import render
from .models import Cancer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import re
from .models import Cancer
from . upload import process

# Create your views here.

homepage = "home.html"
aboutpage = "about.html"
uploadpage = "upload.html"
resultpage = "result.html"
liverpage = "liverupload.html"
breastpage = "breastupload.html"
cervicalpage = "cervicalupload.html"


def home(request):
    return render(request, homepage)


def about(request):
    return render(request, aboutpage)


def upload(request):
    return render(request, uploadpage)


def liver(request):
    if request.method == "POST":
        m1path = 'app/models/liver models/CNN.h5'
        m2path = 'app/models/liver models/mobilenet.h5'
        pathss = os.listdir(r"app/Dataset/liver data/test")
        classes = []
        for i in pathss:
            classes.append(i)
        m = int(request.POST['alg'])
        File = request.FILES['imag']

        resulttt, imgp = process(
            m, File, classes, path1=m1path, path2=m2path)
        return render(request, resultpage, {"result": resulttt, "path1": imgp})

    return render(request, liverpage)


def breast(request):
    if request.method == "POST":
        m1path = 'app/models/breast models/CNN.h5'
        m2path = 'app/models/breast models/mobilenet.h5'
        pathss = os.listdir(r"app/Dataset/breast cancer data/test")
        classes = []
        for i in pathss:
            classes.append(i)
        m = int(request.POST['alg'])
        File = request.FILES['imag']

        resulttt, imgp = process(
            m, File, classes, path1=m1path, path2=m2path)
        return render(request, resultpage, {"result": resulttt, "path1": imgp})
    return render(request, breastpage)


def cervical(request):
    if request.method == "POST":
        pathss = os.listdir(r"app/Dataset/cerivical data/test")
        classes = []
        for i in pathss:
            classes.append(i)
            print(classes)
        m1path = 'app/models/cervical models/CNN.h5'
        m2path = 'app/models/cervical models/mobilenet.h5'

        m = int(request.POST['alg'])
        File = request.FILES['imag']

        resulttt, imgp = process(
            m, File, classes, path1=m1path, path2=m2path)
        return render(request, resultpage, {"result": resulttt, "path1": imgp})
    return render(request, cervicalpage)

