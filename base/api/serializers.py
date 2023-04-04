from rest_framework import serializers
from .models import Level, ProgrammingLang, Question, Comment, Favourite


class LevelModelSerializer(serializers.ModelSerializer):
    """
    Serializes a Level model instance into JSON-compatible data.
    Attributes:
        Meta: A class that contains metadata about the LevelModelSerializer.
        It specifies the model class to use and the fields to include in the serialized data.
    """
    class Meta:
        model = Level
        fields = ('name', 'short_desc')


class ProgrammingLangModelSerializer(serializers.ModelSerializer):
    """
    Serializes a ProgrammingLang model instance into JSON-compatible data.
    Attributes:
        Meta: A class that contains metadata about the ProgrammingLangModelSerializer.
        It specifies the model class to use and the fields to include in the serialized data.
    """
    class Meta:
        model = ProgrammingLang
        fields = ('name', 'short_desc')

