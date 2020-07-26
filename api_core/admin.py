from django.contrib import admin
from .models import User, Agent, Group, GroupUser

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Group)
admin.site.register(GroupUser)
