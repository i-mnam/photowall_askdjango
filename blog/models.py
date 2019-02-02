# blog/models.py

import re
from django import forms
from django.db import models


def lnglat_validator(value):
    if not re.match(r'^[+-]?\d+\.?\d*,[+-]?\d+\.?\d*$', value):
        raise forms.ValidationError('경도,위도를 입력해주세요.')


class Post(models.Model):
    print("[class Post 호출]") # server on..
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