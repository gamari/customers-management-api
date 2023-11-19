import uuid

from django.db import models

class Inquiry(models.Model):
    """お問い合わせ情報"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(verbose_name="会社名", max_length=255)
    phone_number = models.CharField(verbose_name="電話番号", max_length=255)
    pdf_file = models.FileField(verbose_name="何かしらのPDFファイル", upload_to="pdf_file")
    desired_contract_date = models.DateField(verbose_name="契約希望日", null=True, blank=True)