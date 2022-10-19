from django.urls import path
from .views import HomePageView, WhoWeArePageView, HumbleBeginningPageView, ChildDevelopmentPageView,\
    FeelForPoorPageView, WhatWeDoPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('who-we-are/', WhoWeArePageView.as_view(), name = 'who-we-are'),
    path('humble-beginning/', HumbleBeginningPageView.as_view(), name = 'humble-beginning'),
    path('child-development/', ChildDevelopmentPageView.as_view(), name = 'child-development'),
    path('feel-for-poor/', FeelForPoorPageView.as_view(), name = 'feel-for-poor'),
    path('what-we-do/', WhatWeDoPageView.as_view(), name = 'what-we-do'),
    path('contact/', ContactPageView.as_view(), name = 'contact'),
]