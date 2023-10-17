from django.db import models

# TODO 顧客情報
class Customer:
    urikake_list = models.ManyToManyField(Urikake)
