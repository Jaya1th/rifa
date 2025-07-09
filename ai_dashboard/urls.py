from django.contrib import admin
from django.urls import path, include
from courses import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
        # Add this line
        path('', views.dashboard, name='dashboard'),
    
]
