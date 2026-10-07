from PIL import Image, UnidentifiedImageError
from django.db import models
import uuid
from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.save(self.image.path)
        except (AttributeError, IOError, UnidentifiedImageError) as e:
            logger.error(f"Image Error{self.user.username}:{e}")
            # Handle cases where image file might be missing or corrupted (like default.jpg)


class PendingUser(models.Model):
    username=models.CharField(max_length=150)
    email=models.EmailField()
    password=models.CharField(max_length=128)
    token=models.UUIDField(default=uuid.uuid4,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pending {self.username} ({self.email})"