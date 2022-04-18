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



#----------------------------------------------------------------------------

class Event_informationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_information
        fields = ('id','event_name','start_date','end_date','location')

class feesSerializer(serializers.ModelSerializer):
    class Meta:
        model = fees
        fields = ('id','fees','event_id')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category_description')

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id','fees_id','discount_category','discount_percent')


class Custom_informationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_information
        fields = ('id','field1_name','field1','field2_name',
                   'field2','field3_name','field3','field4_name','field4',
        'num1_name','num1','num2_name','num2','num3_name','num3',
        'num4_name','num4','date1_name','date1','date2_name',
        'date2','date3_name','date3','date4_name','date4')


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields =('id','gender')


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('id','name','age','gender')

class Primmary_contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Primmary_contact
        fields = ('id','name','phone','email','address')

class event_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = event_table
        fields =('id','fees_id','discount_id',
                'contact_id','category_id',
                'custom_id')




class meet_boardSerializer(serializers.ModelSerializer):
    class Meta:
        model = meet_board
        fields ='__all__'
class prayerscheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = prayerschedule
        fields ='__all__'