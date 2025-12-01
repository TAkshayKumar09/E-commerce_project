from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import users
from .models import products
import cloudinary

# Create your views here.

@csrf_exempt
def login(req):
    if req.method !="POST":
        return HttpResponse("Only POST allowed")
    
    useremail=req.POST.get("useremail")
    userpassword=req.POST.get("userpassword")
    try:
        user=users.objects.get(email=useremail, password=userpassword)
        return HttpResponse("Login Successfully")
    except users.DoesNotExist:
        return HttpResponse("Invalid Credentials")
        


@csrf_exempt
def register(req):
    if req.method =="POST":
        user_name=req.POST.get("name")
        user_email=req.POST.get("email")
        user_password=req.POST.get("password")
    new_user=users.objects.create(name=user_name, email=user_email, password=user_password)
    return HttpResponse("User Created Successfully")


@csrf_exempt
def update_user(req,email):
    try:
        user=users.objects.get(email=email)

        # check correct field name
        new_password=req.POST.get("password")
        
        if new_password:
            user.password=new_password
        user.save()
        return HttpResponse("Password Updated Successfully")
    except:
        return HttpResponse("User Not Found")


@csrf_exempt
def delete_user(req,email):
    try:
        delete_user=users.objects.get(email=email)
        
        delete_user.delete()
        return HttpResponse("Account Deleted Successfully")

    except:
        return HttpResponse("Account Not Found")


# products views

@csrf_exempt
def home(req):
    if req.method == "GET":
        homepage=products.objects.all().values()
        data=list(homepage)
        return JsonResponse(data,safe=False)



@csrf_exempt
def admin(req):
    if req.method =="POST":
        try:
            product_title=req.POST.get("title")
            product_price=req.POST.get("price")
            product_description=req.POST.get("description")
            product_image=req.FILES.get('image')
            image_url=cloudinary.uploader.upload(product_image)
            # print(image_url["secure_url"])
            new_user=products.objects.create(title=product_title,price=product_price,description=product_description,image=image_url['secure_url'])
        
            return HttpResponse("Product Uploaded SuccessFully")
        except:
            return HttpResponse("Product not Uploaded")

@csrf_exempt
def update_product(req,title):
    try:
        update=products.objects.get(title=title)
        if req.POST.get("name"):
            product_name=req.POST.get("name")
        if req.POST.get("price"):
            product_price=req.POST.get("price")
        if req.POST.get("description"):
            product_description=req.POST.get("description")
        if req.FILES.get("image"):
            product_image=req.FILES.get("image")
            image_url=cloudinary.uploader.upload(product_image)
            update.image=image_url['secure_url']
        update.save()
        return HttpResponse("Item Updated Successfully")
    except products.DoesNotExist:
        return HttpResponse("Updating Failed")



@csrf_exempt
def delete_product(req,title):
    try:
        delete_item=products.objects.get(title=title)

        delete_item.delete()
        return HttpResponse("Item Deleted Successfully")
    except products.DoesNotExist:
        return HttpResponse("Item Not Found")