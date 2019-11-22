from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for filename, file in request.FILES.items():
                handle_uploaded_file(request.FILES[filename])
            #return HttpResponseRedirect('/successful/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form' : form})

def handle_uploaded_file(f):
    with open('/home/webtech/django/assignment6/media/' + str(f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


