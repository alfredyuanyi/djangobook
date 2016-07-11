from rest_framework import serializers
from openlock.models import *

# class imageserializer(serializers.ModelSerializer):

# 	image = serializers.SerializerMethodField()
# 	def get_image(self, instance):
# 		return instance.image.url if instance.image else ''
# 		pass
# 	class Meta:
# 		model = images
# 		field = ('imageName', 'image')
# 	pass