from django.contrib import admin

from loginapp.models import *

admin.site.site_title = '用户信息管理系统'
admin.site.site_header = '用户信息管理系统'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 在新增页面、修改页面设置布局
    fieldsets = (
        ('不可折叠信息', {
            'fields': ('username', 'password')
        }),
        ('可折叠信息', {
            'classes': ('collapse', ),
            'fields': ('email', ),
        })
    )
    # 设置可排序字段
    sortable_by = ['username']
    # 在数据列表页面设置显示的字段
    list_display = ['username', 'password', 'email']
    # 在数据列表页面设置跳转字段（即跳转而不编辑）
    list_display_links = ['username']
    # 在数据列表页面设置可编辑字段（即可编辑而不跳转）
    list_editable = []
    # 在数据列表页面指定每页显示数
    list_per_page = 100
    # 在数据列表页面指定每页显示最大数
    list_max_show_all = 200
    # 在数据列表页面设置过滤器
    list_filter = ['username', 'password', 'email']
    # 在数据列表页面设置可搜索字段
    search_fields = ['username', 'password', 'email']
    # 在修改页面新增“另存为”功能
    save_as = True
    # 设置动作栏的位置
    actions_on_bottom = True
    actions_on_top = False


