from django.shortcuts import render,HttpResponse


from.forms import Myfileuploadform

# Create your views here.

def index(request):

    context = {
        'form': Myfileuploadform()
    }

    return render(request,'index.html',context)