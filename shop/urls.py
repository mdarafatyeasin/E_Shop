from django.urls import path
from . import views 


urlpatterns = [
    path('by_now/<int:id>',views.byNow, name="by_now"),
]
