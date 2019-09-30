from django.contrib import admin
from .models import Blog  # Importing the Blog model

# Registering the Blog model to admin
admin.site.register(Blog)
