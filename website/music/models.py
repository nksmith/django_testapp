# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=1000)

	def __str__(self): 
		return self.artist + ' - ' + self.album_title

class Song(models.Model):
	# the Foriegn Key is what allows a song to be mapped to an album
	# when an album is deleted, the models.CASCADE param says delete the songs
	# in the Songs table associated with that album
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)



# NOTES
# Django creates a primary key by default for each model, so you don't need an id column

# To make the change file (what you change and want applied to the db), 
# the following command is used
# python manage.py makemigrations 

# To apply these changes, the following command is used
# python manage.py migrate

# The cool thing about Django is that it creates the SQL files to build the tables for you
# EX. python manage.py sqlmigrate music 0001   