from django.urls import path, re_path
from . import views
app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path('',views.IndexView.as_view(), name ='index'),
    # ex: /polls/1/
    # path('<int:question_id>/', views.detail, name='detail'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/1/results/
    re_path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/1/vote/
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]