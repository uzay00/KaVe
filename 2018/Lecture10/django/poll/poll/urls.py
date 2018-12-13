"""poll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from ProjeApp.views import index, detail, results, vote



app_name = 'ProjeApp'
urlpatterns = [
    # ex: /polls/
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    # ex: /polls/5/
    path('<int:question_id>/', detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', vote, name='vote'),
]

