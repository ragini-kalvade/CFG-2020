#sql Lite and postgres(production)
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

ASSIGNMENT_CHOICES = (
	('SMS', 'SMS'),
	('SMARTPHONES','SMARTPHONES'),
)

SUBMISSION_CHOICES = (
	('open', 'open'),
	('closed','closed'),
)

class Post(models.Model):
	title = models.CharField(max_length = 100)
	teacher = models.ForeignKey(User,on_delete=models.CASCADE)
	subject = models.CharField(default = 'english',max_length=200)
	Grade = models.IntegerField(default = 0)
	#Assignment_type = models.CharField(default = 'sms',max_length=100,choices = ASSIGNMENT_CHOICES, )
	#submission_type = models.CharField(max_length=200 , choices = SUBMISSION_CHOICES, default = open)
	description = models.TextField()
	#folder = models.FileField(upload_to='teaching_material')
	date_posted = models.DateTimeField(default=timezone.now) #can use auto_now_add = True but wont b able to date,therefore we use default 
	def __str__(self) :
		return self.title
	# def get_absolute_url(self) :
    #     return reverse('post-detail',kwargs={'pk':self.pk})
