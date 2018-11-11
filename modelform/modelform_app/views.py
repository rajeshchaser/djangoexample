from django.shortcuts import render,redirect
from modelform_app.forms import newuser

def index(req):
    return render(req,"modelform_app/index.html")

# Create your views here.
def form_view(req):
    form=newuser()
    if req.method=="POST":
        form=newuser(req.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print('error form invalid')
    return render(req,"modelform_app/formpage.html",context={'form':form})
