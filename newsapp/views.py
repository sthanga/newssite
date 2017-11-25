from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.syndication.views import Feed

# Create your views here.
def index(request):
	#passing lis of docts to templates 
	news = [
	{'title': 'item_title', 'description': 'This is the test2 description'},
	{'title': 'News 2', 'description': 'This is the test2 description'}
	]
	return render(request,'base.html',{'news': news} )




