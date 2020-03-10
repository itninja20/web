from django.db import models
from django.conf import settings
# Create your models here.

class Fachtest(models.Model):
    host_name = models.CharField(max_length=30, blank=False)
    pri_port = models.IntegerField(blank=False)
    sec_port = models.IntegerField(blank=True)
    arch = models.CharField(max_length=30, blank=False)
    server_profile = models.CharField(max_length=30, blank=False)
    app_name = models.CharField(max_length=30, blank=False)
    deploy_version = models.CharField(max_length=10, blank=False)
    deployed_date = models.CharField(max_length=10, blank=False)
    fqdn = models.CharField(max_length=100, blank=False)
    cmdb_app = models.CharField(max_length=30, blank=False)
    cmdb_asset = models.CharField(max_length=30, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ['date_created']
    
    def __str__(self):
        return self.host_name

    def serializeCustom(self):
        data = { 
            "host": self.host_name,
            "primaryport": self.pri_port,
            "seecondaryport": self.sec_port,
            "architecture": self.arch
            }
        return data
