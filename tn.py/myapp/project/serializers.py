from rest_framework.serializers import ModelSerializer
from .models import Poll,Option


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = ('id','option', 'qoute_count')

class PollSerializer(ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'question','active', 'options')