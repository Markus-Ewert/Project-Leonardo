import logging
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import LeonardoProject.predictions as preds

logger = logging.getLogger(__name__)


def dashboard(request):
    return render(
        request,
        'dashboard.html'
    )


def predictions(request):

    kmeans = "No file chosen"
    logrec = "No file chosen"
    svm = "No file chosen"
    rnn = "No file chosen"

    if request.method == 'POST' and 'kmeans' in request.FILES:
        data = request.FILES['kmeans']
        fs = FileSystemStorage()
        fs.delete("LeonardoProject/files/kmeans.csv")
        filename = fs.save("LeonardoProject/files/kmeans.csv", data)
        kmeans = filename
    elif request.method == 'POST' and 'logistic' in request.FILES:
        data = request.FILES['logistic']
        fs = FileSystemStorage()
        fs.delete("LeonardoProject/files/logistic.csv")
        filename = fs.save("LeonardoProject/files/logistic.csv", data)
        logrec = filename
    elif request.method == 'POST' and 'svm' in request.FILES:
        data = request.FILES['svm']
        fs = FileSystemStorage()
        fs.delete("LeonardoProject/files/svm.csv")
        filename = fs.save("LeonardoProject/files/svm.csv", data)
        svm = filename
    elif request.method == 'POST' and 'rnn' in request.FILES:
        data = request.FILES['rnn']
        fs = FileSystemStorage()
        fs.delete("LeonardoProject/files/rnn.csv")
        filename = fs.save("LeonardoProject/files/rnn.csv", data)
        rnn = filename

    context = {
        'kmeans': kmeans,
        'logreg': logrec,
        'svm': svm,
        'rnn': rnn
    }

    return render(
        request,
        'predictions.html',
        context,
    )


def training(request):



    return render(
        request,
        'training.html'
    )


def train_svm(request):
    if filename == "":
        print("No file was given")
    else:
        print("Initiating SVM")

    return render(
        request,
        'training.html'
    )


def train_kmeans(request):
    if filename == "":
        print("No file was given")
    else:
        print("Initiating SVM")

    return render(
        request,
        'training.html'
    )

def predict_kmeans(request):

    prediction = preds.predict_svm()

    context = {
        'machines': prediction['machines'],
        'classes': prediction['classes'],
        'range': prediction['range']
    }

    return render(
        request,
        'svm.html',
        context
    )

from django import template
register = template.Library()