from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=100, default='')
    synopsis = models.CharField(max_length=500, default='')
    num_clues = models.IntegerField()
    user = models.CharField(max_length=100, default='')

    class Meta:
        unique_together = (("title", "user"),)


# stores all the clues information in regards to the story within the database
class Clue(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, default=1)
    clue_id = models.IntegerField()
    clue_num = models.IntegerField()
    clue_text = models.CharField(max_length=1000, default='')
    clue_img_url = models.TextField(default='')
    parent_clues = models.TextField(default='[]')
   

    class Meta:
        unique_together = (("story", "clue_id"),)
######################################################################
