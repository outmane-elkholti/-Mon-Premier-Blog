from django.contrib import admin
from .models import Post
from .models import Commentaire


admin.site.register(Post)
admin.site.register(Commentaire)
