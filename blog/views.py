from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Post, Comment


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list':post_list,
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {
        'post':post,
    }) 

@login_required
def comment_new(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False) # param..??
            comment.post = post
            comment.author = request.user
            # print('comment_new::', comment.author.email)
            comment.save()
            return redirect('blog:post_detail', post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form':form,
        'post':post,
    })


@login_required
def comment_edit(request, post_id, id):
    comment = get_object_or_404(Comment, id=id)
    # print('typeof', type(comment)) #typeof <class 'blog.models.Comment'>
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            #comment = form.save(commit=False) # param..??
            #comment.post = post
            #comment.author = request.user
            # print('comment_new::', comment.author.email)
            comment.save()
            #return redirect('blog:post_detail', post.id)
            return redirect(comment.post) 
            # get_absolute_url() 설정을 model에 해놔서 => post_detail.html
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {
        'form':form,
        'post':post,
    })


@login_required
def comment_delete(request, post_id, id):
    comment = get_object_or_404(Comment, id=id)
    
    if request.method == 'POST':
        comment.delete()
        return redirect(comment.post)
    else:
        print('nothing to do.')
    return render(request, 'blog/comment_delete.html', {
        'comment':comment,
    })