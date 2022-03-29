from django.shortcuts import render
import pymysql
userName=''
userEmail=''
password=''
gender=''
dob=''
ph_n=''
userAddr=''
random_ID = 69  #fix it later make random function 

def signaction(request):
    global userName,userEmail,password,gender,dob,ph_n,userAddr, random_ID
    if request.method=="POST":
        m=pymysql.connect(host="localhost",user="root",passwd="",database='django_cafetest')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="user_name":
                userName=value
            if key=="user_email":
                userEmail=value
            if key=="user_password":
                password=value  
            if key=="user_gender":
                gender=value
            if key=="user_DOB":
                dob=value
            if key=="user_phoneNumber":
                ph_n=value
            if key=="user_address":
                userAddr=value
        
        c="insert into login_users Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(random_ID,userName,userEmail,password, gender,dob,ph_n,userAddr)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')
