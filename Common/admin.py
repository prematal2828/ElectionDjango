from django.contrib import admin

from Common.models import *

from Common.models import Country

# Register your models here.
admin.site.register(Country)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)
admin.site.register(Union)
admin.site.register(Ward)
admin.site.register(CityCorporation)
admin.site.register(Municipality)

