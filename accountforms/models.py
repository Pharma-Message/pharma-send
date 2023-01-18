from django.db import models
from django.urls import reverse
from django.forms import ModelForm

class Doctor(models.Model):
    fname = models.CharField(max_length=255, verbose_name = "First Name")
    lname = models.CharField(max_length=255, verbose_name = "Last Name")
    uname = models.CharField(max_length=255, verbose_name = "Username", primary_key=True)
    email = models.EmailField(verbose_name = "eMail")
    pwd = models.CharField(max_length=255, verbose_name = "Password")
    
    class Meta:
        #app_label = 'pharmasend'
        ordering = ['lname', 'fname']
        
    
    def __str__(self) -> str:
        return self.lname + ", " + self.fname + "(eMail = " + self.email + ")"

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

class Pharmacist(models.Model):
    fname = models.CharField(max_length=255, verbose_name = "First Name")
    lname = models.CharField(max_length=255, verbose_name = "Last Name")
    uname = models.CharField(max_length=255, verbose_name = "Username", primary_key=True)
    clinic = models.CharField(max_length=255, verbose_name = "Clinic")
    email = models.EmailField(verbose_name = "eMail")
    pwd = models.CharField(max_length=255, verbose_name = "Password")

    class Meta:
        ordering = ['lname', 'fname', 'clinic']
        
    
    def __str__(self) -> str:
        return self.lname + ", " + self.fname + "(eMail = " + self.email + ")"

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

