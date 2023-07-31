from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default_avatar.png', upload_to='avatars')
  banner = models.ImageField(default='default_banner.png', upload_to='banners')
  status = models.CharField(max_length=50)
  about = models.TextField()

  def __str__(self):
    return f'{self.user.username} profile'