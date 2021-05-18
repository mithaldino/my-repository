from django.shortcuts import render, redirect
from iphoneapp.forms import *
from iphoneapp.models import *
from django.db import connection
from django.http import HttpResponse, JsonResponse
import json
import datetime
from django.core import serializers
cursor = connection.cursor()
from django.core.files.storage import FileSystemStorage
#superuser: mithun
#admin: mithun@gmail.com
#same_pass: mithun@123

def homepage(request):
    return render(request, "iphoneapp/index.html")
    
def about(request):
    return render(request, "iphoneapp/about.html")
    
def custlogin(request):
    return render(request, "iphoneapp/customerlogin.html")
    
def contacting(request):
    return render(request, "iphoneapp/contacting.html")

def customerlogin(request):
    if request.method == 'POST': 
        email = request.POST.get('userid',' ')
        password = request.POST.get('password',' ')
        for c in Customer.objects.raw("select * from Customer where custemail='%s' and custpassword='%s'"%(email,password)):
            if c.custemail == email and c.custpassword == password:
                request.session['custemail'] = email
                return render(request,"iphoneapp/index.html")
        else:
            return render(request,"iphoneapp/customerlogin.html")
    else:
        return render(request,"iphoneapp/customerlogin.html")
        
def changecustpassword(request):
    return render(request,'iphoneapp/changecustomerpassword.html')
    
def updatecustpassword(request):
    if request.method == 'POST':
        username = request.POST.get('userid',' ')
        password1 = request.POST.get('password1',' ')
        password2 = request.POST.get('password2',' ')
        if password1 == password2:
            sql = "update Customer set custpassword='%s' where custemail='%s'"%(password1,username)
            cursor.execute(sql)
            if cursor.rowcount>=1:
                return render(request,"iphoneapp/customerpasschange.html")
            else:
                return render(request,"iphoneapp/error.html")
            
        else:
            return render(request,'iphoneapp/changecustomerpassword.html')
            
    else:
            return render(request,'iphoneapp/changecustomerpassword.html')
        
    
def adminlogin(request):
    return render(request, "iphoneapp/adminlogin.html")
    
def adminlog(request):
    if request.method == 'POST': 
        email = request.POST.get('adminid',' ')
        password = request.POST.get('adminpassword',' ')
        for c in Admins.objects.raw("select * from Admins where adminemailid='%s' and adminpassword='%s'"%(email,password)):
            if c.adminemailid == email and c.adminpassword == password:
                request.session['adminemailid'] = email
                return render(request,"iphoneapp/index.html")
        else:
            return render(request,"iphoneapp/adminlogin.html")
    else:
        return render(request,"iphoneapp/adminlogin.html")

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request,'iphoneapp/index.html')

def contact(request):
    return render(request, "iphoneapp/contact.html")
    
def iphonevideo(request):
    return render(request, "iphoneapp/iphonevideo.html")
    
def airpodsvideo(request):
    return render(request, "iphoneapp/airpodsvideo.html")
    
def watchvideo(request):
    return render(request, "iphoneapp/watchvideo.html")
    
def macvideo(request):
    return render(request, "iphoneapp/macvideo.html")
    
def store(request):
    return render(request, "iphoneapp/addstore.html")    

def addstore(request): 
    if request.method=="POST":      
        form=Storeform(request.POST, request.FILES)      
        if form.is_valid():  
            try:     
                form.save()                             
                return render(request,"iphoneapp/success.html")     
            except:
                return render(request,"iphoneapp/error.html")
        else:
            form=Storeform() 
        return render(request,"iphoneapp/addstore.html",{'form':Storeform})
        
def storelist(request):
    s = Store.objects.all()
    return render(request, 'iphoneapp/storelist.html',{'sto':s})
    
def getstoreitem(request,storeid):
    s = Store.objects.get(storeid = storeid)
    return render(request, 'iphoneapp/updatestore.html',{'e':s})
    
