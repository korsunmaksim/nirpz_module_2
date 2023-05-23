from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,Image

def gallery_view(request):  
    categories= Category.objects.all()
    return render(request, 'gallery.html',{"categories":categories})


def image_detail(request,pk):
    image=Image.objects.filter(id=pk).first()
    if not image:
        return HttpResponse( "<h1>No image!</h1>")
    return render(request,"image_detail.html",{"image":image})
