from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def root(request):
    return HttpResponse('Server Started')
def index(request):
    return render(request, 'index.html')
def submitquery(request):
    q = request.GET['query']
    # return HttpResponse(q)
    # jsondict = {
    #     "q": q
    # }
    # return JsonResponse(jsondict)
    try:
        ans = eval(q)
        mydict = {
            "q": q,
            "ans": ans,
            "error": False,
            "result": True
        }
    except:
        mydict = {
            "error": True,
            "result": True
        }
    
    return render(request, 'index.html', context=mydict)