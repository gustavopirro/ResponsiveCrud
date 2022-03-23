from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import FormView
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from api.forms import PostForm
from api.models import Post


class CreatePostView(FormView):
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('api:post_list')

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


class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class DeletePostView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_confirm_delete.html'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        post_id = self.kwargs.get('pk')
        post = Post.objects.get(pk=post_id)

        if post.author == self.request.user:
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.updated = True
            post.save()
        else:
            return HttpResponseForbidden()

        return HttpResponseRedirect(self.get_success_url())


class SignUpView(FormView):
    template_name = 'create_post.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('api:post_list')

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)
