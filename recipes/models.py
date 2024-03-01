from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание рецепта")
    steps = models.TextField(blank=True, verbose_name="Шаги приготовления рецепта")
    preparation_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to="recipe_images/", default=None,
                              blank=True, null=True, verbose_name="Изображение")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='recipes', null=True,
                               default=None)

    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLISHED, verbose_name="Статус")
    categories = models.ManyToManyField(Category, through='RecipeCategory')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепты"
        verbose_name_plural = "Рецепты"
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
