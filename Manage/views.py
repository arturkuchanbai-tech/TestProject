# from django.contrib.auth.models import User
# from rest_framework import generics,viewsets
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .models import Category, Tag, Todo, Grade
# from .serializers import CategorySerializer, TagSerializer, TodoSerializer, RegisterSerialiser, GradeSerializer
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerialiser
#     permission_classes = [AllowAny]
# class TodoViewSet(viewsets.ModelViewSet):
#     queryset =Todo.objects.all()
#     serializer_class = TodoSerializer
#     permission_classes =[IsAuthenticated]
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
# class CategoriViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
# class GradeViewSet(viewsets.ModelViewSet):
#     queryset = Grade
#     serializer_class = GradeSerializer

from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import Category,Tag,Todo,SubTask,Comment,Attachment,Grade
from rest_framework import response
# from commongit.permissions import IsAnonimus, IsOvner

User = get_user_model()


from . serializers import(
    CategorySerializer,
    TagSerializer,
    TodoSerializer,
    SubTaskSerializer,
    CommetSerializer,
    AttachmentSerializer,
    GradeSerialiser,
    RegisterSerializer
)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes=[AllowAny]
    serializer_class=RegisterSerializer
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes =[IsAuthenticated]
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
class CommentViewSet(viewsets.ModelViewSet):
    queryset =Comment.objects.all()
    serializer_class = CommetSerializer
class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerialiser





# from rest_framework import viewsets, generics
# from rest_framework.permissions import IsAuthenticated,AllowAny
# from django.contrib.auth.models import User
# from .models import Category
# from .serializers import (
#     CategorySerializer,

# )

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]
#     serializer_class = RegisterSerializer
# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     permission_classes=[IsAuthenticated]
#     serializer_class=TodoSerializer

#     def perform_create(self, serializer):
#         serializer.save(useer = self.request.user)

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# class GradeViewSet(viewsets.ModelViewSet):
#     queryset = Grade.objects.all()
#     serializer_class = GradeSerializer


# class AttachmentViewSet(viewsets.ModelViewSet):
#     queryset = Attachment.objects.all()
#     serializer_class = AttachmentSerializer


# class SubTaskViewSet(viewsets.ModelViewSet):
#     queryset = SubTask.objects.all()
#     serializer_class = SubTaskSerializer







# from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.exceptions import AuthenticationFailed
# from rest_framework import viewsets, generics
# from rest_framework.permissions import AllowAny,IsAuthenticated
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# from .serializers import UserSerializer
# from .models import Todo, Category, Tag, SubTask, Comment,Grade, Attachment
# from .serializers import(
#     TodoSerializer,CategorySerializer,TagSerializer,SubTaskSerializer, CommentSerializer,GradeSerializer,AttachmentSerializer,RegisterSerializer
# )
# user =get_user_model
# class TokenRefreshViewCustom(TokenRefreshView):
#     def post(self, request,*args, **kwargs):
#         refresh_token = request.data.get('refresh')

#         if not refresh_token:
#             return Response({'error':'Pefresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             token=RefreshToken(refresh_token)
#             user_id=token['user_id']
#             user = User.objects.get(id=user_id)
#             if not user.is_active:
#                 raise AuthenticationFailed('User not active, token refresh denided')
#             response =super().post(request, *args, **kwargs)
#             response_data = response.data
#             response_data ['user_status'] = 'active' if user.is_axctive else 'inactive'
#             return Response(response_data, status=status.HTTP_200_OK)
#         except TokenError as e:
#             return Response({'error',str(e)}, status=status.HTTP_401_UNAUTHORIZED)
#         except User.DosNotExist:
#             return Response({'error':'User not fount'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({'error': str(e)},status=status.HTTP_400_BAD_REQUEST)
# class TokenObtainPairViewCustom(TokenObtainPairView):
#     def post(self,request,*args, **kwargs):
#         response=super().post(request,*args,**kwargs)
#         tokens=request.data
#         access_token = tokens.get('assecc')
#         username = response.data.get('username')
#         try:
#             user = User.objects.get(username=username)

