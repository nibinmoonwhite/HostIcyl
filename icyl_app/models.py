from statistics import mode
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models import DateTimeField
from django.db.models.expressions import OrderBy
from django.utils import timezone
from cloudinary_storage.storage import VideoMediaCloudinaryStorage


class Banners(models.Model):
    banner_image1=models.FileField(upload_to='images/',null=True,blank=True)
    link=models.URLField(max_length=500,null=True)
    
    class Meta:
        ordering = ['id']
    # def __str__(self):
    #     return self.id

class Prayer(models.Model):
    image=models.FileField(upload_to='images/',null=True)
    prayer_name=models.CharField(max_length=500)
    iqamat_time=models.DateTimeField(null=True)
    namas_time=models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']
    def __str__(self):
        return str(self.prayer_name)

class Event(models.Model):
    image=models.FileField(upload_to='images/')
    date=models.DateField()
    event_name=models.CharField(max_length=500)
    time=models.CharField(max_length=500)
    description=models.TextField(null=True)
    location=models.CharField(max_length=500,null=True)

    class Meta:
        ordering = ['date']
    def __str__(self):
        return str(self.image)

class Video(models.Model):
    video = models.URLField(max_length=100, blank=True, )
    class Meta:
        ordering = ['id']
    def __str__(self):
        return str(self.video)

class Agegroup(models.Model):
    age=models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.age)


class Committee(models.Model):
    committee=models.CharField(max_length=200)
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return str(self.committee)

class Form(models.Model):
    firstname=models.CharField(max_length=500)
    lastname=models.CharField(max_length=500)
    age_group=models.ForeignKey(Agegroup,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    committee=models.ForeignKey(Committee,on_delete=models.CASCADE)
    is_lead=models.BooleanField()
    is_volunteer=models.BooleanField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.firstname)

class Card(models.Model):    
    image=models.FileField(upload_to='images/')
    image2=models.FileField(upload_to='images/')
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    
    
    
class Index(models.Model):    
    inner_banner=models.FileField(upload_to='images/')
    footer=models.FileField(upload_to='images/')
    logo=models.FileField(upload_to='images/')
    main_menu=models.FileField(upload_to='images/')
    post1=models.FileField(upload_to='images/')
    donations=models.FileField(upload_to='images/',null=True)    
    
class CardBanner1(models.Model):    
    image=models.FileField(upload_to='images/')
    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.image)



class CardBanner2(models.Model):    
    image=models.FileField(upload_to='images/')
    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.image)


class CardBanner3(models.Model):    
    image=models.FileField(upload_to='images/')
    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.image)



class duaandspecialrequests(models.Model):
    name=models.CharField(max_length=500)
    message=models.TextField()
    email=models.EmailField()


class feedbackandquestions(models.Model):
    subject=models.CharField(max_length=500)
    message=models.TextField()
    email=models.EmailField()

class subscribeandnewsletter(models.Model):
    email=models.EmailField()

class Event_information(models.Model):
    event_name=models.CharField(max_length=500,null=True,blank=True)
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    location=models.CharField(max_length=500,null=True,blank=True)

class fees(models.Model):
    fees=models.CharField(max_length=500,null=True,blank=True)
    event_id=models.ForeignKey(Event_information,on_delete=models.CASCADE,null=True,blank=True)


class Category(models.Model):
    category_description=models.CharField(max_length=500,null=True,blank=True)

class Discount(models.Model):
    fees_id=models.ForeignKey(fees,on_delete=models.CASCADE,null=True,blank=True)
    discount_category=models.CharField(max_length=500,null=True,blank=True)
    discount_percent=models.CharField(max_length=500,null=True,blank=True)



class Custom_information(models.Model):
    field1_name=models.CharField(max_length=500,null=True,blank=True)
    field1=models.TextField(null=True,blank=True)   
    field2_name=models.CharField(max_length=500,null=True,blank=True)
    field2=models.TextField(null=True,blank=True)     
    field3_name=models.CharField(max_length=500,null=True,blank=True)
    field3=models.TextField(null=True,blank=True) 
    field4_name=models.CharField(max_length=500,null=True,blank=True)
    field4=models.TextField(null=True,blank=True) 
    num1_name=models.CharField(max_length=500,null=True,blank=True)
    num1=models.CharField(max_length=500,null=True,blank=True)
    num2_name=models.CharField(max_length=500,null=True,blank=True)
    num2=models.CharField(max_length=500,null=True,blank=True)
    num3_name=models.CharField(max_length=500,null=True,blank=True)
    num3=models.CharField(max_length=500,null=True,blank=True)
    num4_name=models.CharField(max_length=500,null=True,blank=True)
    num4=models.CharField(max_length=500,null=True,blank=True)
    date1_name=models.DateField(null=True,blank=True)
    date1=models.DateField(null=True,blank=True)    
    date2_name=models.DateField(null=True,blank=True)
    date2=models.DateField(null=True,blank=True)  
    date3_name=models.DateField(null=True,blank=True)
    date3=models.DateField(null=True,blank=True)  
    date4_name=models.DateField(null=True,blank=True)
    date4=models.DateField(null=True,blank=True)  


class Gender(models.Model):
    gender=models.CharField(max_length=500,null=True,blank=True)


class Participant(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    age=models.CharField(max_length=500,null=True,blank=True)
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE,null=True,blank=True)
    

class Primmary_contact(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    phone=models.CharField(max_length=500,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    address=models.CharField(max_length=500,null=True,blank=True)


class event_table(models.Model):
    fees_id=models.ForeignKey(fees,on_delete=models.CASCADE,null=True,blank=True)
    discount_id=models.ForeignKey(Discount,on_delete=models.CASCADE,null=True,blank=True)
    contact_id=models.ForeignKey(Primmary_contact,on_delete=models.CASCADE,null=True,blank=True)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    custom_id=models.ForeignKey(Custom_information,on_delete=models.CASCADE,null=True,blank=True)


