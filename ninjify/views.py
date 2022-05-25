from django.core.exceptions import BadRequest
from django.http import HttpResponse
from django.views import View
from django.utils.translation import gettext_lazy as _

from ninjify.models import NinjaName


def _parse_str_to_list(string: str) -> list[str]:
    return string.split(',')


class NinjifyView(View):
    def get(self, request):

        x = request.GET.get('x')

        if not x:
            raise BadRequest(_('Missing (x) parameter'))

        keywords = _parse_str_to_list(x)
        ninja_name = ' '.join(
            NinjaName.objects.filter(
                buzzword__label__in=keywords
            ).values_list('label', flat=True))

        return HttpResponse(ninja_name, content_type="application/json")
