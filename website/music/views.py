# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# which model/table you want to query
from .models import Album, Song


class IndexView(generic.ListView):
	# whenver we get a list of albums plug them into the template
	model = Album
	context_object_name = 'all_albums'
	template_name='music/index.html'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	# what type of object are you trying to get the detail of
	model = Album
	template_name ='music/detail.html'

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist','album_title','genre','album_logo']		