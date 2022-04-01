from django.test import TestCase
from django.urls import path
from django.conf import settings
from rest_framework import views
from .views import *
from .import views


urlpatterns = [
    
    path('api/listbanners/',ListBanners.as_view()),
    path('api/listbanner/<int:pk>/',ListBannerbyid.as_view()),
    path('api/listprayers/',ListPrayers.as_view()),
    path('api/listevents/',ListEvent.as_view()),
    path('api/listevent/<int:pk>/',ListEventbyid.as_view()),
    path('api/listvideo/',ListVideo.as_view()),
    path('api/listvideobyid/<int:pk>/',ListVideobyid.as_view()),
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
 

]
