from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
def index(request):
    return render(request,"myapp/index.html")
def fruits(request):
    return render(request,"myapp/fruits.html")
def add(request):
    if request.method=='GET':
        a = request.GET["a"]
        b = request.GET["b"]
        result=int(a)+int(b)
        return JsonResponse({'ret':result})
    else:
        a=request.POST['a']
        b=request.POST['b']
        result = int(a) + int(b)
        return JsonResponse({'ret': result})


