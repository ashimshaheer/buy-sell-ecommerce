from multiprocessing import context
from django.shortcuts import redirect, render
from requests import session
from .models import Product,OrderDetail
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,TemplateView

from django.core.paginator import Paginator


from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import razorpay
# Create your views here.
def index(request):
    return render(request,'index.html')

#fuction based view ptoducts
def products(request):
    page_obj=product=Product.objects.all()
    
    product_name=request.GET.get('product_name')
    if product_name!='' and product_name is not None:
        page_obj=product.filter(name__icontains=product_name)

    paginator=Paginator(page_obj,12)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
       'products':page_obj
    }
    return render(request,'product.html',context)

#class based view for above  products view(listview)
# class productlistview(ListView):
#     model= Product
#     template_name= 'product.html'
#     context_object_name= 'products'
#     paginate_by= 4

def product_detail(request,id):
   product=Product.objects.get(id=id)
   print(product.seller_name)
   context={
       'products':product
   }
   return render(request,'detail.html',context)

#class based view for above product detail view 
class productdetailview(DetailView):
    model= Product 
    template_name='detail.html'
    context_object_name='products'
    pk_url_kwarg='pk'
     
    def get_context_data(self, **kwargs):             
            context=super(productdetailview,self).get_context_data(**kwargs)
            
            return context
            
      

@login_required
def  add_product(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        image=request.FILES['upload']
        sellername=request.user
        product= Product(name=name,price=price,desc=desc,image=image,seller_name=sellername)
        product.save()
        return redirect('/products')
    return render(request,'add_product.html')
    
def update_product(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'POST':
        product.name=request.POST.get('name')
        product.price=request.POST.get('price')
        product.desc=request.POST.get('desc')
        product.image=request.FILES['upload']
        product.save()
        return redirect('products.html')
    context={
       'products':product
      }  
    return render(request,'update.html',context)

def delete_product(request,id):
   product=Product.objects.get(id=id)
   if request.method =='POST':
        product.delete()
        return redirect(index)
   context={
       'products':product
     }
   return render(request,'delete.html',context)
    
def my_listings(request):
    product=Product.objects.filter(seller_name=request.user)
    context={
        'products':product
    }
    return render(request,'listings.html',context)

def payments(request,id):
    product=Product.objects.get(id=id)
    order=OrderDetail()
    order.customer_username=product.name
    order.amount=product.price
    print(order.amount)
    order.payment_PUBLISHABLE_KEY=settings.PUBLISHABLE_KEY
    order.payment_KEY=settings.SECRET_KEY
    order.save()
    if request.method == "POST":
            name = order.customer_username
            amount = order.amount
            

            client = razorpay.Client(
                auth=(order.payment_PUBLISHABLE_KEY, order.payment_KEY))
            payment = client.order.create({'amount': order.amount, 'currency': 'INR',
               
                                        'payment_capture': '1'})
    context={
                
                 'product':product
             }
            
           
    return render(request, 'payment.html',context)
                

class PaymentSuccessView(TemplateView):
    template_name ='mainpage/payment_success.html'
    
  
    
class PaymentFailedView(TemplateView):
    template_name = 'myapp/payment_failed.html'
    