def updatestore(request):
    s = Store.objects.get(storeid = request.POST.get('storeid',' '))
    form = Storeform(request.POST,request.FILES,instance = s)
    if form.is_valid():
        try:
            form.save()
            return render(request,"iphoneapp/storeupdatesuccess.html")
        except:
            return render(request,"iphoneapp/error.html")
    else:
        return render(request,"iphoneapp/error.html")
    return render(request,"iphoneapp/storeupdatesuccess.html",{'e':s})
    
def deletestore(request, storeid):
    st = Store.objects.get(storeid = storeid)
    st.delete()
    return render(request, "iphoneapp/deletesuccess.html")
    
def getimageview(request, storeid):
    s = Store.objects.get(storeid = storeid)
    return render(request, "iphoneapp/imageview.html",{'e':s})
    
def imageview(request):
    return render(request, "iphoneapp/imageview.html")
    
def customer(request):
    return render(request, "iphoneapp/addcustomer.html") 
    
def addcustomer(request):
    if request.method=="POST":
        form=Customerform(request.POST)
        if form.is_valid():
            try:       
                form.save()       
                return render(request,"iphoneapp/customersuccessful.html")   
            except:
                return render(request,"iphoneapp/error.html")
        else:
            form=Customerform()    
        return render(request,"iphoneapp/addcustomer.html",{'form':Customerform})
        
def custlist(request):
    c = Customer.objects.all()
    return render(request, 'iphoneapp/customerlist.html',{'cus':c})
    
def updatecustomer(request, custemail):
    c = Customer.objects.get(custemail= custemail)
    form = Customerform(request.POST,instance = c)
    if form.is_valid():
        try:
            form.save()
            return render(request,"iphoneapp/customersuccessful.html")
        except:
            return render(request,"iphoneapp/error.html")
    else:
        return render(request,"iphoneapp/error.html")
    return render(request,"iphoneapp/editprofile.html",{'e':c})
    
def getcust(request, custemail):
    c = Customer.objects.get(custemail = custemail)
    return render(request, 'iphoneapp/editprofile.html',{'e':c})
    
def showcartform(request, storeid):
    fd = Store.objects.get(storeid = storeid)
    return render(request, 'iphoneapp/addcart.html',{'e':fd})
    
def addtocart(request):
    if request.method == 'POST':
        eid = request.session['custemail']
        fid=request.POST.get('storeid','')
        fn=request.POST.get('name','')
        fp=request.POST.get('price','')
        fq=request.POST.get('quantity','')
        tp = float(fq) * float(fp)
        sql = "insert into Cart(custemailid,storeid,name,price,quantity,totalprice)values('%s','%s','%s','%s','%s','%f')"%(eid,fid,fn,fp,fq,tp)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            return redirect("/showcart")
        else:
            return render(request,"iphoneapp/error.html")
            
        return render(request,"iphoneapp/error.html")
        
def showcart(request):
    email = request.session['custemail']
    carts = Cart.objects.filter(custemailid=email)
    if len(carts) != 0:
        return render(request,"iphoneapp/cartlist.html",{'mycart':carts})
    else:
        return render(request,"iphoneapp/error.html")
        
def deletecart(request, cartid):
    carts = Cart.objects.get(cartid = cartid)
    carts.delete()
    return render(request, "iphoneapp/success.html")
    
def placeorder(request):
    if request.method=='POST':
        email = request.session['custemail']
        sql = "select sum(totalprice) from cart where custemailid='%s'"%(email)
        cursor.execute(sql)
        data = cursor.fetchone()
        totalbill = data[0]
        c_date = datetime.date.today()
        sql = "insert into orders(custemailid, orderdate, totalbill) values('%s','%s','%f')"%(email,c_date,totalbill)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            clearcart(request)
            return redirect("/orderlist")
        else:
            return render(request, "iphoneapp/error.html")
    else:
        return render(request, "iphoneapp/error.html")
        
def showorders(request):
    email = request.session['custemail']
    order = Orders.objects.filter(custemailid = email)
    return render(request, 'iphoneapp/orderlist.html', {'orders':order})
    
def clearcart(request):
    email = request.session['custemail']
    carts = Cart.objects.filter(custemailid = email)
    carts.delete()
    return render(request, "iphoneapp/index.html")