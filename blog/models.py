from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    like_count = models.PositiveIntegerField(default=0) # 양수입력 필드
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'boards'

class Reply(models.Model):
    reply = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rep_date = models.DateTimeField()

    def __str__(self):
        return self.comment
    
    class Meta:
        db_table = 'replies'