#             user_data=UserSerializer(user).data
#         except User.DoesNotExist:
#             return Response({'error':'User Not Fount'},status=status.HTTP_404_NOT_FOUND)
#         user_data=UserSerializer(user).data
#         response_data={
#             'assecc_token':access_token,
#             'refresh_token':tokens.get('refresh'),
#             "user_data":user_data
#         }
#         return Response(response_data, status=status.HTTP_200_OK)
    
# class RegisterView(generics.CreateAPIView):
#     queryset=User.objects.all()
#     serializer_class=RegisterSerializer
#     permission_classes=[AllowAny]
# class TodoViewSet(viewsets.ModelViewSet):
#     queryset=Todo.objects.all()
#     serializer_class=TodoSerializer
#     permission_classes=[IsAuthenticated]
#     def perform_create(self,serializer):
#         serializer.save(user=self.request.user)
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer
# class SubTaskViewSet(viewsets.ModelViewSet):
#     queryset=SubTask.objects.all()
#     serializer_class=SubTaskSerializer
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset=Comment.objects.all()
#     serializer_class=CommentSerializer
# class TagViewSet(viewsets.ModelViewSet):
#     queryset=Tag.objects.all()
#     serializer_class=TagSerializer
# class GradeViewSet(viewsets.ModelViewSet):
#     queryset=Grade.objects.all()
#     serializer_class=GradeSerializer
# class AttachmentViewSet(viewsets.ModelViewSet):
#     queryset=Attachment.objects.all()
#     serializer_class=AttachmentSerializer





# from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError
# from rest_framework.response import Response
# from rest_framework.exceptions import AuthenticationFailed
# from rest_framework import viewsets, generics
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework import status
# from django.contrib.auth import get_user_model
# from .serializers import UserSerializer
# from .models import Todo, Category, Tag, SubTask, Comment, Grade, Attachment
# from .serializers import (
#     TodoSerializer, CategorySerializer, TagSerializer, SubTaskSerializer,
#     CommentSerializer, GradeSerializer, AttachmentSerializer, RegisterSerializer
# )

# User = get_user_model()  # корректно для кастомных моделей пользователей

# # Кастомный refresh view
# class TokenRefreshViewCustom(TokenRefreshView):
#     def post(self, request, *args, **kwargs):
#         refresh_token = request.data.get('refresh')

#         if not refresh_token:
#             return Response({"error": "Refresh token not provided"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             # Создаем объект refresh токена
#             token = RefreshToken(refresh_token)

#             # Получаем пользователя через user_id из токена
#             user_id = token['user_id']
#             user = User.objects.get(id=user_id)

#             # Проверяем, активен ли пользователь
#             if not user.is_active:
#                 raise AuthenticationFailed('User is deactivated, token refresh denied')

#             # Стандартное обновление токена
#             response = super().post# from django.db import models
# from  django.contrib.auth.models import User
# from django.utils import timezone
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name
# class Tag(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name 
    
# class Todo(models.Model):
#     STATUS_CHOICES=[
#         ('new','Новый'),
#         ('progress','В процессе'),
#         ('completed','Завершена'),
#         ('done','Отмена')
#     ]
#     PRIORITY_CHOICES=[
#         ('low','Низкий'),
#         ('medium','Средний'),
#         ('high','Высокий'),
#     ]
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
#     status = models.CharField(choices=STATUS_CHOICES, default='new')
#     priority = models.CharField(choices=PRIORITY_CHOICES, default='medium')
#     tag = models.ManyToManyField(Tag,blank=True)
#     category = models.ForeignKey(Category, on_delete= models.CASCADE, blank=True, null=True)
#     is_importent = models.BooleanField(default=False)
#     completed = models.BooleanField(default=False)
#     du_date = models.DateTimeField(blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     def is_overdue(self):
#         if self.du_date<timezone.now():
#             return True
#         else:
#             return False
#     def __str__(self):
#         return self.title
#     class Meta:
#         ordering = ['-created']
# class SubTask(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE ,related_name='subtasks')
#     title = models.CharField(max_length=255)
#     completed = models.BooleanField(default=False)
#     def __str__(self):
#         return self.title
# class Grade(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='grades')
#     grade = models.IntegerField(default=0)
#     comment = models.CharField(blank=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f'Grade - {self.grade}'
# class Attachment(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='attachments')
#     file = models.FieldFile(upload_to='/attachments/')
#     uploded = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.file.name 

# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# class Category(models.Model):
#     name= models.CharField(max_length=255)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name
# class Tag(models.Model):
#     name = models.CharField(max_length=255)
#     def __str__(self):
#         return self.name
# class Todo(models.Model):
#     STATUS_CHOICES=[
#         ('new','Новая'),
#         ('in progess','В процессе'),
#         ('done','Отмена'),
#         ('cancelled','Завершено'),
#     ]
#     PRIORITY_CHOICES=[
#         ('Low','Низкий'),
#         ('medium','Средний'),
#         ('higt','Высокий'),
#     ]
#     title = models.CharField(max_length=255)
#     description = models.CharField(blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='todos')
#     tags= models.ManyToManyField(Tag, blank=True)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
#     du_date = models.DateTimeField(null=True, blank=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now=True)

#     def is_overd(self):
#         return self.du_date and self.du_date < timezone.now()
#     def __str__(self):
#         return self.title
#     class Meta:
#         ordering = ['-create_at']

# class Grade(models.Model):
#     todo= models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='grades')
#     grade = models.IntegerField(default=0)
#     comment = models.CharField(blank=True)
#     created_at =models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Grade - {self.grade}'






# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name
# class Tag(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
# class Todo(models.Model):
#     STATUS_CHOICES=[
#         ('new','Новая '),
#         ('progress','В процессе'),
#         ('done','Отменена'),
#         ('cancelled','Завершена'),
#     ]
#     PRIORITY_CHOICES=[
#         ('low','Низкий'),
#         ('medium','Средний'),
#         ('high','Высокий'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     status = models.CharField(choices=STATUS_CHOICES,default='new')
#     priority = models.CharField(choices=PRIORITY_CHOICES, default='medium')
#     completed = models.BooleanField(default=False)
#     categori = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
#     tags = models.ManyToManyField(Tag,blank=True)
#     is_importent = models.BooleanField(default=False)
#     due_date = models.DateField(null=True,blank=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     def is_overdue(self):
#         return self.due_date and self.due_date < timezone.now()
#     def __str__(self):
#         return self.title
#     class Meta:
#         ordering = ['-created_at']
# class SubTask(models.Model):
#     toto = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='subtasks')
#     title = models.CharField(max_length=255)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
# class Comment(models.Model):
#     toto = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateField(auto_now_add=True)
#     def __str__(self):
#         return self.text
# class Grade(models.Model):
#     todo= models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='grades')
#     grade = models.IntegerField(default=0)
#     comment = models.CharField(blank=True)
#     created_at =models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Grade - {self.grade}'

# class Attachment(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='attachments')
#     file = models.FileField(upload_to='attachments/')
#     uploaded = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.file.name








# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# # Категории задач
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name
# # Теги
# class Tag(models.Model):
#     name = models.CharField(max_length=255)
#     def __str__(self):
#         return self.name
# # Основная модель задачи
# class Todo(models.Model):
#     STATUS_CHOICES=[
#         ('new','Новая'),
#         ('progress','В процессе'),
#         ('done','Завершена'),
#         ('cancelled','Отменена')
#     ]
#     PRIORITY_CHOICES=[
#         ('low','Низкий'),
#         ('medium','Средний'),
#         ('high','Высокий'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
#     priority=models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
#     completed = models.BooleanField(default=False)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True)
#     tags = models.ManyToManyField(Tag,blank=True)
#     due_date = models.DateTimeField(null=True, blank=True) # срок оплаты
#     is_important = models.BooleanField(default=False) 
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     def is_overdue(self):
#         if self.due_date<timezone.now():
#             return True
#         else:
#             return False
#     def __str__(self):
#         return self.title
#     class Meta:
#         ordering = ['-created_at']
# # Подзадачи
# class SubTask(models.Model):
#     todo = models.ForeignKey(Todo,on_delete=models.CASCADE, related_name='subtasks')
#     title=models.CharField(max_length=255)
#     completed = models.BooleanField(default=False)
#     def __str__(self):
#         return self.title
# # Комментарии
# class Comment(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE,related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text[:20]

# # Оценки
# class Grade(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='grades')
#     grade =models.IntegerField(default=0)
#     comment = models.CharField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f'Grade - {self.grade}'
    
# # Вложения (файлы)
# class Attachment( models.Model):
#     todo = models.ForeignKey(Todo,on_delete=models.CASCADE, related_name='attachments')
#     file = models.FileField(upload_to='attachments/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.file.name
    
# models.py
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# # Категория задачи
# class Category(models.Model):
#     name = models.CharField(max_length=255)  # Название категории
#     description = models.TextField(blank=True)  # Описание категории

#     def __str__(self):
#         return self.name  # Выводит имя категории как строку

# # Теги
# class Tag(models.Model):
#     name = models.CharField(max_length=255)  # Название тега

#     def __str__(self):
#         return self.name  # Выводит имя тега как строку

# # Основная модель задачи (Todo)
# class Todo(models.Model):
#     # Статусы задачи (например, новая, в процессе и т.д.)
#     STATUS_CHOICES = [
#         ('new', 'Новая'),
#         ('progress', 'В процессе'),
#         ('done', 'Завершена'),
#         ('cancelled', 'Отменена')
#     ]
#     # Приоритет задачи
#     PRIORITY_CHOICES = [
#         ('low', 'Низкий'),
#         ('medium', 'Средний'),
#         ('high', 'Высокий'),
#     ]
    
#     # Параметры задачи
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')  # Связь с пользователем
#     title = models.CharField(max_length=255)  # Заголовок задачи
#     description = models.TextField(blank=True)  # Описание задачи
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')  # Статус задачи
#     priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')  # Приоритет задачи
#     completed = models.BooleanField(default=False)  # Выполнена ли задача
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Категория задачи
#     tags = models.ManyToManyField(Tag, blank=True)  # Теги задачи
#     due_date = models.DateTimeField(null=True, blank=True)  # Срок выполнения задачи
#     is_important = models.BooleanField(default=False)  # Флаг важности задачи
#     created_at = models.DateTimeField(auto_now_add=True)  # Дата создания задачи
#     update_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления задачи

#     def is_overdue(self):
#         return self.due_date and self.due_date < timezone.now()  # Проверка, просрочена ли задача

#     def __str__(self):
#         return self.title  # Выводит название задачи как строку

#     class Meta:
#         ordering = ['-created_at']  # Сортировка задач по дате создания (новые сначала)

# # Подзадачи
# class SubTask(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='subtasks')  # Связь с основной задачей
#     title = models.CharField(max_length=255)  # Название подзадачи
#     completed = models.BooleanField(default=False)  # Статус выполнения подзадачи

#     def __str__(self):
#         return self.title  # Выводит название подзадачи как строку

# # Комментарии
# class Comment(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')  # Связь с задачей
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем, который оставил комментарий
#     text = models.TextField()  # Текст комментария
#     created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания комментария

#     def __str__(self):
#         return self.text[:20]  # Выводит первые 20 символов комментария

