from django.urls import path
from api.views import CreatePostView
from api.views import DetailPostView
from api.views import ListPostsView

app_name = 'api'

urlpatterns = [
    path('', ListPostsView.as_view(), name='post_list'),
    path('posts/create', CreatePostView.as_view(), name='post_create'),
    path('posts/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
]
