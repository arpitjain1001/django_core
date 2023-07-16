from django.urls import path
from . import views





urlpatterns = [
  path('tips/',views.tips),
  path('world/',views.world),
  path('index/',views.index),
  path('about/',views.about),
  path('contact/',views.contact)
  # path('base/',views.base),
  # path('admin/',admin.site.urls),
]