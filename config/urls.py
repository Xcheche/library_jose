"""
URL configuration for config project.

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
from django.urls import include, path
from django.views.generic import RedirectView  # Automatic redirect

# from django.contrib.auth import views as auth_views
urlpatterns = [
    path("catalog/", include("catalog.urls")),
    path("admin/", admin.site.urls),
    # Automatic redirect
    path("", RedirectView.as_view(url="/catalog/")),
    # Auth by default from django
    path("accounts/", include("django.contrib.auth.urls")),
    # Custom logout view with a specific template
    # path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
]
