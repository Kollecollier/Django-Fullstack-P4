"""
Imported functions for the view code.
"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Class used from "I think therefore I blog" walkthrough.
class Postlist(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


# Class used from "I think therefore I blog" walkthrough.
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                'liked': liked,
                'comments': comments,
                'commented': False,
                'post': post,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Submit a comment to a
        blog post.
        """
        themessage = None
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(request.POST, instance=request.user)
#        comment_form = CommentForm(data=request.POST)
        if request.method == 'POST':
            comment_id = request.POST.get('comment_id')
            if comment_id is not None:
                comment_instance = Comment.objects.get(user=request.user, id=comment_id, post__slug=slug)
                print(request.POST.get('updated_comment'))
                comment_instance.body = request.POST.get('updated_comment')
                comment_instance.save()
                messages.info(request, 'Your comment has been updated !')

            else:
                comment_form = CommentForm(request.POST)
                comment = Comment()
                if comment_form.is_valid():
                    print('valid')
                    comment.post = post
                    comment.body = comment_form.cleaned_data['body']
                    comment.user = request.user
                    comment.save()
                    messages.info(request, 'Your comment is being reviewed for approval')

        return render(
                request,
                "post_detail.html",
                {
                    'liked': liked,
                    'comments': comments,
                    'commented': True,
                    'post': post,
                    'comment_form': CommentForm(),
                },
            )


# Class used from "I think therefore I blog" walkthrough.
class PostLike(View):
    """
    Allows user to like a
    blog post submission
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return HttpResponseRedirect("/")


def post_update(request, slug):
    return HttpResponseRedirect("/")


def remove_comment(request, slug):
    try:
        comment = Comment.objects.get(post__slug=slug, user=request.user)
        comment.delete()
        messages.info(request, 'Your Comment Was Deleted !')
        return redirect('post_detail', slug)
    except Comment.DoesNotExist:
        messages.error(request, 'You do not have an active comment !')
        return redirect('post_detail', slug)
