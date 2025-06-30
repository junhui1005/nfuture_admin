from django.shortcuts import render
from .models import Member, Post

def dashboard(request):
    member_count = Member.objects.count()
    post_count = Post.objects.count()
    return render(request, 'core/dashboard.html', {
        'member_count': member_count,
        'post_count': post_count,
    })
