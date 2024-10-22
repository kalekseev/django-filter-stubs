from typing import Any
from django.forms import Form

from django_filters import filterset as filterset

FILTER_FOR_DBFIELD_DEFAULTS: Any

class FilterSet(filterset.FilterSet):
    FILTER_DEFAULTS: Any = ...
    @property
    def form(self) -> Form: ...
