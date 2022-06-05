from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Project
from .models import ProjectMember
from .models import DeployEnv

# 第一步创建ModelAdmin的继承类
class ProjectAdmin(ModelAdmin):
    # 第二步指定要显示的列，字段
    list_display = ['id', 'name', 'type', 'status', 'created_by', 'updated_at', 'description']
    # 第三步指定可参与过滤的列
    list_filter = ['created_at', 'type', 'name']
    # 第四步指定可查询的列
    search_fields = ['name']
    list_per_page = 10
    # 设置可编辑列表
    list_editable = ['type', 'status']
    # 搜索帮助文本
    search_help_text = '请输入项目名称进行搜索'
    list_display_links = ['name']
    pass


# Register your models here.
# 将子类也在此注册
admin.site.register(Project, ProjectAdmin)


class ProjectMemberAdmin(ModelAdmin):
    # 设置指定要显示的列，字段
    list_display = ['id', 'project', '__str__', 'join_date', 'role', 'status']
    # 设置连接字段
    list_display_links = ['__str__']
    # 指定可参与过滤的列
    list_filter = ['join_date', 'role', 'status']
    search_fields = ['user__first_name', 'user__username', 'project__name', 'project__id']
    list_per_page = 10


admin.site.register(ProjectMember, ProjectMemberAdmin)


class DeployEnvAdmin(ModelAdmin):
    # 设置指定要显示的列，字段
    list_display = ['id', 'project', 'name', 'hostname', 'port', 'status', 'memo']
    # 设置连接字段
    list_display_links = ['name']
    # 指定可参与过滤的列
    list_filter = ['status']
    search_fields = ['name', 'hostname', 'memo', ]
    list_per_page = 10


admin.site.register(DeployEnv, DeployEnvAdmin)


admin.site.site_header = '自动化测试平台后台管理'
admin.site.site_title = '自动化测试平台后台'
