from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class WhoWeArePageView(TemplateView):
    template_name = 'who-we-are.html'

class HumbleBeginningPageView(TemplateView):
    template_name = 'humble-beginning.html'

class ChildDevelopmentPageView(TemplateView):
    template_name = 'child-development-model.html'

class FeelForPoorPageView(TemplateView):
    template_name = 'feel-for-poor.html'

class WhatWeDoPageView(TemplateView):
    template_name = 'what-we-do.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'