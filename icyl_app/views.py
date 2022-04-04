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
    def get(self, request,pk):
        queryset = Video.objects.filter(id=pk)
        serializer = VideoSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})


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
        email = EmailMessage(data['mailsubject'],message,'abnajahana@gmail.com',['abnajahana@gmail.com'])
        email.content_subtype='html'
        email.send()
        return Response("success")