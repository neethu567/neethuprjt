from django.urls import path
from . import views
app_name = 'new'

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote',views.vote,name='vote'),
    # path('',views.IndexView(),name='index'),
    # path('<int:pk>/',views.IndexView(),name='index'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

]