import os
from django.conf import settings


def get_upload_path(instance, filename):
    return os.path.join(
        settings.MEDIA_ROOT, "/%s/%s" % (instance.form.title, instance.created_by.get_full_name())
    )
