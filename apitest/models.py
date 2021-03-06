from django.db import models
from product.models import Product
# models就是数据模型，对应数据库的表/字段，迁移同步数据就是同步models的数据


class Apitest(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    apitestname = models.CharField('流程接口名称', max_length=64)
    apitestdesc = models.CharField('描述', max_length=64, null=True)
    apitester = models.CharField('测试负责人', max_length=16)
    apitestresult = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitestname


class Apistep(models.Model):
    Apitest = models.ForeignKey(Apitest, on_delete=models.CASCADE)
    apiname = models.CharField('接口名称', max_length=100)
    apiurl = models.CharField('url地址', max_length=200)
    apistep = models.CharField('测试步骤', max_length=100, null=True)
    apiparamvalue = models.CharField('请求参数和值', max_length=800)
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='get', max_length=200, null=True)
    apiresult = models.CharField('预期结果', max_length=200)
    apiresponse = models.CharField('响应数据', max_length=5000, null=True)
    apistatus = models.BooleanField('响应数据')
    create_time = models.DateTimeField('响应数据', auto_now=True)

    def __str__(self):
        return self.apiname


class Apis(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    apiname = models.CharField('接口名称', max_length=100)
    apiurl = models.CharField('url地址', max_length=200)
    apiparamvalue = models.CharField('请求参数和值', max_length=800)
    REQUEST_METHOD = (('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch'))
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='0', max_length=200)
    apiresult = models.CharField('预期结果', max_length=200)
    apistatus = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '单一场景接口'
        verbose_name_plural = '单一场景接口'

    def __str__(self):
        return self.apiname
