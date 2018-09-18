# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models


#==============抽象基类=======================================================

class Basegoods(models.Model):
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True
        ordering = ('goods_sn',)
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#=============商品信息========================================================

class Goodsinfo(Basegoods):
    owner = models.ForeignKey('auth.User', related_name='Goodsinfo', on_delete=models.CASCADE)
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    now_price = models.FloatField(default=0, verbose_name="现售价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    ship_free = models.BooleanField(default=True, verbose_name="是否包邮")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")

    class Meta:
        db_table = 'Goodsinfo'
        verbose_name = "商品信息"

    def save(self, *args, **kwargs):
        """
        保存商品信息模型。
        """
        super(Goodsinfo, self).save(*args, **kwargs)

#=============商品参数========================================================

class Goodsparameter(Basegoods):
    yellow,white,orange,green,red,blue,purple,grey,black,khaki=0,1,2,3,4,5,6,7,8,9

    good_color = {
        yellow: '黄色',white: '白色',orange: '橙色',green: '绿色',red:'红色',
        blue: '蓝色',purple: '紫色',grey: '灰色',black: '黑色',khaki:'卡其色'
    }

    color_choices = ((k, v) for k, v in good_color.items())

    #=================
    small,litter,big,addbig = 0,1,2,3
    good_size = {small:'S',litter:'L',big:'XL',addbig:'XXL'}
    size_choices = ((k, v) for k, v in good_size.items())

    owner = models.ForeignKey('auth.User', related_name='Goodsparameter', on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    goods_brand = models.TextField(max_length=50, verbose_name="品牌")
    goods_size = models.SmallIntegerField(default=small, choices=size_choices, verbose_name="尺码")
    goods_color = models.SmallIntegerField(default=yellow, choices=color_choices, verbose_name="颜色")

    class Meta:
        db_table = 'Goodsparameter'
        verbose_name = "商品参数"

    def save(self, *args, **kwargs):
        """
        保存商品参数模型。
        """
        super(Goodsparameter, self).save(*args, **kwargs)