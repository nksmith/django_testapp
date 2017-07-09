# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# which model/table you want to query
from .models import Album

# Create your views here.

def index(request):
	# connect to the database and retrieve all rows
	all_albums = Album.objects.all()
	
	context = {'all_albums': all_albums}
	# pass in request, what template to use, what data to pass into template	
	return render(request, 'music/index.html', context)
	
def detail(request,album_id):
	# try to query the database and see if there's an album with the id
	# the user typed in
	# send 404 if it's not

	try:
		album = Album.objects.get(id=album_id)

	except Album.DoesNotExist:
		raise Http404("Album does not exist")

	return render(request, 'music/index.html', {'album': album})

	# return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
