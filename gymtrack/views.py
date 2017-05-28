from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def workout_list(request):
	if request.user.is_anonymous:
		messages.info(request, 'You must be signed in to view your workouts!')
		return render(request, 'gymtrack/home.html', {})
	else:
		myWorkouts = Workout.objects.filter(user=request.user)
		return render(request, 'gymtrack/workout_list.html', {'myWorkouts': myWorkouts})

def home(request):
	if request.user.is_anonymous():
		# Send anonymous to template
		user = request.user
	else:
		# Get user
		user = request.user
	print(user)
	return render(request, 'gymtrack/home.html', {'user': user})

def createuser(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			# login(new_user)
			# redirect, or however you want to get to the main view
			return render(request, 'gymtrack/home.html', {})
	else:
		form = UserForm() 

	return render(request, 'gymtrack/newuser.html', {'form': form})

def logout(request):
	django_logout(request)
	messages.info(request, 'Sign out successful')
	return render(request, 'gymtrack/home.html', {})

def createworkout(request):
	if request.method == "POST":
		form = WorkoutForm(request.POST)
		if form.is_valid():
			workout = form.save()
			messages.info(request, 'New workout saved!')
			return redirect('workout_detail', pk=workout.pk)
		else:
			form = WorkoutForm()
	else:
		form = WorkoutForm()
	return render(request, 'gymtrack/newworkout.html', {'form': form})

def exercise_add(request, pk):
	workout = get_object_or_404(Workout, pk=pk)
	form = ExerciseForm()
	if request.method == "POST":
		form = ExerciseForm(request.POST)
		if form.is_valid():
			exercise = form.save(commit=False)
			exercise.workout = workout
			print(exercise)
			exercise.save()
			return render(request, 'gymtrack/workout_detail.html', {'workout': workout})
	form = ExerciseForm()
	return render(request, 'gymtrack/newexercise.html', {'form': form})

def exercise_edit(request, pk):
	exercise = get_object_or_404(Exercise, pk=pk)
	if request.method=="POST":
		form = ExerciseForm(request.POST, instance=exercise)
		if form.is_valid():
			exercise = form.save()
			return redirect('workout_detail', pk=exercise.workout.pk)
	else:
		form = ExerciseForm(instance=exercise)
	return render(request, 'gymtrack/newexercise.html', {'form': form})
	

def workout_detail(request, pk):
	workout = get_object_or_404(Workout, pk=pk)
	if request.user == workout.user:
		return render(request, 'gymtrack/workout_detail.html', {'workout': workout})
	else:
		messages.info(request, 'Not your workout!')
		return redirect('home')

def exercise_delete(request, pk):
	exercise = get_object_or_404(Exercise, pk=pk)
	if request.user == exercise.workout.user:
		workout = exercise.workout
		exercise.delete()
		return render(request, 'gymtrack/workout_detail.html', {'workout': workout})
	else:
		messages.info(request, 'Not your exercise!')
		return redirect('home')

def workout_delete(request, pk):
	workout = get_object_or_404(Workout, pk=pk)
	if request.user == workout.user:
		workout.delete()
		messages.info(request, 'Workout successfully deleted')
	else:
		messages.info(request, 'Cannot Delete: Not your workout!')
	return redirect('home')

