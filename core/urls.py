from core.views import Home, Channel, ProfileCreate, Watch, Subscriptions, VideoDescription, ShowVideo
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', Home.as_view()),
    path('channel/', Channel.as_view()),
    path('subscription/<str:profile_id>/', Subscriptions.as_view()),
    path('profile/create/', ProfileCreate.as_view()),
    path('watch/<str:video_id>/', Watch.as_view()),
    path('video/detail/<str:video_id>/',
         VideoDescription.as_view(), name='show_det'),
    path('movie/play/<str:video_id>/', ShowVideo.as_view())
]
