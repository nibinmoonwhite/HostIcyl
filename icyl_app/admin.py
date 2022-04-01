from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from icyl_app.models import Agegroup,Banners,Card,Committee,Event,Form,Prayer,Video,Index,CardBanner1, CardBanner2, CardBanner3

# Register your models here.
from icyl_app.models import *

admin.site.site_header = "ICYL ADMIN"
admin.site.site_title = "ICYL Admin Portal"
admin.site.index_title = "Welcome To ICYL Portal"

@admin.register(Prayer)
class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'prayer_name','iqamat_time','namas_time','image')


@admin.register(Banners)
class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_image1','link')


@admin.register(Event)
class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'image','date','event_name','time','description','location')


@admin.register(Video)
class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'video')

@admin.register(Committee)
class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'committee')


# admin.site.register(Form)
# @admin.register(Form)
# class FormAdmin(admin.ModelAdmin):
#     list_display = ('id', 'firstname','lastname','age_group','phone','email','committee','is_lead','is_volunteer')

@admin.register(Agegroup)
class AgegroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'age')

@admin.register(Form)
class FormAdmin(ImportExportModelAdmin):
    list_display =('id', 'firstname','lastname','age_group','phone','email','committee','is_lead','is_volunteer')
    
    

@admin.register(Card)
class AgegroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'image','image2','title','description')
    
    
@admin.register(Index)
class IndexgroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'inner_banner', 
        'footer','logo','main_menu','post1','donations')
        
@admin.register(CardBanner1)
class IndexgroupAdmin(admin.ModelAdmin):
    list_display =('id', 'image')

@admin.register(CardBanner2)
class IndexgroupAdmin(admin.ModelAdmin):
    list_display =('id', 'image')

@admin.register(CardBanner3)
class IndexgroupAdmin(admin.ModelAdmin):
    list_display =('id', 'image')
    
    
    
@admin.register(duaandspecialrequests)
class IndexgroupAdmin(admin.ModelAdmin):
    list_display =('id', 'name','email','message')

@admin.register(feedbackandquestions)
class IndexgroupAdmin(admin.ModelAdmin):
    list_display =('id', 'subject','email','message')

@admin.register(subscribeandnewsletter)
class IndexgroupAdmin(admin.ModelAdmin):
    list_display =('id', 'email')

