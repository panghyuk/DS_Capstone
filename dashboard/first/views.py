from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.utils import timezone
# 2-1 POST 형식의 HTTP 통신만 받기
from django.views.decorators.http import require_POST
# 2-2 response를 변환하는 가장 가본 함수, html 파일, 이미지 등 다양한 응답
from django.http import HttpResponse
# 2-3 딕셔너리를 json 형식으로 바꾸기 위해
import json

def showmain(request):
    return render(request, 'first/mainpage.html')
