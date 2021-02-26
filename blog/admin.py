from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'auth', 'published', 'status')

	list_filter = ('status', 'created', 'published', 'auth')

	raw_id_fields = ('auth',)

	date_hierarchy = 'published'

	search_fields = ('title', 'content')

	prepopulated_fields = {'slug':('title',)}

# Register your models here.
