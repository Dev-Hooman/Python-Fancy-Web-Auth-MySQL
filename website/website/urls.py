from django.contrib import admin
from django.urls import path

#########################################################################################

#                              IMPORTING HTML APPLICATIONS 
'''
from login-file.(views.py -> that renders into html) import function
'''
#########################################################################################


from login.views import loginaction
from signup.views import signaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signaction),
    path('login/', loginaction),
]
