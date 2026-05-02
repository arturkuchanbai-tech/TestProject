# # serializers.py
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Category, Tag, Todo, SubTask, Comment, Grade, Attachment
# from django.contrib.auth.password_validation import validate_password
# from rest_framework.exceptions import ValidationError

# # Сериализатор для регистрации пользователя
# class RegisterSerializer(serializers.ModelSerializer):
#     password_1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])  # Пароль
#     password_2 = serializers.CharField(write_only=True, required=True)  # Повтор пароля

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password_1', 'password_2']

#     def validate(self, attrs):
#         if attrs['password_1'] != attrs['password_2']:  # Проверка на совпадение паролей
#             raise ValidationError({'password': 'Пароли не совпадают'})
#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create(username=validated_data['username'], email=validated_data['email'])  # Создание пользователя
#         user.set_password(validated_data['password_1'])  # Хеширование пароля
#         user.save()
#         return user

# # Сериализаторы для других моделей
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'

# class AttachmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attachment
#         fields = '__all__'

# class SubTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubTask
#         fields = '__all__'

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'

# class GradeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Grade
#         fields = '__all__'

# class TodoSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(read_only=True)  # Имя пользователя, который создал задачу
#     attachments = AttachmentSerializer(many=True, read_only=True)  # Вложения к задаче
#     subtasks = SubTaskSerializer(many=True, read_only=True)  # Подзадачи
#     comments = CommentSerializer(many=True, read_only=True)  # Комментарии
#     grades = GradeSerializer(many=True, read_only=True)  # Оценки задачи
#     tags = TagSerializer(many=True, read_only=True)  # Теги задачи
#     category = CategorySerializer(read_only=True)  # Категория задачи

#     class Meta:
#         model = Todo
#         fields = '__all__'
#         # serializers.py


# class UserSerializer(serializers.ModelSerializer):
#     # Поле для полного имени, которое собирается из first_name и last_name
#     full_name = serializers.CharField(source='get_full_name', read_only=True)
    
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'full_name']



# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
# from rest_framework.exceptions import ValidationError
# from . models import Category, Tag, Todo, Grade
# class RegisterSerialiser(serializers.ModelSerializer):
#     password_1 = serializers.CharField(write_only = True, required =True, validators =[validate_password] )
#     password_2 = serializers.CharField(write_only =True,required = True)
#     class Meta:
#         model =User
#         fields= '__all__'
#     def validate(self, attrs):
#         if attrs['password_1']!=attrs['password_2']:
#             raise ValidationError({'password':'пароли не совпадают'})
#         return attrs
#     def create(self, validate_data):
#         user =User.objects.create(username=validate_data['username'], email=validate_data['email'])
#         user.set_password(validate_data['password_1'])
#         user.save()
#         return user
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','email','username']
# class TodoSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     category = CategorySerializer(read_only=True)
#     tags = TagSerializer(many=True, read_only=True)  

#     class Meta:
#         model = Todo
#         fields = '__all__'
# class GradeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gradefrom rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from .models import Category, Tag, Todo, Comment, SubTask, Attachment, Grade
class RegisterSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(write_only = True, required=True, validators=[validate_password])
    password_2 = serializers.CharField(write_only =True,required=True )
    password_3 = serializers.CharField(write_only =True, required=True)
    class Meta:
        model = User
        fields = ['username','email','password_1','password_2','password_3']
    def validate(self, attrs):
        if attrs['password_1']!=attrs['password_2']!=attrs['password_3']:
            raise ValidationError({'password','пароли не совпадают'})
        return attrs
    def crete(self,validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password_1'])
        user.save()
        return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiields = ['id','email','username']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class CommetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
class GradeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only =True)
    comments = CommetSerializer(many=True, read_only=True)
    subtasks = SubTaskSerializer(many=True, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)
    grades = GradeSerialiser(many=True ,read_only =True)

    category = CategorySerializer(read_only=True)
    tags= TagSerializer(many =True, read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'


# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
# from rest_framework.exceptions import ValidationError
# from .models import Category
# from rest_framework import serializers
# class RegisterSerializer(serializers.ModelSerializer):
#     password_1 = serializers.CharField(write_only =True, required=True,validators =[validate_password])
#     password_2 = serializers.CharField(write_only = True,required=True)
#     class Meta:
#         model =User
#         fields =['username','email','password_1','password_2']
#     def validate(self,attrs):
#         if attrs['password_1']!= attrs['password_2']:
#             raise ValidationError({'password':'пароли не совпадают'})
#         return attrs
#     def create(self, validated_data):
#         user =User.objects.create(username=validated_data['username'],email=validated_data['email'])
#         user.set_password(validated_data['password_1'])
#         user.save()
#         return user
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Category
#         fields = '__all__'
# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields ='__all__'
# class AttachmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attachment
#         fields = '__all__'
# class SubTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubTask
#         fields = '__all__'
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
# class GradeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Grade
#         fields = '__all__'
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','email','username']
# class TodoSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only = True)
#     attachments = AttachmentSerializer(many = True,read_only = True)
#     subtasks = SubTaskSerializer(many = True, read_only = True)
#     comments = CommentSerializer(many =True, read_only=True)
#     grades = GradeSerializer(many =True,read_only = True)

#     tags = TagSerializer(many = True, read_only = True)
#     category = CategorySerializer(read_only=True)

#     class Meta:
#         model = Todo
#         fields = '__all__'









# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
# from rest_framework.exceptions import ValidationError
# from .models import Todo, Grade, Category, Comment, Tag, SubTask, Attachment


# class RegisterSerializer(serializers.ModelSerializer):
#     password_1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password_2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password_1', 'password_2']

#     def validate(self, attrs):
#         if attrs['password_1'] != attrs['password_2']  :
#             raise ValidationError({'password': 'Пароль не совпадает'})
#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
#         user.set_password(validated_data['password_1'])
#         user.save()
#         return user


# class GradeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Grade
#         fields = '__all__'


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'


# class SubTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubTask
#         fields = '__all__'


# class AttachmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attachment
#         fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "email"]


# class TodoSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     subtasks = SubTaskSerializer(many=True, read_only=True)
#     comments = CommentSerializer(many=True, read_only=True)
#     grades = GradeSerializer(many=True, read_only=True)
#     attachment = AttachmentSerializer(many=True, read_only=True)

#     category = CategorySerializer(read_only=True)
#     tags = TagSerializer(many=True, read_only=True)

#     class Meta:
#         model = Todo
#         fields = '__all__'