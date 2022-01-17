from django.urls import path
from .views import activity_logger

app_name = 'activity_logger'

urlpatterns = [
    path('activity-logger/', activity_logger, name='activity_logger')
]
