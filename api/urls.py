from django.urls import path
from api.views import CreatePostView
from api.views import ListPostsView

app_name = 'api'

urlpatterns = [
    path('', CreatePostView.as_view(), name='create_post'),
    path('posts/', ListPostsView.as_view(), name='list_posts')
]
