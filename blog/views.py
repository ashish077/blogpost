from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import post
# Create your views here.
def post_list(request):
post=post.objects.filter(Published_date__lte=timezone.now()).order_by('Publishd_date')
    return render(request,'blog/post_list.html',{'Posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
