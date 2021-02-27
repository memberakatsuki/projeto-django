from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from . models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(ListView):
	model = Post
	template_name = 'blog/home.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	#context_object_name = 'custom'

class BlogCreateView(CreateView):
	model = Post
	template_name = 'blog/post_new.html'
	fields = ('auth','title','content')

class BlogUpdateView(UpdateView):
	model = Post
	template_name = 'blog/post_edit.html'
	fields  = ('title','content')

class BlogDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('home')