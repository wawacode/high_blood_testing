'''
代码编写人：
编写时间
修改时间
确认时间
'''
from rest_framework import serializers
from .models import HighBlood
class BloodSerializer(serializers.ModelSerializer):
    class Meta():
        model=HighBlood
        fields="__all__"