"""
URL configuration for PersonalBudget project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# We always want to use include() for including URLs patterns, 'admin.site.urls' is the only exception to this
# We use this patter so that we can include all the URLs from an app to the main app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('', include('users.urls')),
    path('', include('transactions.urls')),
    path('', include('budget.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
