from django.http import HttpResponseForbidden
import logging

logger = logging.getLogger(__name__)

class AdminRestrictedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            allowed_ips = ['129.205.124.197', '127.0.0.1']
            client_ip = request.META.get('REMOTE_ADDR')
            if client_ip not in allowed_ips:
                logger.info(f"Access denied for IP: {client_ip}")
                return HttpResponseForbidden("Forbidden: You don't have permission to access this resource.")
        return self.get_response(request)
