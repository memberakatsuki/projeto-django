from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from . models import Post
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.

class BlogListView(ListView):
	model = Post
	template_name = 'blog/home.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	#context_object_name = 'custom'

class BlogCreateView(SuccessMessageMixin, CreateView):
	model = Post
	template_name = 'blog/post_new.html'
	fields = ('auth','title','content')
	success_message = "%(field)s - Criado com Sucesso"

	def get_success_message(self, cleaned_data):
        	return self.success_message % dict(
        	cleaned_data,
        	field=self.object.title,
        	)

class BlogUpdateView(SuccessMessageMixin, UpdateView):
	model = Post
	template_name = 'blog/post_edit.html'
	fields  = ('title','content')
	success_message = "%(field)s - Alterado com Sucesso"

	def get_success_message(self, cleaned_data):
        	return self.success_message % dict(
        	cleaned_data,
        	field=self.object.title,
        	)

class BlogDeleteView(SuccessMessageMixin, DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('home')
	success_message = "Deletado com Sucesso"

	def delete(self, request, *args, **kwargs):
			messages.success(self.request,self.success_message)
			return super(BlogDeleteView,self).delete(request, *args, **kwargs)