from django.db import models
from mac_vendor_lookup import MacLookup

class Device(models.Model):

    hostname = models.CharField(max_length=128, blank=True)
    hostip = models.GenericIPAddressField(unique=True,primary_key=True)
    macaddress = models.CharField(max_length=20,blank=True,null=True)
    vendor = models.CharField(max_length=64,blank=True,null=True)
    osfamily = models.CharField(max_length=64,blank=True,null=True)
    osname = models.CharField(max_length=32,blank=True,null=True)
    ostype = models.CharField(max_length=32,blank=True,null=True)
    osvendor = models.CharField(max_length=32,blank=True,null=True)
    ports = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=64,default="Unkknown")
    discovered = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    lastupdate = models.DateTimeField(auto_now=True,blank=True,null=True)
    lastresponded = models.DateTimeField(blank=True,null=True)
    valid = models.BooleanField(default=True)
    def __str__(self):
        return f"Host: {self.hostname}, PK: {self.hostip}" 

    



