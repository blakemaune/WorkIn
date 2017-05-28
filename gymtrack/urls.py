from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^workouts/$', views.workout_list, name='workout_list'),
    url(r'^signup/$', views.createuser, name='new_user'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'gymtrack/login.html'}, name='login'),
    url(r'^workouts/create/$', views.createworkout, name='new_workout'),
    url(r'^workouts/(?P<pk>\d+)/$', views.workout_detail, name='workout_detail'),
    url(r'^workouts/(?P<pk>\d+)/add/$', views.exercise_add, name='exercise_add'),
    url(r'^workouts/(?P<pk>\d+)/delete/$', views.workout_delete, name='workout_delete'),
    url(r'^exercises/(?P<pk>\d+)/delete/$', views.exercise_delete, name='exercise_delete'),
    url(r'^exercises/(?P<pk>\d+)/edit/$', views.exercise_edit, name='exercise_edit'),
]