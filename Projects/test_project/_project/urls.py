from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('myapp/', include('myapp.urls', namespace='myapp')),

    path('todo/', include('todo.urls', namespace='todo')),

    path("accounts/", include("django.contrib.auth.urls")),

    # http://127.0.0.1:[PORT]/admin/
    path('admin/', admin.site.urls),
]

"""
We can turn text into slug by importing package and using function:
    from django.utils.text import slugify
    title = 'Nejlepsi restaurace v Praze'
    print(slugify(title)) ---> Nejlepsi-restaurace-v-Praze
"""

