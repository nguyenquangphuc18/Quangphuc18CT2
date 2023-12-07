from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

    
    
    
class groupnv(models.Model):
    group = models.CharField(max_length=200,null=True)
    info = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.group
class addnv(models.Model):
    user =  models.CharField(max_length=200,null=True)
    group = models.ForeignKey(groupnv,on_delete=models.SET_NULL,blank=True,null=True)
    phone = models.CharField(max_length=200,null=True) 
    email = models.CharField(max_length=200,null=True)
    Note = models.CharField(max_length=500,null=True)
    
    def __str__(self):
        return str(self.user)    
class adddv(models.Model):
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True, blank=True)
    
    
    price =  models.CharField(max_length=200,null=True)
    user = models.ForeignKey(addnv,on_delete=models.SET_NULL,blank=True,null=True)
    time = models.CharField(max_length=200,null=True)
    intime = models.CharField(max_length=200,null=True)
    quantity = models. IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return str(self.name)
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    @property
    def total(self):
        adddvs = self.adddv_set.all()
        total = sum([adddv.get_price for price in adddvs])
        return total
    @property
    def get_price(self):
        total = self.adddv.price * self.quantity
        return total
        
    
class groupkh(models.Model):
    group =  models.CharField(max_length=200,null=True)
    info = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.group)
   

class addkh(models.Model):
    id = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    date = models.DateField(max_length=200,null=True)
    group = models.ForeignKey(groupkh,on_delete=models.SET_NULL,blank=True,null=True)
    email = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    Note = models.CharField(max_length=500,null=True)
    def __str__(self):
        return str(self.name)



        
        
    
     
     
        