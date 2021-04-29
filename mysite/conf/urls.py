"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views as views

# Below is a list of the urls used for the login page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('accounts/login/', views.login, name='login'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', views.signup, name='signup'),
    path('signout/',views.signout,name='signout'),
    path('new_story/', views.new_story, name="new_story"),
    path('save_story/', views.save_story, name="save_story"),
    path('load_story/', views.load_story, name="load_story"),
    path('storycreator/', views.storyboard, name="storyboard"),
    path('addclue/', views.add_clue, name="add_clue"),
    path('removeclue/', views.remove_clue, name="remove_clue"),
    path('refresh/', views.refresh_story, name="refresh_story"),
    path('display_clues/', views.display_clues, name="display_clues"),
    path('return_to_editor/', views.return_to_editor, name="return_to_editor")
]
