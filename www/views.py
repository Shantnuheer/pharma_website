from django.shortcuts import render,redirect
from .models import fromula,contact,request_for_quote
from .models import cart
from .form import formulaform,contactform,cartform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from django.db.models import Max , Min ,Avg,Sum,Q,F
from django.core.mail import send_mail

# Create your views here.

def home(request):
    if request.method=='GET':
        data= fromula.objects.all()[:3]
        return render(request,'home.html',{'data':data})
    
def products(request):
    data= fromula.objects.filter(Product_name__startswith='A')
    return render(request,'products.html',{'data':data})
def C(request):
    data= fromula.objects.filter(Product_name__startswith='C')
    return render(request,'products.html',{'data':data})
def B(request):
    data= fromula.objects.filter(Product_name__startswith='B')
    return render(request,'products.html',{'data':data})
    

def about(request):
    return render(request,'about.html')

def contactData(request):
    if request.method=='GET':
        return render(request,'contact.html')
    else:
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        Message = request.POST['Message']

        send_mail(
            "Thanks for your Concern",
            "WE recieved your message and we will try to contact you Soon!",
            "invinciblegoat5911@gmail.com",
            [Email],
            fail_silently=False,
        )

        contact.objects.create(Name=Name,Email=Email,Phone=Phone,Message=Message)
        messages.info(request,"Message Sent Sucessfully")
        return redirect('home')





def custom(request):
    return render(request,'custom.html')

def unknown(request):
    return render(request,'unknown.html')
def facilities(request):
    return render(request,'facilities.html')

def readmore(request,id):
    data= fromula.objects.get(id=id)
    return render(request,'readmore.html',{'data':data})

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password =request.POST['confirm password']
        if password==confirm_password:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
        else:
            print('try matching password')
            return redirect('register')
    else:
        return render(request,'register.html')
    
def loginview(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(username=username,password=password)

        if user is None:
            print('invalid usaername or password')
            return redirect('loginview')
        else:
            login(request,user)
            return redirect('home')
    else:
        return render(request,'login.html')
def logoutview(request):
    logout(request)
    return redirect('login')

def enquiry(request):
    if request.method=='POST':
        product= request.POST['product']
        name= request.POST['name']
        email= request.POST['email']
        contact= request.POST['contact']
        company= request.POST['company']
        package= request.POST['package']
        weight= request.POST['weight']

        print(name)
        request_for_quote.objects.create(product=product,name=name,email=email,company=company,contact=contact,package=package,weight=weight).save()

        # breakpoint()
        messages.info(request,'Your Data is submitted we will contact you soon')
        return redirect("home")
    else:
        return render(request,'readmore.html')
    
def cart1(request,id):
    if request.user.is_authenticated:
        data= fromula.objects.get(id=id)

        
        a = cart.objects.filter(Q(user=request.user) and Q(Product_name=data.Product_name))
        
        for i in a:
                    global d
                    d=i

                    global u
                    u = i.quantity
        print("g",a)

        if cart.objects.filter(Q(Product_name=data.Product_name) & Q(user=request.user)).exists():
        
            
            if request.method=='POST':
                print("h")
                # data = cart.objects.get(Product_name=data.Product_name)
                product_name= request.POST['Product_name']
                

                quantity= int(request.POST['quantity'])+int(u)
    
                user= request.POST['user']
                data= cart(id=d.id,Product_name=product_name,quantity=quantity,user=user).save()
                return render(request,'Cart.html',{'data':data,'u':u})
            else:

                return render(request,'Cart.html',{'data':data})
            
        else:
            if request.method=='POST':
                data = fromula.objects.get(id=id)
                product_name= request.POST['Product_name']
                quantity= request.POST['quantity']
                user= request.user
                print("heelo")
                data= cart.objects.create(Product_name=product_name,quantity=quantity,user=user)
                return render(request,'Cart.html')
            else:


                return render(request,'Cart.html',{'data':data})
    return render(request,'Cart.html')
    

    
# def showcart(request):
#     data= cart.objects.all()
#     return render(request,'showcart.html',{'data':data})
            
def showcart(request):
    # data = cart.objects.get(user=request.user)
    data = cart.objects.filter(user=request.user)
    print(data)
    # data = cart.objects.filter(user=request.user)
    
    return render(request,'showcart.html',{'data':data})

def order(request):
    messages.info(request,'Your order is placed successfully')
    user =  cart.objects.filter(user=request.user)
    user.delete()
    return redirect('home')

def deletecart(request,id):
    cart.objects.get(id=id).delete()
    return redirect('showcart')

def search(request):
    if request.method =="POST":
        search = request.POST['search']
        data= fromula.objects.filter(Product_name__contains=search)
        return render(request,'search.html',{'data':data})
        
    return render(request,'search.html')