from django.shortcuts import render_to_response, redirect, render
from django.template.context_processors import csrf
from django.conf import settings
from upload_form.models import FileNameModel
import sys, os
UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'

def form(request):
    if request.method != 'POST':
        c = {}
        c.update(csrf(request))
        return render(request, 'upload_form/form.html')

    file = request.FILES['file']
    #path = os.path.join(settings.BASE_DIR, file.name)
    path = os.path.join(UPLOADE_DIR, file.name)
    destination = open(path, 'wb')

    for chunk in file.chunks():
        destination.write(chunk)

    insert_data = FileNameModel(file_name = file.name)
    insert_data.save()

    return redirect('upload_form:complete')

def complete(request):
    return render(request, 'upload_form/complete.html')
