from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics

from django.core.mail import EmailMessage
from django.core.mail import send_mail
import smtplib


class ListBanners(generics.GenericAPIView):
    serializer_class=BannersSerializer        
    def get(self, request):
        queryset = Banners.objects.all()
        serializer = BannersSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class ListBannerbyid(generics.GenericAPIView):
    serializer_class=BannersSerializer        
    def get(self, request ,pk):
        queryset = Banners.objects.filter(id=pk)
        serializer = BannersSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class ListPrayers(generics.GenericAPIView):
    serializer_class=PrayerSerializer        
    def get(self, request):
        queryset = Prayer.objects.all()
        serializer = PrayerSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class ListEvent(generics.GenericAPIView):
    serializer_class=EventSerializer        
    def get(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})
            
class ListEventbyid(generics.GenericAPIView):
    serializer_class=EventSerializer        
    def get(self, request,pk):
        queryset = Event.objects.filter(id=pk)
        serializer = EventSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})
            
class ListVideo(generics.GenericAPIView):
    serializer_class=VideoSerializer        
    def get(self, request):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class ListVideobyid(generics.GenericAPIView):
    serializer_class=VideoSerializer        
    def get(self, request,):
        queryset = Video.objects.get(id=1)
        serializer = VideoSerializer(queryset)
        return Response(serializer.data)



class ListAgegroup(generics.GenericAPIView):
    serializer_class=AgegroupSerializer        
    def get(self, request):
        queryset = Agegroup.objects.all()
        serializer = AgegroupSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class ListCommittee(generics.GenericAPIView):
    serializer_class=CommitteeSerializer        
    def get(self, request):
        queryset = Committee.objects.all()
        serializer = CommitteeSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class AddForm(generics.CreateAPIView):
    serializer_class=FormSerializer        
    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})
        

class Addduaandspecialrequests(generics.CreateAPIView):
    serializer_class=duaandspecialrequestsSerializer        
    def post(self, request):
        serializer = duaandspecialrequestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})        


class Addfeedbackandquestions(generics.CreateAPIView):
    serializer_class=feedbackandquestionsSerializer        
    def post(self, request):
        serializer = feedbackandquestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})        

class Addsubscribeandnewsletter(generics.CreateAPIView):
    serializer_class=subscribeandnewsletterSerializer        
    def post(self, request):
        serializer = subscribeandnewsletterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})        

        
        
class ListCard(generics.GenericAPIView):
    serializer_class=CardSerializer        
    def get(self, request):
        queryset = Card.objects.all()
        serializer = CardSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})
            
            
            
class ListIndex(generics.GenericAPIView):
    serializer_class=IndexSerializer        
    def get(self, request):
        queryset = Index.objects.all()
        serializer = IndexSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})
            
            
            
            
            
class Listbannercard1(generics.GenericAPIView):
    serializer_class=BannerCard1Serializer        
    def get(self, request):
        queryset = CardBanner1.objects.all()
        serializer = BannerCard1Serializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})



class Listbannercard2(generics.GenericAPIView):
    serializer_class=BannerCard2Serializer        
    def get(self, request):
        queryset = CardBanner2.objects.all()
        serializer = BannerCard2Serializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class Listbannercard3(generics.GenericAPIView):
    serializer_class=BannerCard3Serializer        
    def get(self, request):
        queryset = CardBanner3.objects.all()
        serializer = BannerCard3Serializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})



# class Okview(generics.GenericAPIView):
#     def get(self, request):
#         return Response({"ok"})

class okview(generics.GenericAPIView):
    def get(self, request):

        return Response({"ok"})

class volunteeremail(generics.CreateAPIView):
    def post(self,request):
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        age_group=Agegroup.objects.get(id=request.data['age_group'])
        phone = request.data['phone']
        committee=Committee.objects.get(id=request.data['committee'])
        is_lead = request.data['is_lead']
        is_volunteer = request.data['is_volunteer']


        data ={

            'mailsubject':" Volunteer Registration",
            'firstname': firstname,
            'lastname': lastname,
            'age_group':age_group.age,
            'phone':phone,
            'committee':committee.committee,
            'is_lead':is_lead,
            'is_volunteer':is_volunteer
        }

        message = '''
             <h3> firstname:{} </h3><br> 
             <h3> lastname:{} </h3><br> 
             <h3> age_group:{} </h3><br> 
             <h3> phone:{} </h3><br> 
             <h3> committee:{} </h3><br> 
             <h3> is_lead:{} </h3><br> 
             <h3> is_volunteer:{} </h3><br> 

        '''.format(data['firstname'],data['lastname'],data['age_group'],data['phone'],data['committee']
        ,data['is_lead'],data['is_volunteer'])
        email = EmailMessage(data['mailsubject'],message,'office@icyl.org',['office@icyl.org'])
        email.content_subtype='html'
        email.send()
        return Response("success")



