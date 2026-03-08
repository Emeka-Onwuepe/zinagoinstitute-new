from django.shortcuts import render
from frontview.helpers.events import internationalEvents, nigerianEvents
from frontview.helpers.home import nav_links, section_header, highlights, stats
from frontview.helpers.research import programmes, flagshipProjects, outputs
from frontview.helpers.publications import publications,underReview,conferencePresentations
from frontview.helpers.policy import policyTopics



# Create your views here.
def homeView(request):  
    return render(request,'frontview/index.html',{'nav_links':nav_links,'active_link':"Home",
                                                  'section_header':section_header,'highlights':highlights,'stats':stats})

def aboutView(request):
    return render(request,'frontview/about.html',{'nav_links':nav_links,'active_link':"About"})


def researchView(request):
    return render(request,'frontview/research.html',
                  {'nav_links':nav_links,'active_link':"Research",
                   'programmes': programmes, 'flagshipProjects': flagshipProjects,
                     'outputs': outputs})

def publicationsView(request):
    return render(request,'frontview/publications.html',
                  {'nav_links':nav_links,'active_link':"Publications",
                   'publications': publications, 'underReview': underReview,
                     'conferencePresentations': conferencePresentations})


def eventsView(request):
    return render(request,'frontview/events.html',{'nav_links':nav_links,
                                                   'active_link':"Events",
                                                   'internationalEvents': internationalEvents,
                                                   'nigerianEvents': nigerianEvents})

def policyView(request):
    return render(request,'frontview/policy.html',
                  {'nav_links':nav_links,'active_link':"Policy",'policyTopics':policyTopics})

