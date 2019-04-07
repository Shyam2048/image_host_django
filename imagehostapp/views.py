from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from . import db
from .  import models
import json
import pdb
from django.contrib import auth
import shutil
import os
from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.conf import settings

# Create your views here.

def home(request):
	return render(request,"home.html",{})

def signup(request):
	return render(request,"signup.html",{})

def login(request):
	return render(request,"login.html",{})

@csrf_exempt
def save_user(request):
	if request.user.is_authenticated:
		return render(request,"upload.html",{})
	
	else:
		# pdb.set_trace()
		data=json.loads(request.body.decode('utf-8'))
		first_name=data.get('first_name')
		last_name=data.get('last_name')
		email=data.get('email')
		password=data.get('password')
		print(data)

		if(first_name and last_name and email and password):
			username=db.creat_username(first_name,last_name)
			print(username)
			user_exist=db.check_if_user_exist(email)
			if user_exist==False:
				user=db.createuser(username,first_name,last_name,email,password)
				# username=db.get_username_from_email(email)

				# ------ Create User Directory ---------
				base_dir2 = os.getcwd()
				print(base_dir2)
				email_name=email.split("@")[0]
				print(email_name)
				access_rights = 0o777

				try:  
				    os.mkdir((base_dir2+("/uploads/{0}".format(email_name))),access_rights)

				except OSError:  
				    print ("Creation of the directory %s failed" )
				else:  
				    print ("Successfully created the directory %s " )

				if user:
					return JsonResponse({"status":"True","message":"User successfully created"},status=200)
				else:
					return JsonResponse({"status":"False","message":"Error creating User"},status=400)
			
			else:
				return JsonResponse({"status":"False","message":"User already exist"},status=400)

		
		else:
			return JsonResponse({"status":"False","message":"fill all the details"},status=400)




@csrf_exempt
def login_check(request):

	data=json.loads(request.body.decode('utf-8'))
	# pdb.set_trace()
	if not data:
		return JsonResponse({'status':'False','message':'No Data Received'}, status=400)
	email=data.get('email')
	password=data.get('password')
	username=db.get_username_from_email(email)
	user = auth.authenticate(username=username, password=password)
	print(user)
	auth.login(request, user)
	if not user:
		return JsonResponse({'status':'False','message':'Incorrect Id Or Password'}, status=400)
	else:
		return JsonResponse({'status':'True','message':'Logged In'},status=200)








@csrf_exempt
def logout(request):
	auth.logout(request)
	return render(request,"home.html",{})








def upload_pic(request):

	if request.user.is_authenticated:
	

		# this is done to reach to the user's folder
	

		username=request.user

		email_id=db.fetch_email(username)
		
		email_name=email_id.split("@")[0]

		access_rights = 0o777

		base=os.getcwd()
		
		folder=os.path.join(base,"uploads/{0}".format(email_name))

		fs = FileSystemStorage(location=folder,base_url=folder)


		# images are dsiplayed when the user logged in 


		i=[]
		for images in os.walk(folder):
			print(images)
		for j in range(len(images[2])):
			i.append(images[2][j])
		list_of_images=[]	
		f=settings.MEDIA_URL.replace('/','\\')
		for fil1 in i:
			file1=fs.url(fil1)
			list_of_images.append(("/uploads/{0}/".format(email_name))+file1)
			print(list_of_images)


# When user uploads the image ad post the image the page is refreshed

	
		if request.method == 'POST' and request.FILES['image']:
			myfile = request.FILES.get('image')
			
			filename = fs.save(myfile.name, myfile)

			img = Image.open(myfile)
			width = 500
			height = 300
			im1 = img.resize((width, height), Image.ANTIALIAS)  
			im1.save(("uploads/{0}/".format(email_name))+myfile.name)

			uploaded_file_url = fs.url(filename)
			
			# print(uploaded_file_url)

			print((settings.BASE_DIR+settings.MEDIA_URL))

			for root, dirs, files in os.walk(folder):
				print(files)
			f=settings.MEDIA_URL.replace('/','\\')
			
			
			list_of_images=[]

			for fil1 in files:
				file1=fs.url(fil1)
				# print(file1)
				list_of_images.append(("/uploads/{0}/".format(email_name))+file1)
				print(list_of_images)
			return render(request, 'upload.html', {
				'list_of_images': list_of_images
			})
		return render(request, 'upload.html',{'list_of_images':list_of_images})

	else:
		return render(request,"home.html",{})


