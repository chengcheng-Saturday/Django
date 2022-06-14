from django.db import models
from django.contrib.auth.models import User
from test_plt.models import Project


# Create your models here.
class ApiTest(models.Model):
    # 主键，用例编号
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='测试项目')
    # 用例名称
    api_test_name = models.CharField(max_length=64, verbose_name='用例名称')
    # 用例描述
    api_test_desc = models.CharField(max_length=64, verbose_name='用例描述')
    # 用例执行人
    api_tester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='用例执行人')
    # 测试结果
    api_test_result = models.BooleanField(verbose_name='测试结果')
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 更新时间
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最近更新时间')

    def __str__(self):
        return self.api_test_name

    class Meta:
        verbose_name = '用例管理'
        verbose_name_plural = verbose_name


class ApiStep(models.Model):
    # 关联接口ID
    api_test = models.ForeignKey(ApiTest,null=False, on_delete=models.CASCADE,verbose_name='用例名称')
    # 用例标题
    api_name = models.CharField(max_length=100, verbose_name='用例标题')
    # 接口地址
    api_url = models.CharField(max_length=200, verbose_name='接口地址')
    # 测试步骤
    api_step = models.CharField(max_length=100, verbose_name='测试步骤', null=True)
    # 参数和值
    api_param_value = models.CharField(max_length=800, verbose_name='参数和值')
    # 请求方法，字典
    REQUEST_METHOD = (
        ('get', 'get'),
        ('post', 'post'),
        ('put', 'put'),
        ('delete', 'delete'),
        ('patch', 'patch')
    )
    api_method = models.CharField(choices=REQUEST_METHOD, default='get',
                                  max_length=200, null=True, verbose_name='请求方法')
    # 预期结果
    api_result = models.CharField(max_length=200, verbose_name='预期结果')
    # 响应数据
    api_response = models.CharField(max_length=5000, null=True, verbose_name='响应数据')
    # 是否通过
    api_status = models.BooleanField(verbose_name='是否通过')
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 更新时间
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最近更新时间')

    def __str__(self):
        return self.api_name


    class Meta:
        verbose_name = '接口信息'
        verbose_name_plural = verbose_name