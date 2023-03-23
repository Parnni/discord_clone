from base.models import Room
from django.forms import ModelForm


class RoomForm(ModelForm):
    """Form for creating rooms."""

    class Meta:
        model = Room
        fields = "__all__"
