import pytest
from mixer.backend.django import mixer

from apps.core.models import Profile

pytestmark = pytest.mark.django_db
