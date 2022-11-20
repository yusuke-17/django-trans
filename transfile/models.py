from django.db import models

# Create your models here.
class FileUpload(models.Model):
    uploadedFile = models.FileField(upload_to = "Uploaded_Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)