from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.

class Parano(models.Model): 
    created_by = models.ForeignKey(
        'Member',
        null=True,
        verbose_name="Créé par",
        related_name="%(app_label)s_%(class)s_creator" #app, class
    )

    modified_by = models.ForeignKey(
        'Member',
        null=True,
        verbose_name="Modifié par",
        related_name="%(app_label)s_%(class)s_modificator" #app, class
    )

    created_at = models.DateTimeField(
        auto_now_add=True, # when we add a date
        verbose_name="Crée le"
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Modifié le"
    )

    class Meta:
        abstract=True
        app_label="todo"

class Setting(Parano,models.Model):
    notify_mail = models.BooleanField(
        verbose_name="Notification par mail",
        default=False,
        blank=True
    )

    notify_sms = models.BooleanField(
        verbose_name="Notification par sms",
        default=False,
        blank=True
    )

class Group(Parano,models.Model):
    settings = models.ForeignKey(
        'Setting',
        null=True,
        blank=True,
        verbose_name="Paramètres",
        related_name="%(app_label)s_%(class)s_setting"
    )

    avatar = models.ImageField(
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=60,
        verbose_name="Nom"
    )

    class Meta:
        app_label="todo"

class Relation(models.Model):
    group = models.ForeignKey(
        'Group',
        null=True,
        blank=True,
        verbose_name="Group",
        related_name="%(app_label)s_%(class)s_group"
    )

    member = models.ForeignKey(
        'Member',
        null=True,
        blank=True,
        verbose_name="Member",
        related_name="%(app_label)s_%(class)s_member"
    )

    class Meta:
        app_label="todo"

class Member(models.Model):
    settings = models.ForeignKey(
        'Setting',
        null=True,
        blank=True,
        verbose_name="Paramètres",
        related_name="%(app_label)s_%(class)s_setting"
  )

    user = models.OneToOneField(
        User,
    )

    avatar = models.ImageField(
        null=True,
        blank=True
    )

    class Meta:
        app_label="todo"
        ordering=["user__date_joined"]

    def __str__(self):
        return str(self.user.username)

class Task(Parano, models.Model):
    status_choices = (
        (None, '---'),
    )
    name = models.CharField(
        max_length=60,
        verbose_name="Nom"
    )

    assigned_to = models.ForeignKey(
        'Member',
        verbose_name="Assigné à",
        related_name="tasks_assigned",
        null=True,
        blank=True
    )

    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )
    due_date = models.DateTimeField(
        verbose_name="Fin prévue le",
        null=True,
        blank=True,
        default=timezone.now() + timedelta(1)
    )
    completed = models.BooleanField(
        verbose_name="Tache terminée ? ",
        default=False,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default=None,
        null=True,
        blank=True
    )
    # list = models.ForeignKey(
    #     Group,
    #     verbose_name="Liste",
    #     related_name="tasks"
    # )

    class Meta:
        app_label = "todo"
        #ordering = ['-created_at'] #on recupere le dernier element

    def __str__(self):
        return str(self.name) #affichage

    def get_absolute_url(self):
        return '/'+str(self.id)+'/'
        #return reverse_lazy('todo:tasks:retrieve', kwargs={'pk': self.id})