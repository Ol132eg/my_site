from django.urls import path
from.import views
urlpatterns = [
    path('', views.main),
    path('posts/', views.posts),
    path('posts/<int:number_post>/', views.number_rout_post),
    path('posts/<name_post>/', views.name_rout_post),
    path('posts/actor/1', views.name_actor),
    path('posts/blog/1', views.get_guinness_world_records),

]