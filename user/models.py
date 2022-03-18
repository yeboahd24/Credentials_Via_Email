from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

import random
import string


# Create your models here.
 
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=100)

	def __str__(self):
		return self.full_name


	@classmethod
	def create_user_and_send_credentials_via_email(cls, full_name, email, user=None):
	                           

		password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
		user_email = email if email else "".join([full_name, password])

		if user is None:
			user = User.objects.create_user(username=user_email, password=password, email=email)
			user_p = cls.objects.create(user=user, full_name=full_name)
			user_p.save()
			user.save()
		else:
			return ObjectDoesNotExist




		if email:

			send_mail(                                                              
				'Your credentials',                                                 
				f'Your username is: {user_email}\n Your password is: {password}',
				'sytech@gmail.com',                                                 
				[email],                                                       
				fail_silently=False,                                                
			)








 


