from django.db import models


class AliveModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = models.Manager()
    alive_objects = AliveModelManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()
