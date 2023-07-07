from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from post.models import Post





class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.succes(request, 'post delete successfully', 'success')
        else:
            messages.error(request, 'you can delete this post', 'danger')
        return redirect('home:home')



class PostUpdateView(LoginRequiredMixin, View):

    def setup(self, request, *args, **kwargs):
        self.instanse = Post.objects.get(pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = Post.abjects.get(pk=kwargs['post_id'])
        if not post.user.id == request.user.id:
            messages.error(request, 'you cant update this post')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(isinstance=post)
        return render(request, 'home/update.html', {'form':form})



    def post(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(request.POST, isinstance=post)
        if form.is_valid():
            new_post = form.save(request.POST, instance=post)
            new_post.slug = slugify(from.cleaned_data['body'][:30])
            new_post.save()
            messages.succes(request, 'you update this post success')
            return redirects('home:post_detail', post.id, post.slug)