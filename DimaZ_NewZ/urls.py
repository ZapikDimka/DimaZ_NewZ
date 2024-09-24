"""
URL configuration for DimaZ_NewZ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello import views
from django.conf import settings  # Import the settings to access MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static  # Import static to serve media files during development


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Route for the home page
    path('news/', views.all_news, name='all_news'),  # Route for the full news list
    path('news/<int:new_id>/', views.news_detail, name='news_detail'),  # Route for a specific news article
    path('authors/', views.authors_list, name='authors_list'),  # Route for the list of authors
    path('authors/<int:author_id>/news/', views.author_news, name='author_news'),  # Route for news by a specific author
]
# This enables Django to serve uploaded media files, such as images, during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)