from django.db import models


# stores all the clues information in regards to the story within the database
class Clue(models.Model):
    # once story database is complete edit this to connect the two together
    # story_title = models.ForeignKey(Story, on_delete=models.CASCADE)
    # story = models.ForeignKey(Story, on_delete=models.CASCADE)
    clue_id = models.IntegerField()
    clue_num = models.IntegerField()
    clue_text = models.CharField(max_length=1000, default='')
    clue_img_url = models.TextField(default='')
    parent_list = models.TextField(default='[]')

    # class Meta:
    #    unique_together = (("story_title", "clue_id"),)

    # def __str__(self):
    #    return '(Story: ' + str(self.story_title) + ' Clue: ' + str(self.clue_id) + ')'
######################################################################
