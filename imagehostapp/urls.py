from django.urls import path
from django import urls
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
		path('',views.home,name="home"),
		path('signup/',views.signup,name='signup'),
		path('login/',views.login,name='login'),
		path('save_user/',views.save_user,name="save_user"),
		path('login_check/',views.login_check,name="login_check"),
		path('upload_pic/',views.upload_pic,name="upload_pic"),
		path('logout/',views.logout,name="logout")

] 

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)