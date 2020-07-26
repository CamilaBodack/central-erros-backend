from django.db import models
from django.core.validators import MinLengthValidator


class User(models.Model):
    username = models.CharField("Nome", max_length=50)
    email = models.EmailField("Email")
    password = models.CharField("Senha", max_length=50, validators=[MinLengthValidator])
    last_login = models.DateTimeField("Último login", auto_now=True)

    def __str__(self):
        return self.username


class Agent(models.Model):
    name = models.CharField("Nome", max_length=50)
    status = models.BooleanField("Status", default=True)
    env = models.CharField("Ambiente", max_length=20)
    version = models.CharField("Versão", max_length=5)
    address = models.GenericIPAddressField("Ipv4", protocol="IPv4")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField("Nome", max_length=50)

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id
