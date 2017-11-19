from django.shortcuts import render,redirect
from .forms import ShortUrlForm
from . import shortener
from .models import URLDB
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    form = ShortUrlForm()
    if request.method == 'POST':
        form = ShortUrlForm(request.POST) 
        if form.is_valid():
            
            flag = True
            while True:
                try:
                    o=form.save(commit=False)
                    break
                except:
                    print('Unique Constraint Voilated')
                    flag = False
                    break
            while True and flag:
                try:
                    shortUrl = shortener.shorten()
                    o.shortenedUrl = shortUrl
                    o.save()
                    break
                except:
                    print('Duplicate shortUrl trying again...')
            
            return home(request) if flag else render(request,'baseApp/index.html',{'form':form})

        else:
            print('invalid') 
    else:
        print('Denied')    
    return render(request,'baseApp/index.html',{'form':form})
def home(request):
    lst = URLDB.objects.all()
    
    return render(request,'baseApp/home.html',{'allUrls':lst})
def mapIt(request):
    key = request.get_full_path()[1:]
    origUrl = URLDB.objects.filter(shortenedUrl=key).values('originalUrl')[0]['originalUrl']
    
    print(origUrl)
    if origUrl[:11] == 'http://www.' or origUrl[:12] == 'https://www.' or origUrl[:8] == 'https://':
        return redirect(origUrl)
    if origUrl[:4] == 'www.':
        origUrl = origUrl[4:]
    origUrl  = 'http://www.'+origUrl
    return redirect(origUrl)
