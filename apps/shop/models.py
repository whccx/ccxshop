# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Goods(models.Model):
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    now_price = models.FloatField(default=0, verbose_name="现售价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    ship_free = models.BooleanField(default=True, verbose_name="是否包邮")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='shop', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('goods_sn',)
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        保存模型时，使用pygments代码突出显示库填充突出显示的字段。
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'is_hot' if self.is_hot else False
        options = {'name': self.name} if self.name else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.goods_brief, lexer, formatter)
        super(Goods, self).save(*args, **kwargs)