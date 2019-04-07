from . import models
from django.contrib.auth import login
from django.contrib.auth.models import User




def createuser(username,first_name,last_name,email,password):
	try:
		user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_superuser=False)

		if user:
			user.save()
			print(user)
			return user

	except Exception as exp:
		print(exp)
		return {'error':exp}



def creat_username(first_name,last_name):
	try:
		user_name=first_name+"_"+last_name+"_"+first_name[:3]+"_"+last_name[:2]
		print(user_name)
		return user_name

	except Exception as exp:
		print(exp)
		return {'error':exp}



def check_if_user_exist(email):
	try:
		user = User.objects.filter(email=email).values('username')
		print(user)
		if user:
			return ({'error':"not already exist"})
		else:
			return False


	except Exception as exp:
		print(exp)
		return ({'error':exp})




def get_username_from_email(email):
	try:
		username=User.objects.filter(email=email)[0].username
		print(username)
		return username

	except Exception as e:
		print(e)
		return({'error':e})


def fetch_email(username):
	try:
		email=User.objects.filter(username=username)[0].email
		return email
	except Exception as e:
		raise({'error':e})
	