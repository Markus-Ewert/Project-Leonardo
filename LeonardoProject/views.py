from django.shortcuts import render
import LeonardoProject.training as train
from django.core.files.storage import FileSystemStorage

def training(request):

    svm = ""

    if request.method == 'POST' and 'svm' in request.FILES:
        data = request.FILES['svm']
        fs = FileSystemStorage()
        fs.delete("LeonardoProject/files/svm_train.csv")
        filename = fs.save("LeonardoProject/files/svm_train.csv", data)
        svm = "Uploaded successfully!"

    context = {
        'svm': svm,
    }

    return render(
        request,
        'training.html',
        context
    )


def train_svm(request):

    success = train.train_svm()

    context = {
        'success': success
    }

    return render(
        request,
        'training.html',
        context
    )




