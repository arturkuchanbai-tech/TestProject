# from django.db import models
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



from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Todo(models.Model):
    STATUS_CHOICES=[
        ('new', 'Новый'),
        ('progress','В процессе'),
        ('done', 'Отмена'),
        ('cancelled' ,'Завершено'),
    ]
    PRIORITY_CHOICES=[
        ('low','Низкий'),
        ('medium','Средний'),
        ('high','Высокий'),
    ]
    GRADE_CHOICES = [
    ('1/10', '1/10'),
    ('2/10', '2/10'),
    ('3/10', '3/10'),
    ('4/10', '4/10'),
    ('5/10', '5/10'),
    ('6/10', '6/10'),
    ('7/10', '7/10'),
    ('8/10', '8/10'),
    ('9/10', '9/10'),
    ('10/10', '10/10'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='new')
    priority = models.CharField(choices=PRIORITY_CHOICES, default='medium')
    grade = models.CharField(choices=GRADE_CHOICES, default='1/10')
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    is_importent =models.BooleanField(default=False)
    du_date = models.DateField(null=True, blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    def is_overdue(self):
        return self.du_date and self.du_date < timezone.now()
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
class SubTask(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='todo_comments')
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
class Grade(models.Model):
    GRADE_CHOICES = [
    ('1/10', '1/10'),
    ('2/10', '2/10'),
    ('3/10', '3/10'),
    ('4/10', '4/10'),
    ('5/10', '5/10'),
    ('6/10', '6/10'),
    ('7/10', '7/10'),
    ('8/10', '8/10'),
    ('9/10', '9/10'),
    ('10/10', '10/10'),
    ]
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='grades')
    garade = models.CharField(choices=GRADE_CHOICES, default='1/10')
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f' Grade - {self.garade}, Comment - {self.comment}'
    
class Attachment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attacment/')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
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
#         ('cancelled','Завершено'),
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
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='subtasks')
#     title = models.CharField(max_length=255)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
# class Comment(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
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
#         return self.file.name  # Выводит имя файла вложения