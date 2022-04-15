from django.test import TestCase
from django.urls import path
from django.conf import settings
from rest_framework import views
from .views import *
from .import views


urlpatterns = [
    path('',okview.as_view()),
    # path('',Okview.as_view()),
    path('api/listbanners/',ListBanners.as_view()),
    path('api/listbanner/<int:pk>/',ListBannerbyid.as_view()),
    path('api/listprayers/',ListPrayers.as_view()),
    path('api/listevents/',ListEvent.as_view()),
    path('api/listevent/<int:pk>/',ListEventbyid.as_view()),
    path('api/listvideo/',ListVideo.as_view()),
    path('api/listvideobyid/',ListVideobyid.as_view()),
    path('api/listagegroup/',ListAgegroup.as_view()),
    path('api/listcommittee/',ListCommittee.as_view()),
    path('api/addform/',AddForm.as_view()),
    path('api/listcard/',ListCard.as_view()),
    path('api/listindex/',ListIndex.as_view()),

    path('api/listbannercard1/',Listbannercard1.as_view()),
    path('api/listbannercard2/',Listbannercard2.as_view()),
    path('api/listbannercard3/',Listbannercard3.as_view()),
    
    
    path('api/addduaandspecialrequests/',Addduaandspecialrequests.as_view()),
    path('api/addfeedbackandquestions/',Addfeedbackandquestions.as_view()),
    path('api/addsubscribeandnewsletter/',Addsubscribeandnewsletter.as_view()),
    path('api/volunteeremail/',volunteeremail.as_view()), 


    path('api/duamail/',Duamail.as_view()), 
    path('api/feedbackmail/',Feedbackmail.as_view()), 
    path('api/newsletteremail/',Newsletteremail.as_view()), 



    #---------------------15/april/2021-----------------------------------


    path('api/ListEvent_information/',ListEvent_information.as_view()), 
    path('api/AddEvent_information/',AddEvent_information.as_view()), 

    path('api/Listfees/',Listfees.as_view()), 
    path('api/Addfees/',Addfees.as_view()), 


    path('api/ListCategory/',ListCategory.as_view()), 
    path('api/AddCategory/',AddCategory.as_view()), 

    path('api/ListDiscount/',ListDiscount.as_view()), 
    path('api/AddDiscount/',AddDiscount.as_view()), 


    path('api/ListCustom_informationSerializer/',ListCustom_informationSerializer.as_view()), 
    path('api/AddCustom_information/',AddCustom_information.as_view()), 

    path('api/ListGender/',ListGender.as_view()), 


    path('api/ListParticipant/',ListParticipant.as_view()), 
    path('api/AddParticipant/',AddParticipant.as_view()), 

    path('api/ListPrimmary_contact/',ListPrimmary_contact.as_view()), 
    path('api/AddPrimmary_contact/',AddPrimmary_contact.as_view()), 

    path('api/Listevent_table/',Listevent_table.as_view()), 
    path('api/Addevent_table/',Addevent_table.as_view()), 

    #----------------end-----15/april/2021-----------------------------------


]
