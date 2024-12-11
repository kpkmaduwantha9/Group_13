from django.shortcuts import render

def hkvhome(request):
    return render(request,'hkv/HKVhome.html',{})