from django.urls import path
from .views import ArtistAPIView

urlpatterns = [
    path('', ArtistAPIView.as_view(), name='artist-api-view')
]
