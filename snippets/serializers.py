from rest_framework import serializers
from django.contrib.auth import User
from snippets.models import *



class SnippetSerializer(serializers.ModelSerializer):#serializers.Serializer):
    # pk = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    class Meta:
        model = Snippet
        field = ('id', 'title', 'code', 'linenos', 'language', 'style')
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaruKeyRelatedField(many = True, queryset = Snippet.objects.all())
    class Meta:
        model = User
        field = ('id', 'username', 'snippets')


class TestArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestArticle
        field = ('id', 'created', 'title', 'href') 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        

class ConcernDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcernDirection

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News

class SchoolNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolNews