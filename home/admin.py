from django.contrib import admin
from home.models import person, gallery1, gallery_subitem, Doc_file


# Register your models here.
admin.site.register(person)
admin.site.register(gallery1)
admin.site.register(gallery_subitem)
admin.site.register(Doc_file)
