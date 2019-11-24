from django.shortcuts import render

# Create your views here.

from app.models import IMG
from django.conf import settings
from app import main
def uploadImg(request):
    """
    图片上传
    :param request: 
    :return: 
    """
    context = {}
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name
        )
        new_img.save()
        context["imgurl"] = "http://oken.club:81" + "/media/" + new_img.img.name
        context["data"] = main.main(context["imgurl"])
    return render(request, 'app/upload.html', context)
