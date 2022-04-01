from rest_framework import serializers
from .models import Agegroup, Banners,Card, Committee, Event, Form, Prayer, Video,Index,CardBanner1, CardBanner2, CardBanner3
from .models import *
class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ['id', 'banner_image1','link']

class PrayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prayer
        fields = ['id','image', 'prayer_name', 'iqamat_time','namas_time']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'image', 'date','event_name','time','description','location']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video']

class AgegroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agegroup
        fields = ['id', 'age']

class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = ['id', 'committee']
        
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'firstname', 
        'lastname','age_group','phone',
        'email','committee','is_lead',
        'is_volunteer']
        
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'image', 
        'image2','title','description',]
        
class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ['id', 'inner_banner', 
        'footer','logo','main_menu','post1','donations']
        
class BannerCard1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CardBanner1
        fields = ['id', 'image']


class BannerCard2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CardBanner2
        fields = ['id', 'image']

class BannerCard3Serializer(serializers.ModelSerializer):
    class Meta:
        model = CardBanner3
        fields = ['id', 'image']
        
        
class duaandspecialrequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = duaandspecialrequests
        fields = ['id', 'name', 
        'message','email']

class feedbackandquestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedbackandquestions
        fields = ['id', 'subject', 
        'message','email']

class subscribeandnewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscribeandnewsletter
        fields = ['id','email']
