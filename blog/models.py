# blog/models.py

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(default='') #no옵션 필수필드 #경로만 저장
    is_public = models.BooleanField(default=False) # 공개여부
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title