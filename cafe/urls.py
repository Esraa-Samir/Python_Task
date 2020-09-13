from django.conf.urls import url
from cafe import views


urlpatterns = [
    url(r'^api/CoffeMachine/$',  views.CoffeMachine.as_view()),
    url(r'^api/CoffePod/$',  views.CoffePod.as_view()),
]
