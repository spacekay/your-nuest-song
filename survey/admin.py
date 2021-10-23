from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Song
from .models import Result

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Song)
admin.site.register(Result)
