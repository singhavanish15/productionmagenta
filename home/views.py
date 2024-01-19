from urllib import response
from django.shortcuts import render, HttpResponse
from home.models import person, gallery1, gallery_subitem, Doc_file
import requests
# Create your views here.
def home (request):
   #return HttpResponse('this is home')
   resp1 = requests.get("http://125.63.74.18:67/api/values")
   resp = resp1.json()
   return render(request, 'home.html', {'resp':resp})
 
#def api (request):
   resp1 = requests.get("http://125.63.74.18:67/api/values")
   resp = resp1.json()
   print(resp)
   return render(request, 'api.html', {'resp':resp})

def about (request):
   #return HttpResponse('this is about')
    return render(request, 'about.html')


def team (request):
   #return HttpResponse('this is about')
    return render(request, 'team.html')



def ourproduct (request):
   #return HttpResponse('this is about')
    return render(request, 'ourproduct.html')

def ourbusinessmodel (request):
   #return HttpResponse('this is about')
    return render(request, 'ourbusinessmodel.html')

def ouroperationalmodel (request):
   #return HttpResponse('this is about')
    return render(request, 'ouroperationalmodel.html')

def gallery (request):
  
   gallery_con = gallery1.objects.all()
   print(request.GET.get('gal'))
   galid = request.GET.get('gal')
   gall_item= None
   if galid:
        gall_item = gallery_subitem.objects.filter(subitem_id=galid)
   else:
        gall_item = gallery_subitem.objects.all()

   data={
      'gallery_con':gallery_con,
      'gall_item':gall_item
   }
   print(galid)
   print(gallery_con)
   print(gall_item)
   return render(request, 'gallery.html',data)

def downloads (request):

   doc_con = Doc_file.objects.all()
   file_data ={
      'doc_con':doc_con
   }
   print(file_data)
   
   return render (request, 'downloads.html', file_data)

def services (request):
  # return HttpResponse('this is services')
    return render(request, 'services.html')

def contact(request):
   if request.method=="POST":
      name1=request.POST['name']
      phone1=request.POST['phone']
      email1=request.POST['email']
      messagge1=request.POST['messagge']
      ins = person(name=name1, phone=phone1, email=email1, messagge= messagge1)
      ins.save()
      

   return render(request, 'contact.html')