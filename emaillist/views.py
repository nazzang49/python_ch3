from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist

def index(request):
    # -id = id 컬럼을 거꾸로 출력(가장 최근 데이터부터)
    # select
    emaillist = Emaillist.objects.all().order_by('-id')
    data={
        'emaillist':emaillist
    }
    return render(request,'emaillist/index.html',data)

def form(request):
    return render(request,'emaillist/form.html')

def add(request):
    # vo 객체 만드는 것과 유사 개념
    # insert
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save()

    # 메인으로 이동
    return HttpResponseRedirect('/emaillist')