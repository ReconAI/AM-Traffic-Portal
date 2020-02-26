from django.contrib import admin
from .models import Dataset, DatasetType, EdgeNode, Project

# Register your models here.

admin.site.register(Project)
admin.site.register(EdgeNode)
admin.site.register(DatasetType)
admin.site.register(Dataset)
