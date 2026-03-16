from django.urls import path
from .import views

app_name="frontview"

urlpatterns = [
    
    path('',views.homeView,name="homeView"),  
    path('about',views.aboutView,name="aboutView"),
    path('research',views.researchView,name="researchView"),
    path('publications',views.publicationsView,name="publicationsView"),
    path('events',views.eventsView,name="eventsView"),
    path('policy',views.policyView,name="policyView"), 
    # path('loaddata',views.loadData,name="loadData"), 

]
