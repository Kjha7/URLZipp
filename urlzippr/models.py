from django.db import models
import uuid
from django.contrib.auth.models import User
import hashlib
import base64
# Create your models here.


class UrlModel(models.Model):
    url_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    original_url = models.CharField(max_length=200)
    creation_date = models.DateField()
    # expiration_date = models.DateField()
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hits = models.IntegerField(default=0)
    encrypted_url = models.CharField(max_length=200, null=True, blank=True,unique=True)

    def __str__(self):
        return self.original_url

    def get_encoded(self):
        return int(hashlib.sha1(self.original_url.encode('utf-8')).hexdigest(), 16)

    def get_decoded(self, str_):
        return base64.b16decode(str_)
