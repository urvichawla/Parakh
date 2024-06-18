from django.db import models
# Create your models here.

class QuizCategory(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    # image=models.ImageField(upload_to='cat_imgs/')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

class QuizLevel(models.Model):
    level=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Level'

    def __str__(self):
        return self.level
    
class QuizQuestion(models.Model):
    category=models.ForeignKey(QuizCategory, on_delete=models.CASCADE, related_name='category_set', null=True)
    level=models.ForeignKey(QuizLevel, on_delete=models.CASCADE, related_name='level_set')
    question=models.TextField()
    opt_1=models.CharField(max_length=400)
    opt_2=models.CharField(max_length=400)
    opt_3=models.CharField(max_length=400)
    opt_4=models.CharField(max_length=400)
    # level=models.CharField(max_length=100)
    time_limit=models.IntegerField()
    right_opt=models.CharField(max_length=400)

    class Meta:
        verbose_name_plural='Questions'

    def __str__(self):
        return self.question
    
