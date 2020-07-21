from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)
        )


class Course(models.Model):
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Atalho")
    description = models.TextField("Descrição Simples", blank=True)
    about = models.TextField("Sobre o curso", blank=True)
    start_date = models.DateField("Data de Início", null=True, blank=True)
    image = models.ImageField(
        "Imagem", upload_to="courses/images", null=True, blank=True
    )
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("courses:details", args=[self.slug])

    class Meta:
        verbose_name = "curso"
        ordering = ["name"]


class Enrollment(models.Model):
    STATUS_CHOICES = ((0, "Pendete"), (1, "Aprovado"), (2, "Cancelado"))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Usuário",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    course = models.ForeignKey(
        Course,
        verbose_name=("Curso"),
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    status = models.IntegerField(
        "Situação", choices=STATUS_CHOICES, default=1, blank=True
    )
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1

    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"
        unique_together = ("user", "course")


class Announcement(models.Model):
    course = models.ForeignKey(Course, verbose_name="Curso", on_delete=models.CASCADE)
    title = models.CharField("Título", max_length=100)
    content = models.TextField("Conteúdo")
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    def __str__(self):
        self.title

    class Meta:
        verbose_name = "Anúncio"
        verbose_name_plural = "Anúncios"
        ordering = ["-created_at"]


class Comment(models.Model):
    announcement = models.ForeignKey(
        Announcement,
        verbose_name="Anúncio",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Usuário", on_delete=models.CASCADE
    )
    content = models.TextField("Comentário")
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
        ordering = ["created_at"]
