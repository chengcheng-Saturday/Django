from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import ApiTest, ApiStep


# Register your models here.
class ApiStepAdmin(admin.TabularInline):
    # 指定展示的列
    list_display = ['api_name', 'api_url', 'api_method', 'api_result',
                    'api_status', 'created_at', 'updated_at', 'id', 'api_test']
    model = ApiStep
    extra = 1


@admin.register(ApiTest)
class ApiTestAdmin(admin.ModelAdmin):
    list_display = ['api_test_name', 'api_tester', 'api_test_result', 'id', 'created_at', 'updated_at']
    inlines = [ApiStepAdmin]


admin.site.site_header = '自动化测试平台后台管理'
admin.site.site_title = '自动化测试平台后台'
