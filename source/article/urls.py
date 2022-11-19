from django.urls import path

from .views import (
    ContentView, ArtileView, 
)

app_name = 'article'

urlpatterns = [
    path('', ContentView.as_view(), name='content'),
    # path('log-out/', LogOutView.as_view(), name='log_out'),
    path('artile/<int:artile_id>/', ArtileView.as_view(), name='artile'),
]
