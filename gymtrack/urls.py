from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.workout_list, name='workout_list'),
]