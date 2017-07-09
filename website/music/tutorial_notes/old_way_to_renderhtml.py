# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# which model/table you want to query
from .models import Album

# Create your views here.

def index(request):
	# connect to the database and retrieve all rows
	all_albums = Album.objects.all()

	# by default django is setup to look at templates directory in your app
	# why you don't right /templates/music

	template = loader.get_template('music/index.html')
	
	# dictionary of what you want to pass into your template
	context = { 'all_albums': all_albums,
	}

	# always make sure to pass in the request
	return HttpResponse(template.render(context,request))
	# in the html template
	# python code goes in between '{% %}'
	# variables go in between {{ }} 	



	# EXAMPLE, don't mix html / django code use a statics or templates folder for that stuff
	# html = ''
	# for album in all_albums:
	# 	# construct url based on id 
	# 	url = '/music/' + str(album.id) + '/'
	# 	html += '<a href=" ' + url + '">' + album.album_title  + '</a><br>'
	# return HttpResponse(html)

	# return HttpResponse('<h1> This is the music app homepage </h1>')


def detail(request,album_id):
	# pass in <album_id> from the request
	# e.g. when a user requests /music/123 
	# 123 gets assigned to album_id 
	return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
