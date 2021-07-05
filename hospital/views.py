from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    hos = Hospital.objects.all()
    context = {
        'hos': hos,
    }
    return render(request, template_name='hospital/main.html', context=context)


def hospital(request, hos_id):
    head_doctor = HeadDoctor.objects.get(id=hos_id)
    doctor = Doctor.objects.filter(hospital_id=hos_id)
    context = {
        'main': head_doctor,
        'doctor': doctor,
    }
    return render(request, template_name='hospital/index.html', context=context)


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, template_name='news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})
