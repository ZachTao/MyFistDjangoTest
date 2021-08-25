from django.contrib import admin
from set.models import Set


class SetAdmin(admin.ModelAdmin):
    list_display = ['setname', 'setvalue', 'id']


admin.site.register(Set)  # 把Set系统设置模块注册到django admin 后台并显示
