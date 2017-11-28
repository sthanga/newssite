import feedparser
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.syndication.views import Feed
from newsapp.models import NewsLink

# Create your views here.
def index(request):
	#passing lis of docts to templates 
	link = NewsLink.objects.get(id=1)
	feed = feedparser.parse(link.rss) #'http://zeenews.india.com/tamil/india.xml'

	return render(request,'base.html',{'feed': feed} )


