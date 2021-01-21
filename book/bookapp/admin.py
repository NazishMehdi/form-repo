from django.contrib import admin
from bookapp.models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    l=['title','author','ISBN','date','noOfCopiesSold']
admin.site.register(Book,BookAdmin)
