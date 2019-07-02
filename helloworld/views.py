from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

# 매핑 개념(템플릿 디렉토리로 이동)
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html')

def hello2(request, id=0):
    return HttpResponse(f'id:{id}')

def hello3(request):
    jsonresult = {
        'result':'success',
        'data':['hello','world','nice',True,(1,2,3)]
    }
    return JsonResponse(jsonresult)

def counter_add(request):
    c = Counter()
    c.groupno=1
    c.depth=1
    c.orderno=1
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3
    c.save()

    return HttpResponse('ok')

# 맥스 그룹번호
def counter_max(request):
    value = Counter.objects.aggregate(max_groupno=Max('groupno'))
    max_groupno = 0 if value['max_groupno'] is None else value['max_groupno']
    return HttpResponse(f'max group >> {value["max_groupno"]}')

# 쿼리셋 예제
# __gt ~보다 크다, __lt ~보다 작다
# F() = 현재 객체 like this
def counter_update(request):
    # groupno = 1, orderno >= 2의 모든 게시물 orderno+=1
    list = Counter.objects.filter(groupno=1).filter(orderno__gte=2).update(orderno=F('orderno')+1)

    return HttpResponse('ok')