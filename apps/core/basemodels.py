from django.db import models


class BaseModel(models.Model):
    created_by = models.ForeignKey('user.User', models.CASCADE, related_name='+')
    updated_by = models.ForeignKey('user.User', models.CASCADE, related_name='+')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
