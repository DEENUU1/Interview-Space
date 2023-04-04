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


class QuestionModelSerializer(serializers.ModelSerializer):
    """
    Serializes a Question model instance into JSON-compatible data.
    Attributes:
        Meta: A class that contains metadata about the QuestionModelSerializer.
        It specifies the model class to use and the fields to include in the serialized data.
    """
    class Meta:
        model = Question
        fields = ('name', 'content', 'content_code', 'date_create', 'programming_lang', 'level', 'author')


class CommentModelSerializer(serializers.ModelSerializer):
    """
    Serializes a Comment model instance into JSON-compatible data.
    Attributes:
        Meta: A class that contains metadata about the CommentModelSerializer.
        It specifies the model class to use and the fields to include in the serialized data.
    """
    class Meta:
        model = Comment
        fields = ('name', 'content', 'content_code', 'date_create', 'question', 'author')

