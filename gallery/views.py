from django.shortcuts import render, get_object_or_404

def gallery_view(request):   
    return render(request, 'gallery.html')


def image_detail(request,pk):
    print(pk)
    return render(request,"image_detail.html")
