from django.conf.urls import url
from . import views

urlpatterns = [

	# r' means regular expression, '^' = begin, '$' = end 
	# so when the user requests /music/ and nothing else, this should return
	# what is defined in the view file, for the function named index (hence views.index) as the second param
    url(r'^$', views.index, name='index'),

    # Next we want to return a page that is based on the album_id
    # Regex explained
    # (?P < variable_name> [0-9]+)
    # This says when a user requests for example /music/123 
    # store 123 into the variable called variable_name
    # the variable_name should be from the numbers [0-9] and any integer that follows '+'
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]