#from django.db import models


#class Story(models.Model):
#    details = models.CharField(max_length=500)
#    photo = models.ImageField(upload_to='evidence')
#    parent_clue = models.CharField(max_length=100)


#class Clue(models.Model):
    # once story database is complete edit this to connect the two together
    # story_title = models.ForeignKey(Story, on_delete=models.CASCADE)
#    story_title = models.CharField(max_length=20, primary_key=True)
#    clue_num = models.IntegerField(primary_key=True)
#    clue_text = models.CharField(max_length=1000, default='')
#   clue_img_url = models.TextField(default='')


#class Clue_Parent(models.Model):
#    clue_num = models.ForeignKey(Clue, on_delete=models.CASCADE, primary_key=True)
#    parent_num = models.ForeignKey(Clue, on_delete=models.CASCADE, primary_key=True)


#class Clue_Children(models.Model):
#    clue_num = models.ForeignKey(Clue, on_delete=models.CASCADE, primary_key=True)
#    child_num = models.ForeignKey(Clue, on_delete=models.CASCADE, primary_key=True)
