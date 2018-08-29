from django.shortcuts import redirect, render, get_object_or_404
from article.models import Article, Tag, Comment
from article.forms import CommentForm
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def home(request):
    post_list = Article.objects.all().order_by('date_time')  # 获取全部的Article对象
    tag_list = Tag.objects.all()

    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'contacts': contacts, 'tag_list': tag_list})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list})


def search_tag(request, tag):
    try:
        p_list = Article.objects.filter(tag_name__name__iexact=tag)  # contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post': p_list})


def detail(request, id):
    post = Article.objects.get(id=id)
    all_comment = Comment.objects.filter(article__id=id)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'detail.html', {'post': post, 'all_comment': all_comment, 'comment_form': comment_form})



