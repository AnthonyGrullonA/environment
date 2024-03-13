# middleware.py

from django.http import HttpResponseForbidden
from .models import CustomUser as User

class ControlAccesoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Suponiendo que el usuario está autenticado y que el modelo User tiene un campo `empresa`.
        if request.user.is_authenticated:
            try:
                usuario = User.objects.get(id=request.user.id)  # Asumiendo que 'request.user' devuelve una instancia del modelo User personalizado.
                request.empresa_usuario = usuario.Empresa
            except User.DoesNotExist:
                return HttpResponseForbidden("Usuario no válido o sin empresa asociada.")
        return None
