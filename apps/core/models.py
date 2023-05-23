from django.db import models

from core.basemodels import BaseModel
from core.consts import STATUS, PLANNED, FIELD_TYPES, OTHER
from core.utils import get_upload_path


class Form(BaseModel):
    title = models.CharField(max_length=200)
    groups = models.ManyToManyField('user.TgGroup')
    deadline = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS, default=PLANNED)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title


class FormField(BaseModel):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=FIELD_TYPES, default=OTHER)
    forms = models.ManyToManyField('core.Form')

    def __str__(self):
        return self.title


class FieldValue(BaseModel):
    file = models.FileField(upload_to=get_upload_path, null=True)
    string = models.CharField(max_length=400, null=True)
    integer = models.IntegerField(null=True)
    double = models.DecimalField(max_digits=20, decimal_places=6, null=True)
    form_field = models.ForeignKey('core.FormField', models.CASCADE, related_name='values')
    form = models.ForeignKey('core.Form', models.SET_NULL, null=True, related_name='field_values')

    def __str__(self):
        return getattr(self.form_field, 'title', str(self.id))

    class Meta:
        ordering = ('-created_at',)
        indexes = (
            models.Index(fields=('-created_by', '-updated_by'), name='Index by student'),
            models.Index(fields=('form',), name='Index by form'),
            models.Index(fields=('form_field',), name='Index by form field'),
        )