# # Оценки
# class Grade(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='grades')  # Связь с задачей
#     grade = models.IntegerField(default=0)  # Оценка задачи
#     comment = models.CharField(blank=True, max_length=255)  # Комментарий к оценке
#     created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания оценки

#     def __str__(self):
#         return f'Grade - {self.grade}'  # Выводит строку с оценкой

# # Вложения
# class Attachment(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='attachments')  # Связь с задачей
#     file = models.FileField(upload_to='attachments/')  # Файл вложения
#     uploaded_at = models.DateTimeField(auto_now_add=True)  # Дата и время загрузки файла

#     def __str__(self):
#         return self.file.name  # Выводит имя файла вложения(request, *args, **kwargs)

#             # Добавляем статус пользователя в ответ
#             response_data = response.data
#             response_data['user_status'] = 'active' if user.is_active else 'inactive'

#             return Response(response_data, status=status.HTTP_200_OK)

#         except TokenError as e:
#             return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
#         except User.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# # Кастомный obtain pair view
# class TokenObtainPairViewCustom(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
        
#         tokens = response.data
#         access_token = tokens.get('access')
        
#         username = request.data.get('username')
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         user_data = UserSerializer(user).data
        
#         response_data = {
#             'access_token': access_token,
#             'refresh_token': tokens.get('refresh'),
#             'user_data': user_data
#         }
        
#         return Response(response_data, status=status.HTTP_200_OK)


# # Регистрация пользователей
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]


# # CRUD для задач (Todo)
# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# # CRUD для категорий задач
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# # CRUD для тегов
# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# # CRUD для подзадач
# class SubTaskViewSet(viewsets.ModelViewSet):
#     queryset = SubTask.objects.all()
#     serializer_class = SubTaskSerializer


# # CRUD для комментариев
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# # CRUD для оценок задач
# class GradeViewSet(viewsets.ModelViewSet):
#     queryset = Grade.objects.all()
#     serializer_class = GradeSerializer


# # CRUD для вложений
# class AttachmentViewSet(viewsets.ModelViewSet):
#     queryset = Attachment.objects.all()
#     serializer_class = AttachmentSerializer






# from rest_framework import viewsets, generics
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.contrib.auth.models import User

# from .models import Todo, Category, Tag, SubTask, Comment, Grade, Attachment
# from .serializers import (
#     TodoSerializer,
#     CategorySerializer,
#     TagSerializer,
#     SubTaskSerializer,
#     CommentSerializer,
#     GradeSerializer,
#     AttachmentSerializer,
#     RegisterSerializer
# )


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]


# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# class SubTaskViewSet(viewsets.ModelViewSet):
#     queryset = SubTask.objects.all()
#     serializer_class = SubTaskSerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class GradeViewSet(viewsets.ModelViewSet):
#     queryset = Grade.objects.all()
#     serializer_class = GradeSerializer


# class AttachmentViewSet(viewsets.ModelViewSet):
#     queryset = Attachment.objects.all()
#     serializer_class = AttachmentSerializer





    
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all() #queryset это набор запросов
#     permission_classes = [AllowAny]  #разрешения_классы AllowAny не афторизованные пользователи
#     serializer_class = RegisterSerializer
    
# class TodoViewSet(viewsets.ModelViewSet):

#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated] #разрешения_классы IsAuthenticated афторизованные пользователи

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class CategoryViewSet(viewsets.ModelViewSet):

#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class TagViewSet(viewsets.ModelViewSet):

#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# class SubTaskViewSet(viewsets.ModelViewSet):

#     queryset = SubTask.objects.all()
#     serializer_class = SubTaskSerializer


# class CommentViewSet(viewsets.ModelViewSet):

#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class GradeViewSet(viewsets.ModelViewSet):

#     queryset = Grade.objects.all()
#     serializer_class = GradeSerializer


# class AttachmentViewSet(viewsets.ModelViewSet):

#     queryset = Attachment.objects.all()
#     serializer_class = AttachmentSerializer
