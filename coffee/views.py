from django.shortcuts import render
from django.http import HttpResponse
from .models import background_video
from .models import cold_coffee
from .models import hot_coffe
from .models import juice
from .models import special_iteams
from .models import contactbox
from .models import about_page
from .models import about_page_right
# from .models import  fruit_juicess
# Create your views here.
def menu(request):

# background video 
    video1=background_video.objects.all()
    print(video1)
# image name price text
    first_img=cold_coffee.objects.all()
    hot_img=hot_coffe.objects.all()
    print(hot_img)
    jyuice_img=juice.objects.all()
    special_img=special_iteams.objects.all()

    aboutpage=about_page.objects.all()
    aboutpage_right=about_page_right.objects.all()
    # contact=contactbox.objects.all()
    # print(contact)
    if(request.GET.get('name') and request.GET.get('email') and request.GET.get and request.GET.get('message')):
        Name=request.GET.get('name')
        Email=request.GET.get('email')
        Message=request.GET.get('message')
        contactbox.objects.create(name=Name,email=Email,message=Message)
        a=contactbox.objects.all().values()
        print(a)
        
# contact 
    return render(request,('index.html'),{'video':video1,'first_page':first_img ,'second_page':hot_img,'third_page':jyuice_img,'special_iteams_page':special_img,'aboutpage1':aboutpage,'aboutpage_right':aboutpage_right})
                                                                                                            