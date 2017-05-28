from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.
DEFAULT_WORKOUT_ID = 1
class Exercise(models.Model):
	NAME_CHOICES = (
	    ('Arms', (
	            ('bicurl', 'Biceps Curl'),
	            ('armpress', 'Shoulder Press'),
	            ('tricurl', 'Triceps Curl'),
	        )
	    ),
	    ('Legs', (
	            ('legpress', 'Leg Press'),
	            ('legcurl', 'Leg Curl'),
	            ('legext', 'Leg Extension'),
	            ('abduction', 'Leg Abduction'),
	            ('adduction', 'Leg Adduction'),
	        )
	    ),
	    ('Chest', (
	    		('chestpress', 'Chest Press'),
	    		('chestfly', 'Chest Flys'),
	    	)
	    ),
	    ('abs', 'Abdominal Crunches'),
	    ('cardio', 'Cardio Exercise'),
	    ('unknown', 'Unknown'),
	)
	name = models.CharField(max_length=100, choices=NAME_CHOICES)
	max_weight = models.PositiveSmallIntegerField(default=0)
	num_sets = models.PositiveSmallIntegerField(default=0)
	reps_per_set = models.PositiveSmallIntegerField(default=0)
	duration = models.DurationField(blank=True, null=True)
	workout = models.ForeignKey('Workout', default = DEFAULT_WORKOUT_ID)

	def __str__(self):
		return self.name

class Gym(models.Model):
	name = models.CharField(max_length = 50)
	location = models.CharField(max_length = 100)
	notes = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class Workout(models.Model):
	user = models.ForeignKey('auth.User', default=1)
	gym = models.ForeignKey('Gym', on_delete=models.CASCADE)
	workout_time = models.DateTimeField(default = timezone.now)
	# exercises = models.ManyToManyField(Exercise)

	def __str__(self):
		outStr = self.workout_time.__str__() + " at " + self.gym.name
		return outStr
