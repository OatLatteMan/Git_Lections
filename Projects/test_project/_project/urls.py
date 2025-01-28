"""
URL configuration for _project project.

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
from myapp import views

urlpatterns = [
    path('', views.index_page),

    # http://127.0.0.1:[PORT]/url-paths/
    path('url-paths/', views.url_paths),

    # http://127.0.0.1:[PORT]/admin/
    path('admin/', admin.site.urls),

    # http://127.0.0.1:[PORT]/my-math/
    path('my-math/', views.my_math),

    # http://127.0.0.1:[PORT]/test-template/
    path('test-template/', views.test_template),

    # http://127.0.0.1:[PORT]/calculator/
    path('calculator/', views.calculator),

    # http://127.0.0.1:[PORT]/time/
    path('time/', views._time),

    # http://127.0.0.1:[PORT]/jmeno/[any string]/
    path('jmeno/<str:name>/', views.my_page),

    # http://127.0.0.1:[PORT]/age/
    path('age/', views.age),

    # http://127.0.0.1:[PORT]/admin/
    path('login/', views.login)

]
