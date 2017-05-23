from django.db import models

# Create your models here.
class user(models.Model):
      name = models.CharField(max_length=200)

class roles(models.Model):
      role = models.CharField(max_length=200)


class permissions(models.Model):
      permission = models.CharField(max_length=200)

class user_roles(models.Model):
      user_id = models.ForeignKey(user, on_delete=models.CASCADE)
      role_id = models.ForeignKey(roles, on_delete=models.CASCADE)

class user_permissions(models.Model):
      role_id = models.ForeignKey(roles, on_delete=models.CASCADE)
      perm_id = models.ForeignKey(permissions, on_delete=models.CASCADE)
