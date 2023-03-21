from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import Board

# Create your views here.

def index(request):
    all_boards = Board.objects.all().order_by("-pub_date") # 모든 데이터 조회, 내림차순(-표시) 조회
    return render(request, 'blog/index.html', {'title':'board List', 'board_list':all_boards})

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'blog/detail.html', {'board': board})

def write(request):
    return render(request, 'blog/write.html')

def write_board(request):
    b = Board(title=request.POST['title'], content=request.POST['detail'], author="min", pub_date=timezone.now())
    b.save()
    return HttpResponseRedirect(reverse('blog:index'))

def create_reply(request, board_id):
    b = Board.objects.get(id = board_id)
    b.reply_set.create(comment=request.POST['comment'], rep_date=timezone.now())
    return HttpResponseRedirect(reverse('blog:detail', args=(board_id,)))