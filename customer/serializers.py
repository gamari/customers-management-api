from rest_framework.serializers import ModelSerializer, ValidationError

from customer.models import Inquiry

class InquirySerializer(ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ["id", "company_name", "phone_number", "pdf_file", "desired_contract_date"]
    
    def validate_pdf_file(self, value):
        # PDFファイルの検証はこちらで行います
        if not value.name.endswith(".pdf"):
            raise ValidationError("PDFファイルのみ受け付けています")
        if value.size > 1024 * 1024:
            raise ValidationError("ファイルサイズは1MBまでです")
        return value