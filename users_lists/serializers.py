from rest_framework import serializers
from .models import *
from collections import namedtuple
DetailFullInfo = namedtuple('DetailFullInfo', ('detail_info', 'detail_image','detail_3D'))
OrderFullInfo = namedtuple('OrderFullInfo', ('order', 'order_detail','detail'))
#детали
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Detail
        fields=('id','name','author','added_date','project','a2v_id')

#Изображение деталей
class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetailImage
        fields=('detail','image_file')

#3D-модель деталей
class Detail3DSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail3D
        fields = ('detail','model_file')

class FullDetailSerializer(serializers.Serializer):
    detail_info=DetailSerializer(many=True)
    detail_image=ImageModelSerializer(many=True)
    detail_3D=ImageModelSerializer(many=True)


#пользователи
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


#Заказы
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

#Заказы детали
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"


class FullOrderSerializer(serializers.Serializer):
    order=OrderSerializer(many=True)
    order_detail=OrderDetailSerializer(many=True)
    detail=DetailSerializer(many=True)




    #Вместо изображения получаем url изображения
    # def get_photo_url(self, obj):
    #     request=self.context.get('request')
    #     photo_url=obj.image_file.url
    #     return request.build_absolute_url(photo_url)

# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = "__all__"
#         extra_kwargs = {'password': {'write_only': True}}
#
#
#     #Создание нового пользователя
#     # def create(self, validated_data):
#     #     user = Users.objects.create_user(**validated_data)
#     #     return user