import feedparser
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.syndication.views import Feed

# Create your views here.
def index(request):
	#passing lis of docts to templates 

	feed = feedparser.parse('http://zeenews.india.com/tamil/india.xml')

	return render(request,'base.html',{'feed': feed} )


