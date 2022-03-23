from django.urls import path
from api.views import CreatePostView
from api.views import DetailPostView
from api.views import ListPostsView
from api.views import DeletePostView

app_name = 'api'

urlpatterns = [
    path('', ListPostsView.as_view(), name='post_list'),
    path('posts/create', CreatePostView.as_view(), name='post_create'),
    path('posts/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
    path('posts/<int:pk>/delete', DeletePostView.as_view(), name='post_delete')
]
