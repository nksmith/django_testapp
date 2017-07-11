# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# which model/table you want to query
from .models import Album, Song

# Create your views here.

def index(request):
	# connect to the database and retrieve all rows
	all_albums = Album.objects.all()	
	return render(request, 'music/index.html', {'all_albums': all_albums})
	
def detail(request,album_id):
	# tries to query object from database or returns 404	
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', {'album': album})


# EXAMPLE HOW TO RETURN DATABASE 
# function to handle the form data 
def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
		# so in the detail.html we set the value of name=song e.g. 'song' to the song_id that they selected

	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', {
			'album': album,
			'error_message': "You did not select a valid song"
			})

	else:
		# Update and store changes to the the database
		selected_song.is_favorite=True
		selected_song.save()
		return render(request, 'music/detail.html', {'album': album})