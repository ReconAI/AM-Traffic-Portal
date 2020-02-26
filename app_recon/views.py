from django.shortcuts import render
from .models import Dataset, DatasetType, EdgeNode, Project
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from boto.s3.connection import S3Connection
from django.conf import settings
from django.http import HttpResponse
#from PIL import Image
import requests
#from io import BytesIO
from requests.auth import HTTPDigestAuth

def index(request):

   
    Count_of_Datasets = Dataset.objects.all().count()
    Count_of_EdgeNodes = EdgeNode.objects.all().count()
    # Доступные книги (статус = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    # num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html', 
        context={'Count_of_Datasets': Count_of_Datasets,
                 'Count_of_EdgeNodes': Count_of_EdgeNodes},
    )
    

def getRealTime(self, pk):
   
    try:
        print(f"LOG:Trying to get image")
        image_data = requests.get("http://10.8.0.10/ISAPI/Streaming/channels/101/picture", auth=HTTPDigestAuth('admin', 'sQu555bQhB'))
        print(f"LOG:{image_data.headers}")
       # print(f"LOG:{image_data.text}")
       
    except:
        image_data = open("app_recon/static/img/noImage.png", "rb").read()
        
   
    
   # image_data = open("app_recon/static/img/noImage.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")
    

@method_decorator(login_required, name='dispatch') 
class DatasetListView(generic.ListView):
    model = Dataset
    context_object_name = 'my_dataset_list'

    def get_context_data(self, **kwargs):
        context = super(DatasetListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
@method_decorator(login_required, name='dispatch') 
class DatasetDetailView(generic.DetailView):
    model = Dataset
    
@method_decorator(login_required, name='dispatch') 
class EdgeNodeListView(generic.ListView):
    model = EdgeNode
    paginate_by = 20

@method_decorator(login_required, name='dispatch') 
class EdgeNodeDetailView(generic.DetailView):
    model = EdgeNode
    def get_context_data(self, **kwargs):
        context = super(EdgeNodeDetailView, self).get_context_data(**kwargs)
        
        
        print(f"LOG:{context['edgenode'].S3_Address}")
        conn = S3Connection(settings.AWS_ACCESS_KEY_ID,settings.AWS_SECRET_ACCESS_KEY, host='s3.eu-central-1.amazonaws.com')
        bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        
        bucket_list = bucket.list()
         
        #log = bucket_list.join();
        file_list = []
        for file in bucket_list:
            if "jpeg" in file.name:
                file_list.append({ "name": file.name, "url": file.generate_url(expires_in=10) })
            
        
        context['file_list'] = file_list
        return context
        

