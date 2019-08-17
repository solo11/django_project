from django.shortcuts import render,redirect
from .models import short_urls
from .forms import UrlForm,search
from .shortner import shortner

# Create your views here.

def Home (request,token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

def Search(request):
    form = search(request.POST)
    var=""
    if request.method =='POST':
        if form.is_valid():
            if form.data['URL']:
                l_url = form.data['URL']
            ss = short_urls.objects.filter(long_url=l_url).first()
            if ss==None:
                var = 'URL DOES NOT EXISTS'
            else:
                var=ss.short_url
            
        else:
            form = search()
            var = 'invakld'
    return render(request, 'search.html', {'form':form, 'a':var})

def short_main (request):
    form = UrlForm(request.POST)
    a=""
    cn = True
    if request.method == 'POST':
        cn=True
        if form.is_valid():
            long = "127.0.0.1:8000/s/"
            if form.data['short_url'] :
                c_url = form.data['short_url']
                
                if short_urls.objects.filter(short_url=c_url).exists():
                    
                    a = "custom URL exists already"
                    cn = False
                else:
                    a = c_url
            else:
                a = shortner().issue_token()
            if(cn):
                New_url = form.save(commit=False)
                New_url.short_url = a
                a=long+a
                New_url.save()
        else:
            form = UrlForm()
            a = 'invalid URL / URL exists already'
    return render(request, 'short.html', {'form':form , 'a':a})