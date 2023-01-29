from rest_framework.serializers import ModelSerializer
from app.models import Task, Category, Subcategory, User

class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name']

class TaskSerializer(ModelSerializer):
    client = UserSerializer(many=False, read_only=True)
    subcategory = SubcategorySerializer(many=False, read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'created', 'client', 'subcategory', 'description']