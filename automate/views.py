from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageForm
from io import BytesIO
from PIL import Image
# Create your views here.
size = 360,500
def thumbnail(file):
    #check if file is svg and skip
    name=file._name
    if(name.find(".svg")!=-1):
        return file

    img = Image.open(file)

    img.thumbnail(size)

    files=BytesIO()
    img.save(files,"jpeg")
    file.size=files.tell()
    file.file=files
    file.seek(0)
    return file

@csrf_exempt
def addImage(req):
    try:
        req.FILES['image']=thumbnail(req.FILES['file'])
    except:
        req.FILES['image']=thumbnail(req.FILES['image'])
            
    instance = ImageForm(req.POST,req.FILES)
    instance.save()
    return HttpResponse('1')

def testImage(req):
    instance = ImageForm()
    html = f"""
    <form action='addImage' method="post" enctype="multipart/form-data"> {instance.as_p()}
    <input type='submit'/>
    </form>"""
    return HttpResponse(html)

