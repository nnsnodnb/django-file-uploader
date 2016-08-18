from django.db import models
from datetime import datetime

class FileNameModel(models.Model):
    file_name = models.CharField(max_length = 50)
    upload_time = models.DateTimeField(default = datetime.now)
