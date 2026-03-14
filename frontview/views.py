from django.http import HttpResponse
from django.shortcuts import render
from frontview.helpers.events import internationalEvents, nigerianEvents
from frontview.helpers.home import nav_links, section_header, highlights, stats,policies
from frontview.helpers.research import programmes, outputs, flagshipProjects
from frontview.helpers.publications import publications,underReview,conferencePresentations
from frontview.helpers.policy import policyTopics
from .models import ConferencePresentation, FlagshipProject,Publications,Events



# Create your views here.
def homeView(request):  
    return render(request,'frontview/index.html',{'nav_links':nav_links,'active_link':"Home",
                                                    'policies':policies,
                                                  'section_header':section_header,'highlights':highlights,'stats':stats})

def aboutView(request):
    return render(request,'frontview/about.html',{'nav_links':nav_links,'active_link':"About"})


def researchView(request):
    flagshipProjects = FlagshipProject.objects.all()
    return render(request,'frontview/research.html',
                  {'nav_links':nav_links,'active_link':"Research",
                   'programmes': programmes, 'flagshipProjects': flagshipProjects,
                     'outputs': outputs})

def publicationsView(request):
    publications = Publications.objects.filter(published = True)
    underReview =  Publications.objects.filter(published = False)
    conferencePresentations = ConferencePresentation.objects.all()

    return render(request,'frontview/publications.html',
                  {'nav_links':nav_links,'active_link':"Publications",
                   'publications': publications, 'underReview': underReview,
                     'conferencePresentations': conferencePresentations})


def eventsView(request):
    nigerianEvents = Events.objects.filter(type = 'local')
    internationalEvents = Events.objects.filter(type = 'foreign')

    return render(request,'frontview/events.html',{'nav_links':nav_links,
                                                   'active_link':"Events",
                                                   'internationalEvents': internationalEvents,
                                                   'nigerianEvents': nigerianEvents})

def policyView(request):
    return render(request,'frontview/policy.html',
                  {'nav_links':nav_links,'active_link':"Policy",'policyTopics':policyTopics})

def loadData(request):
    for data in flagshipProjects:
        FlagshipProject.objects.create(**data)
    
    for data in publications:
        data['published'] = True
        Publications.objects.create(**data)
    
    for data in underReview:
        data['published'] = False
        Publications.objects.create(**data)
    
    for data in internationalEvents:
        data['type'] = 'foreign'
        Events.objects.create(**data)
    
    for data in internationalEvents:
        data['type'] = 'local'
        Events.objects.create(**data)
    
    for data in conferencePresentations:
        ConferencePresentation.objects.create(**data)

    return HttpResponse('data_loaded',status=200)
