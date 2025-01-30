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
from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index_page),

    # http://127.0.0.1:[PORT]/url-paths/
    path('url-paths/', views.url_paths),

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

    # http://127.0.0.1:[PORT]/clanky/mista-na-kavu-1425324/
    path('article/<slug:name>-<int:number>/', views.article),

    # http://127.0.0.1:[PORT]/pages/number/name
    path('pages/<int:number>/<slug:name>', views.pages),

    # http://127.0.0.1:[PORT]/age/
    path('age/', views.age),

    # http://127.0.0.1:[PORT]/admin/
    path('login/', views.login),

    # http://127.0.0.1:[PORT]/signup/
    path('signup/', views.signup)

]

"""
We can turn text into slug by importing package and using function:
    from django.utils.text import slugify
    title = 'Nejlepsi restaurace v Praze'
    print(slugify(title)) ---> Nejlepsi-restaurace-v-Praze
"""

