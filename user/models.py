from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

roles = {
    ('AM', 'Administrador'),
    ('EP', 'Empleado'),
}


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(default='EP', max_length=2, choices=roles)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.user.username}) | Rol: {self.role}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        role = 'EP'
        if instance.is_superuser and instance.is_staff:
            role = 'AM'
        Staff.objects.create(user=instance, role=role)
