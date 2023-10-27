from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from customer.models import Inquiry
from customer.serializers import InquirySerializer


class InquiryCreateAPIView(CreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

# TODO 複雑な仕様の場合APIViewを利用することを推奨します（下記）
# class InquiryCreateAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = InquirySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)