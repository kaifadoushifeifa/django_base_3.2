import time

from django.shortcuts import render,HttpResponse
import json
# Create your views here.

def test(request):
    data1 = {
        'name':"周港",
        'age':24,
        'hobby':"打篮球",
    }
    retobj =HttpResponse(json.dumps(data1),content_type="application/json")
    retobj["Access-Control-Allow-Origin"] = "http://192.168.0.101:8080"
    retobj['Access-Control-Allow-Credentials'] = "true"
    retobj['SameSite'] = "None"
    retobj['Secure '] = ""
    request.session['login'] = True
    # print(request.POST.dict())
    print(request.COOKIES)
    return retobj

def test1(request):
    print(request.GET.dict())
    print(request.POST.dict())
    retobj =HttpResponse("ok",content_type="application/json")
    print(request.META)
    retobj["Access-Control-Allow-Origin"] = request.META['HTTP_ORIGIN']
    retobj['Access-Control-Allow-Credentials'] = "true"
    retobj['SameSite'] = "None"
    retobj['Secure '] = ""
    return retobj

def test2(request):

    return render(request,'test1.html')


def test3(request):
    print(request.GET.dict())
    return render(request,'tz.html')


def redis_ex(request):
    from django.core.cache import caches
    request.cache_time = 30
    cache = caches['view_cache']
    cache_key1 = 'redis_ex_time'
    # 引入缓存
    cache_ret = cache.get(cache_key1)
    if not cache_ret:
        typelist = time.time()
        cache.set(cache_key1, typelist, request.cache_time)
    else:
        typelist = cache_ret
    return HttpResponse(typelist)