from django.contrib import admin

from core.models import Form, FormField, FieldValue


class FormFieldInline(admin.StackedInline):
    model = FormField
    extra = 0
    fields = ('title', 'type')


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    ...
    # inlines = [FormFieldInline]


@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    ...


@admin.register(FieldValue)
class FieldValueAdmin(admin.ModelAdmin):
    ...
