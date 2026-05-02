from .views import CategoryViewSet, TagViewSet, TodoViewSet, SubTaskViewSet, AttachmentViewSet, GradeViewSet, CommentViewSet,RegisterView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'ctegoris', CategoryViewSet)
router.register(r'tags',TagViewSet)
router.register(r'todos', TodoViewSet)
router.register(r'subtasks', SubTaskViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api/v1/register/', RegisterView.as_view(), name='register')
]







# from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# from .views import (CategoryViewSet)
# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)

# urlpatterns = [
#     path('',include(router.urls)),
#     # path('api/register/', RegisterView.as_view(), name='register')
# ]









# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from .views import RegisterView, CategoriViewSet, TagViewSet, TodoViewSet, GradeViewSet

# создаём объект DefaultRouter
# router = DefaultRouter()
# router.register(r'tags', TagViewSet)
# router.register(r'categories', CategoriViewSet)
# router.register(r'todos', TodoViewSet)
# router.register(r'grades', GradeViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api/v1/register/', RegisterView.as_view(), name='register'),  # обычный путь для APIView
# ]


# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from .views import RegisterView,CategoriViewSet,TagViewSet,TodoViewSet,GradeViewSet
# router=DefaultRouter
# router.register(r'register', RegisterView, basename='register')
# router.register(r'tags', TagViewSet)
# router.register(r'categories', CategoriViewSet)
# router.register(r'todos', TodoViewSet)
# router.register(r'grades', GradeViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api/v1/register/', RegisterView.as_view(), name='register')
# ]




# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import(TodoViewSet,CategoryViewSet, TagViewSet,SubTaskViewSet, CommentViewSet,GradeViewSet,AttachmentViewSet,RegisterView)
# router =DefaultRouter()
# router.register(r'todos', TodoViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'tags', TagViewSet)
# router.register(r'subtasks', SubTaskViewSet)
# router.register(r'comments', CommentViewSet)
# router.register(r'grades', GradeViewSet)
# router.register(r'attachments', AttachmentViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
#     path('api/register/',RegisterView.as_view(),name='register'),
# ]




# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TodoViewSet,CategoryViewSet, TagViewSet,SubTaskViewSet,CommentViewSet,GradeViewSet,AttachmentViewSet,RegisterView
# from .views import TokenObtainPairViewCustom,TokenRefreshViewCustom
# router=DefaultRouter()

# router.register(r'categories', CategoryViewSet)
# router.register(r'todos', TodoViewSet)
# router.register(r'tags', TagViewSet)
# router.register(r'subtasks',SubTaskViewSet)
# router.register(r'comments',CommentViewSet)
# router.register(r'grades', GradeViewSet)
# router.register(r'attachments', AttachmentViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('api/register/', RegisterView.as_view(), name='register'),
#     path('api/token/', TokenObtainPairViewCustom.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshViewCustom.as_view(), name='token_refresh'),
# ]



# urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TodoViewSet, CategoryViewSet, TagViewSet, SubTaskViewSet, CommentViewSet, GradeViewSet, AttachmentViewSet, RegisterView
# from .views import TokenObtainPairViewCustom, TokenRefreshViewCustom

# # Создание маршрутизатора
# router = DefaultRouter()
# router.register(r'todos', TodoViewSet)  # Эндпоинт для задач (Todo)
# router.register(r'categories', CategoryViewSet)  # Эндпоинт для категорий (Category)
# router.register(r'tags', TagViewSet)  # Эндпоинт для тегов (Tag)
# router.register(r'subtasks', SubTaskViewSet)  # Эндпоинт для подзадач (SubTask)
# router.register(r'comments', CommentViewSet)  # Эндпоинт для комментариев (Comment)
# router.register(r'grades', GradeViewSet)  # Эндпоинт для оценок (Grade)
# router.register(r'attachments', AttachmentViewSet)  # Эндпоинт для вложений (Attachment)

# urlpatterns = [
#     path('', include(router.urls)),  # Включаем все URL маршруты, определённые в роутере
#     path('api/register/', RegisterView.as_view(), name='register'),  # Эндпоинт для регистрации пользователей
#         # Эндпоинт для получения JWT токенов
#     path('api/token/', TokenObtainPairViewCustom.as_view(), name='token_obtain_pair'),
    
#     # Эндпоинт для обновления JWT токенов
#     path('api/token/refresh/', TokenRefreshViewCustom.as_view(), name='token_refresh'),
# ]