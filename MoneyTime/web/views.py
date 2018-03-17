from django.views.generic import TemplateView
from django.views.generic.list import MultipleObjectMixin


class ReactPage(MultipleObjectMixin, TemplateView):
    """React Page View."""

    object_list = {}
    template_name = 'pages/react.html'
