from django.shortcuts import render
import pymysql
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em, pwd
    if request.method=="POST":
        m=pymysql.connect(host="localhost",user="root", passwd='' ,database='django_cafetest')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="user_email":
                em=value
            if key=="user_password":
                pwd=value
        
        c= "select * from django_cafetest.login_users where user_email ='{}' and user_password= '{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t==():
            return render(request, "error.html")
        else:
            return render(request, "welcome.html")

    return render(request,'login_page.html')

