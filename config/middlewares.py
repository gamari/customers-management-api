from django.http import HttpResponseForbidden

from config.settings import ALLOWD_IPS

class IPWhitelistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = ALLOWD_IPS

    def __call__(self, request):
        ip = self.get_client_ip(request)
        
        if "*" in self.allowed_ips:
            """「*」の場合は全てを許可する（検証用）"""
            response = self.get_response(request)
            return response
        
        if ip not in self.allowed_ips:
            return HttpResponseForbidden("IPアドレスが許可されていません")
        response = self.get_response(request)
        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
