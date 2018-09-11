from django.contrib import admin
from app2.models import Topic
from app2.models import AccessRecord
from app2.models import Webpage


admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
