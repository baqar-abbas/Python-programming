from django.contrib import admin
from .models import Member

# Register your models here.

# Set list_display
# We can control the fields to display by specifying them in a list_display property in the admin.py file.

# First create a MemberAdmin() class and specify the list_display tuple:

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'joined_date')

admin.site.register(Member, MemberAdmin)
