"""{{cookiecutter.project_name}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),  # add path for Django admin app

    # add urls for your apps here:

    # delegate entirely to the app (add no prefix at site level)
    # path('', include('my_app.urls', namespace="my_app")),
{% if cookiecutter.rest_project %}
    # add an API
    # path('api/', include('my_api.urls', namespace="my_api")),
{% endif %}
    # all paths in my_other_app.urls will be prefixed with 'other_app_prefix'
    # path('other_app_prefix/', include('my_other_app.urls', namespace="other_app")),
]

# include Django Debug toolbar if DEBUG is set
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns