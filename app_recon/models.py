from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
import uuid

# Create your models here.


class Project(models.Model):
    """
    Model representing a Project.
    """
    Name = models.CharField(
        max_length=255, help_text="Enter a name of project")

    Description = models.CharField(
        max_length=2000, help_text="Enter a Description for", null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Name


class EdgeNode(models.Model):

    Name = models.CharField(
        max_length=255, help_text="Enter a name of project")

    Description = models.CharField(
        max_length=2000, help_text="Enter a Description for This edge node",  null=True)

    Address = models.CharField(
        max_length=2000, help_text="Enter an location address of Edge node")
        
    IP_Address = models.CharField(
        max_length=2000, help_text="Enter an IP OpenVPN address of Edge node")
        
    S3_Address = models.CharField(
        max_length=2000, help_text="Enter an S3 address of storage for the Edge node")
        
    Camera_Address = models.CharField(
        max_length=2000, help_text="Enter an IP address\device path of connected camera")

    Project = models.ForeignKey(Project, on_delete=models.SET_NULL,  null=True)

    Version = models.CharField(
        max_length=255, help_text="Version of software on edge node")
        
    def get_absolute_url(self):
        """Returns the url to access a particular edge instance."""
        return reverse('edgenode-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Name


class DatasetType(models.Model):
    Name = models.CharField(
        max_length=255, help_text="Name of DatasetType (video, image, etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Name


class Dataset(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique ID for this Dataset")

    BucketURL = models.CharField(
        max_length=2000, help_text="Enter a Description for This edge node")

    Type = models.ForeignKey(DatasetType, on_delete=models.SET_NULL, null=True)

    EdgeNode = models.ForeignKey(EdgeNode, on_delete=models.SET_NULL, null=True)

    Created_dt = models.DateTimeField(auto_now=True)

def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.BucketURL
