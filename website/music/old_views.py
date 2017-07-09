# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

# which model/table you want to query
from .models import Album

# Create your views here.

def index(request):
	# connect to the database and retrieve all rows
	all_albums = Album.objects.all()	
	return render(request, 'music/index.html', {'all_albums': all_albums})
	
def detail(request,album_id):

	"""
	Because raising 404 or getting object from database is common
	Django included the get_object_or_404 method to 
	reduce this to one line
	"""

	try:
		# could use pk=album_id (primary_key) doesn't matter
		album = Album.objects.get(id=album_id)

	except Album.DoesNotExist:
		raise Http404("Album does not exist")

	return render(request, 'music/detail.html', {'album': album})


