from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from callfile.SMA import *

url = ""

def index(request):
    return render(request, 'index.html')

def upload_file(request):
    #file upload
    if request.method == 'POST':
         uploaded_file = request.FILES['smapy']
         #uploaded_csv_file = request.FILES['csv_file']
         fs = FileSystemStorage()
         fs.save(uploaded_file.name, uploaded_file)
         #name_csv = fs.save(uploaded_csv_file.name, uploaded_csv_file)

    x = int(request.POST.get('nod', 'default'))
    dict = callthisfunc(x)
    return render(request, 'upload_file.html', dict)
