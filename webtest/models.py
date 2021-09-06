from django.db import models
from product.models import Product


class Webcase(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    # on_delete=models.CASCADE 级联删除,主表数据被删除时候，从表数据也要被删除
    webcasename = models.CharField('用例名称', max_length=200)
    webtestresult = models.BooleanField('测试结果')
    webtester = models.CharField('测试负责人', max_length=16)
    create_time = models.DateTimeField('创建时间', auto_now=True)


class Meta:
    verbose_name = 'web测试用例'  # admin页面中显示，单数形式（中文没区别）
    verbose_name_plural = 'web测试用例'  # admin页面中显示，单数形式（中文没区别）

    def __str__(self):
        return self.verbose_name


class Webcasestep(models.Model):
    Webcase = models.ForeignKey(Webcase, on_delete=models.CASCADE)
    webcasename = models.CharField('测试用例标题', max_length=200)
    webteststep = models.CharField('测试用例步骤', max_length=200)
    webtestobjname = models.CharField('测试对象名称描述', max_length=200)
    webfindmethod = models.CharField('定位方式', max_length=200)
    webvelement = models.CharField('控件元素', max_length=800)
    weboptmethod = models.CharField('操作方法', max_length=200)
    webtestdata = models.CharField('测试数据', max_length=200, null=True)
    webassertdata = models.CharField('验证数据', max_length=200)
    webtestresult = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.webcasename
