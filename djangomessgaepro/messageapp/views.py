from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
# Create your views here.
from .models import *

class PostView(SuccessMessageMixin, generic.CreateView):
	model = Post
	fields = '__all__'
	template_name = 'post.html'
	success_url = reverse_lazy('post')
	success_message = "post was created successfully"
