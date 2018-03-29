from django.contrib import admin
from django.urls import path, include

from quiz import urls as quiz_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include(quiz_urls)),
]
