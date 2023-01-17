from django.db import models
from django.urls import reverse
from django.forms import ModelForm
from pharmasend.apps import DoctorConfig

class Doctor(models.Model):
    fname = models.CharField(max_length=255, help_text="First Name of Doctor", verbose_name = "First Name")
    lname = models.CharField(max_length=255, help_text="Last Name of Doctor", verbose_name = "Last Name")
    uname = models.CharField(max_length=255, help_text="Username of Doctor", verbose_name = "Username", primary_key=True)
    email = models.EmailField(help_text="eMail to contact you for notifications", verbose_name = "eMail")
    pwd = models.CharField(max_length=255, help_text="Password", verbose_name = "Password")
    
    class Meta:
        app_label = 'pharmasend'
        #app_config = DoctorConfig
        ordering = ['lname', 'fname']
        
    
    def __str__(self) -> str:
        return self.lname + ", " + self.fname + "(eMail = " + self.email + ")"

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

class Pharmacist(models.Model):
    fname = models.CharField(max_length=255, help_text="First Name of Doctor", verbose_name = "First Name")
    lname = models.CharField(max_length=255, help_text="Last Name of Doctor", verbose_name = "Last Name")
    uname = models.CharField(max_length=255, help_text="Username of Doctor", verbose_name = "Username", primary_key=True)
    clinic = models.CharField(max_length=255, help_text="First Name of Doctor", verbose_name = "First Name")
    email = models.EmailField(help_text="eMail to contact you for notifications", verbose_name = "eMail")
    pwd = models.CharField(max_length=255, help_text="Password", verbose_name = "Password")

    class Meta:
        app_label = 'pharmasend'
        #app_config = DoctorConfig
        ordering = ['lname', 'fname']
        
    
    def __str__(self) -> str:
        return self.lname + ", " + self.fname + "(eMail = " + self.email + ")"

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

