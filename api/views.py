from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import FormView
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from api.forms import PostForm
from api.models import Post
from django.contrib.auth.models import User


class AuthorListView(ListView):
    template_name = 'author_list.html'
    context_object_name = 'authors_list'

    def get_queryset(self):
        authors = User.objects.all()
        authors_list = []
        for author in authors:
            authors_list.append({
                'author': author,
                'last_post': Post.objects.filter(author=author).last()
            })
        return authors_list


class ListPostsByAuthorView(ListView):
    template_name = 'post_list.html'

    def get_queryset(self):
        queryset = Post.objects.filter(author__username=self.kwargs.get('author'))
        return queryset


class CreatePostView(LoginRequiredMixin, FormView):
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


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):

        if request.user != self.get_object().author:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class UpdatePostView(LoginRequiredMixin, UpdateView):
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

    def dispatch(self, request, *args, **kwargs):

        if request.user != self.get_object().author:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class SignUpView(FormView):
    template_name = 'create_post.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('api:post_list')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)
