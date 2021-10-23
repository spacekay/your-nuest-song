from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Song
from .models import Result
from .models import ResultSong
from .models import Parameter

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Song)
admin.site.register(Result)
admin.site.register(ResultSong)
admin.site.register(Parameter)
