# blog/models.py

import re
from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models


def lnglat_validator(value):
    if not re.match(r'^[+-]?\d+\.?\d*,[+-]?\d+\.?\d*$', value):
        raise forms.ValidationError('경도,위도를 입력해주세요.')


class Post(models.Model):
    # print("[class Post 호출]") # server on..
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(default='') #no옵션 필수필드 #경로만 저장
    lnglat = models.CharField(max_length=40, blank=True, validators=[lnglat_validator]) 
    # PointField GeoDjango 
    is_public = models.BooleanField(default=False) # 공개여부
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]
        return None
    
    @property
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[1]
        return None

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'id': self.pk})
    



class Comment(models.Model):
    # Post : Comment = 1 : N
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL) # auth.User
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def get_edit_url(self):
        #print('who are you...????', self.pk,'//', self.created_at)
        # reverse()가 url 을 반환해주나? str으로 ..?????  
        #print('~~~~~~~``', type(reverse('blog:comment_edit', args=[self.post.pk, self.pk])))
        #str
        #print("33333333", reverse('blog:comment_edit', args=[self.post.pk, self.pk]))
        #/blog/1/commit/1/edit/
        return reverse('blog:comment_edit', args=[self.post.pk, self.pk])

    def get_delete_url(self):
        return reverse('blog:comment_delete', args=[self.post.pk, self.pk])