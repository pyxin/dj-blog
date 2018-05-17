from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = timezone.now()
        self.modified_time = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['-created_time']  # 默认排序


# class Author(models.Model):
#     name = models.CharField(max_length=20)
#
#
# class Publisher(models.Model):
#     name = models.CharField(max_length=20)
#
#
# class Book(models.Model):
#     name = models.CharField(max_length=20)
    # pub = models.ForeignKey(Publisher)
    # authors = models.ManyToManyField(Author)
