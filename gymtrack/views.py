from django.shortcuts import render
from .models import *

# Create your views here.
def workout_list(request):
	myWorkouts = Workout.objects.filter(user=request.user)
	return render(request, 'gymtrack/workout_list.html', {'myWorkouts': myWorkouts})