class Duamail(generics.CreateAPIView):
    def post(self,request):
        name = request.data['name']
        message = request.data['message']
        email = request.data['email']



        data ={

        'mailsubject':" Dua Or specialrequest",
        'name':name, 
        'message':message,
        'email':email
        }

        message = '''
             <h3> name:{} </h3><br> 
             <h3> message:{} </h3><br> 
             <h3> email:{} </h3><br> 


        '''.format(data['name'],data['message'],data['email'])
        email = EmailMessage(data['mailsubject'],message,'office@icyl.org',['office@icyl.org'])
        email.content_subtype='html'
        email.send()
        return Response("success")


class Feedbackmail(generics.CreateAPIView):
    def post(self,request):
        subject = request.data['subject']
        message = request.data['message']
        email = request.data['email']



        data ={

        'mailsubject':" Feedback",
        'subject':subject, 
        'message':message,
        'email':email


        }

        message = '''
             <h3> subject:{} </h3><br> 
             <h3> message:{} </h3><br> 
             <h3> email:{} </h3><br> 


        '''.format(data['subject'],data['message'],data['email'])
        email = EmailMessage(data['mailsubject'],message,'office@icyl.org',['office@icyl.org'])
        email.content_subtype='html'
        email.send()
        return Response("success")

class Newsletteremail(generics.CreateAPIView):
    def post(self,request):

        email = request.data['email']



        data ={

        'mailsubject':"Newsletter",

        'email':email
        }

        message = '''

             <h3> email:{} </h3><br> 


        '''.format(data['email'])
        email = EmailMessage(data['mailsubject'],message,'office@icyl.org',['office@icyl.org'])
        email.content_subtype='html'
        email.send()
        return Response("success")


#####-------------------------------------------------------------------------


                 #######################

class ListEvent_information(generics.GenericAPIView):
    serializer_class=Event_informationSerializer        
    def get(self, request):
        queryset = Event_information.objects.all()
        serializer = Event_informationSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class AddEvent_information(generics.CreateAPIView):
    serializer_class=Event_informationSerializer        
    def post(self, request):
        serializer = Event_informationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})
        
         ######################################



class Listfees(generics.GenericAPIView):
    serializer_class=feesSerializer        
    def get(self, request):
        queryset = fees.objects.all()
        serializer = feesSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class Addfees(generics.CreateAPIView):
    serializer_class=feesSerializer        
    def post(self, request):
        serializer = feesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})
        
         ######################################


class ListCategory(generics.GenericAPIView):
    serializer_class=CategorySerializer        
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class AddCategory(generics.CreateAPIView):
    serializer_class=CategorySerializer        
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})
        
         ######################################


class ListDiscount(generics.GenericAPIView):
    serializer_class=DiscountSerializer        
    def get(self, request):
        queryset = Discount.objects.all()
        serializer = DiscountSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class AddDiscount(generics.CreateAPIView):
    serializer_class=DiscountSerializer        
    def post(self, request):
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})
        
         ######################################



class ListCustom_informationSerializer(generics.GenericAPIView):
    serializer_class=Custom_informationSerializer        
    def get(self, request):
        queryset = Custom_information.objects.all()
        serializer = Custom_informationSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class AddCustom_information(generics.CreateAPIView):
    serializer_class=Custom_informationSerializer        
    def post(self, request):
        serializer = Custom_informationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})
        
         ######################################



class ListGender(generics.GenericAPIView):
    serializer_class=GenderSerializer        
    def get(self, request):
        queryset = Gender.objects.all()
        serializer = GenderSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


       ######################################



class ListParticipant(generics.GenericAPIView):
    serializer_class=ParticipantSerializer        
    def get(self, request):
        queryset = Participant.objects.all()
        serializer = ParticipantSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class AddParticipant(generics.CreateAPIView):
    serializer_class=ParticipantSerializer        
    def post(self, request):
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})
        
         ######################################


class ListPrimmary_contact(generics.GenericAPIView):
    serializer_class=Primmary_contactSerializer        
    def get(self, request):
        queryset = Primmary_contact.objects.all()
        serializer = Primmary_contactSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class AddPrimmary_contact(generics.CreateAPIView):
    serializer_class=Primmary_contactSerializer        
    def post(self, request):
        serializer = Primmary_contactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})
        
         ######################################


class Listevent_table(generics.GenericAPIView):
    serializer_class=event_tableSerializer        
    def get(self, request):
        queryset = event_table.objects.all()
        serializer = event_tableSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


class Addevent_table(generics.CreateAPIView):
    serializer_class=event_tableSerializer        
    def post(self, request):
        serializer = event_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Success", "response": {}})
        return Response({"status": False, "message": "failed", "response": serializer.errors})
        
         ######################################




class Listmeet_board(generics.GenericAPIView):
    serializer_class=meet_boardSerializer        
    def get(self, request):
        queryset = meet_board.objects.all()
        serializer = meet_boardSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

class Listprayerschedule(generics.GenericAPIView):
    serializer_class=prayerscheduleSerializer        
    def get(self, request):
        queryset = prayerschedule.objects.all()
        serializer = prayerscheduleSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})