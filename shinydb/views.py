from tkinter import Widget
from typing import List
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Shiny
from django.forms import widgets
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
class Main_Page(LoginRequiredMixin, ListView):
    model = Shiny
    template_name = 'shiny_list.html'
    context_object_name = 'shiny'
    ordering = ['-date_caught']
    paginate_by = 5

class ShinyListView(LoginRequiredMixin, ListView):
    model = Shiny
    template_name = 'shiny_user.html'
    context_object_name = 'shiny'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Shiny.objects.filter(author=user).order_by('-date_caught')

class ShinyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Shiny
    fields = ['nickname', 'species', 'method', 'attempts', 'date_caught']
    
    def get_form(self, form_class=None):
        form = super(ShinyUpdateView, self).get_form(form_class)
        form.fields['date_caught'].widget = widgets.SelectDateWidget(years=[i for i in range(2000, 2041)])
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Shiny Pokemon Successfully Updated!')
        return super().form_valid(form)

    def test_func(self):
        shiny = self.get_object()
        
        return self.request.user == shiny.author

class ShinyCreateView(LoginRequiredMixin, CreateView):
    model = Shiny
    fields = ['nickname', 'species', 'method', 'attempts', 'date_caught']
    
    def get_form(self, form_class=None):
        form = super(ShinyCreateView, self).get_form(form_class)
        form.fields['date_caught'].widget = widgets.SelectDateWidget(years=[i for i in range(2000, 2041)])
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Shiny Pokemon Successfully added!')
        return super().form_valid(form)

class ShinyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Shiny
    username = User.username
    success_url = '/'

    def test_func(self):
        shiny = self.get_object()
        
        return self.request.user == shiny.author

class ShinyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'shinydb/shiny_detail.html'
    model = Shiny
    context_object_name = 'shiny'
    
    success_message = 'Shiny Pokemon Added!'