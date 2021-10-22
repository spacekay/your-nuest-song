from django.db import models

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    result_title = models.CharField(max_length=200)
    result_content = models.CharField(max_length=3000)
    result_like = models.IntegerField(default=0)
    result_dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.result_title


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_title = models.CharField(max_length=100)
    song_link = models.CharField(max_length=200)
    song_like = models.IntegerField(default=0)
    song_dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.song_title


class ResultSong(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    result_id = models.ForeignKey(Result, on_delete=models.CASCADE)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return "SONG: "+self.song_id+" RESULT: "+self.result_id


class Parameter(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)
e_i_para = models.IntegerField(default=0)
    n_s_para = models.IntegerField(default=0)
    f_t_para = models.IntegerField(default=0)
    p_j_para = models.IntegerField(default=0)

