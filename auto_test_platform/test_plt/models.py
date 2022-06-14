from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    # 项目类型：字典
    PROJECT_TYPE = (
        (1, 'Web'),
        (2, 'App'),
        (3, '微服务')
    )
    # 自增字段，主键
    id = models.AutoField(primary_key=True)
    # 项目名称
    name = models.CharField(max_length=200, verbose_name='测试项目名称')
    # 版本
    version = models.CharField(max_length=20, verbose_name='版本')
    # 类型
    type = models.IntegerField(verbose_name='产品类型', choices=PROJECT_TYPE)   # 32bit，4bytes
    # 描述
    description = models.CharField(max_length=200, verbose_name='项目描述', blank=True, null=True)
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态')
    # 创建人
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   db_column = 'created_by',
                                   null=True, verbose_name='创建人')
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最近更新时间')
    # 项目成员
    members = models.ManyToManyField(User, related_name='project_members',
                                     through='ProjectMember',
                                     through_fields=('project', 'user'))
    # 测试环境

    # 默认显示
    def __str__(self):
        return self.name

    # 新建一个内部类
    class Meta:
        verbose_name = '项目设置'
        verbose_name_plural = verbose_name


class ProjectMember(models.Model):
    """
    项目成员(项目和用户之间的关系)
    """
    MemberRule = (
        (1, '测试员'),
        (2, '测试组长'),
        (3, '测试经理'),
        (4, '开发'),
        (5, '运维'),
        (6, '项目经理')
    )
    # 主键
    id = models.AutoField(primary_key=True)
    # 项目
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='测试项目')
    # 用户
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='创建人')
    # 加入日期
    join_date = models.DateField(verbose_name='加入日期')
    # 角色
    role = models.IntegerField(choices=MemberRule, verbose_name='角色')
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态')
    # 退出日期
    quit_date = models.DateField(verbose_name='退出日期')
    # 备忘录
    memo = models.CharField(max_length=200, verbose_name='备忘录', blank=True, null=True)

    # 增加判空逻辑
    def __str__(self):
        if not self.user:
            return '-'
        else:
            # 张某某
            firstname = self.user.first_name if self.user.first_name else '-'
            username = self.user.username
            return f"{firstname}({username})"

    class Meta:
        verbose_name = '项目成员'
        verbose_name_plural = verbose_name


class DeployEnv(models.Model):
    # 主键
    id = models.AutoField(primary_key=True)
    # 项目
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='测试项目')
    # 名称
    name = models.CharField(max_length=50, verbose_name='环境名称')
    # 主机名
    hostname = models.CharField(max_length=50, verbose_name='主机名', help_text='主机名(IP)')
    # 端口
    port = models.IntegerField(verbose_name='端口')
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态')
    # 备忘录
    memo = models.CharField(max_length=200, verbose_name='备忘录', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部署环境'
        verbose_name_plural = verbose_name
