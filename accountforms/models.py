from django.db import models
from django.urls import reverse
from django.forms import ModelForm
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Doctor(models.Model):
<<<<<<< Updated upstream
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
=======
    email = models.EmailField(primary_key=True, unique=True)
    name = models.CharField(max_length = 255, verbose_name = "name", blank = True)
    doctorid = models.CharField(max_length = 255, blank = True)
    #comment
    class Meta:
        #app_label = 'pharmasend'
        ordering = ['email', 'doctorid']
        
    
    def __str__(self) -> str:
        return self.name + "(eMail = " + self.email + ")"
>>>>>>> Stashed changes

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

class Pharmacist(models.Model):
<<<<<<< Updated upstream
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

=======
    email = models.EmailField(primary_key = True, unique = True)
    clinic = models.CharField(max_length = 255, blank = True)
    name = models.CharField(max_length = 255, verbose_name = "name", blank = True)

    class Meta:
        ordering = ['email', 'clinic']
    def __str__(self) -> str:
        return self.name + ", " + self.clinic + "(eMail = " + self.email + ")"
>>>>>>> Stashed changes
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


class AccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email is invalid")
        if not username:
            raise ValueError("Username is invalid")
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(email=self.normalize_email(email), username=username)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

<<<<<<< Updated upstream


=======
>>>>>>> Stashed changes
class Account(AbstractBaseUser):
    email           = models.EmailField(max_length=60, verbose_name="eMail", primary_key=True)
    username        = models.CharField(max_length=255, verbose_name = "Username")
    password        = models.CharField(max_length=255)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    #backend = CIModelBackend()

    objects = AccountManager()
    # undeveloped
    puser = models.OneToOneField(Pharmacist, on_delete=models.SET_NULL, null = True)
    duser = models.OneToOneField(Doctor, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

<<<<<<< Updated upstream
class Message(models.Model):
    sender = models.ForeignKey(Account, related_name='sender', on_delete = models.SET_NULL, null = True)
    
=======
class Order(models.Model):
    sender = models.ForeignKey(Account, related_name='sender', on_delete = models.SET_NULL, null = True)
    reciever = models.ForeignKey(Pharmacist, related_name='reciever', on_delete = models.SET_NULL, null = True)
    patientid = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['sender', 'reciever']
    def __str__(self) -> str:
        ret = self.sender + " to " + self.reciever
        if (len(self.message) > 20):
            ret += self.message[:19] + "..."
        else:
            ret += self.message
        return ret
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


>>>>>>> Stashed changes
