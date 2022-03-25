from django.urls import path
from api.views import CreatePostView, UpdatePostView
from api.views import DetailPostView
from api.views import ListPostsView
from api.views import ListPostsByAuthorView
from api.views import DeletePostView
from api.views import AuthorListView
from api.views import PostListAPIView, PostRetrieveAPIView

app_name = 'api'

urlpatterns = [
    path('', ListPostsView.as_view(), name='post_list'),
    path('posts/create', CreatePostView.as_view(), name='post_create'),
    path('posts/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
    path('posts/<int:pk>/delete', DeletePostView.as_view(), name='post_delete'),
    path('posts/<int:pk>/update', UpdatePostView.as_view(), name='post_edit'),
    path('posts/<str:author>/', ListPostsByAuthorView.as_view(), name='post_list_author'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('api/posts/', PostListAPIView.as_view(), name='api_post_list'),
    path('api/posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='api_post_detail'),
]
