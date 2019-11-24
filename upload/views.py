from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .forms import UploadFileForm
import os

from django.core.exceptions import ValidationError
attempted = 0
successful = 0
msg = ""
def upload_file(request):
    global attempted
    global successful
    global msg
    msg = ""
    attempted = 0
    successful = 0
    if request.method == 'POST':
        '''form = UploadFileForm(request.POST, request.FILES)'''
        '''if form.is_valid():'''
        for filename, file in request.FILES.items():
            # Do the incrementation
            attempted+=1

            
            if(handle_uploaded_file(request.FILES[filename])):
                successful+=1
        msg+="<p>Upload Summary: " + str(successful) + " successful out of " + str(attempted) + "."
        template = loader.get_template('upload/results.html')
        context = {'msg': msg}
        return HttpResponse(template.render(context, request))
            #return HttpResponseRedirect('/successful/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html')
    #return render(request, 'upload/upload.html',) #{'form' : form})

def handle_uploaded_file(f):
    global msg
    maximum = 500000
    file_path = '/home/webtech/django/assignment6/media/' + str(f.name)
    name = str(f.name)
    name2, extension = os.path.splitext(f.name)

    if os.path.isfile(file_path):
        msg += "<p>Sorry, <b>media/" + str(f.name) + "</b> already exists."
        return False
    
    if extension != '.jpg' and extension != '.png':
        msg+= "<p>Sorry, only JPG and PNG files are allowed, not <b>" + str(f.name) + "</b>"
        return False

    # Do HTISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    filesize = f.read()
    if len(filesize) > maximum:
        msg+="<p>Sorry, file <b>" + str(f.name) + "</b> is too large (" +                     str(len(filesize)) + " > " + str(maximum) + ")."
        return False

    with open('/home/webtech/django/assignment6/media/' + str(f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    msg+="<p>The file <b>" + str(f.name) + "</b> has been uploaded (bytes = " +             str(len(filesize)) + ")."
    return True;


