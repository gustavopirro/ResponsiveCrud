from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import ListView
from api.forms import PostForm
from api.models import Post


class CreatePostView(FormView):
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('api:list_posts')

    def form_valid(self, form):
        Post.objects.create(
            title=form.cleaned_data['title'].capitalize(),
            content=form.cleaned_data['content'].capitalize(),
            author=self.request.user
            )
        return super().form_valid(form)


class ListPostsView(ListView):
    queryset = Post.objects.all().order_by('-creation_date')
    template_name = 'post_list.html'
