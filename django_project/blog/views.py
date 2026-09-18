import datetime

from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {'auther':'John dou',
     'title' :'John dou\'s blog',
     'content':'John dou first blog.........',
     'date_posted':datetime.date.today()
     },
     {'auther':'Steven byard',
     'title' :'Steven byard\'s blog',
     'content':'Steven byard first blog.........',
     'date_posted':datetime.date.today()
     },
    {'auther':'Bob hone',
     'title' :'Bob hone\'s blog',
     'content':'Bob hone first blog.........',
     'date_posted':datetime.date.today()
     }
]

# Create your views here.
def home(request):
    context = {'posts':posts}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})