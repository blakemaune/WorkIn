from django import forms
from django.contrib.auth.models import *
from .models import *

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		help_texts = {
			'username': None,
		}
		fields = ('username', 'email', 'password')

class WorkoutForm(forms.ModelForm):
	class Meta:
		model = Workout
		help_texts = {
			'gym': None,
			'workout_time': None,
		}
		fields = ('gym', 'workout_time')

class ExerciseForm(forms.ModelForm):
	class Meta:
		model = Exercise
		fields = ('name', 'max_weight', 'num_sets', 'reps_per_set', 'duration')