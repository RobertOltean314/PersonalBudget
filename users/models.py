from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # Define a one-to-one relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Define an image field for the profile picture with a default image and upload directory
    image = models.ImageField(default='default.png', upload_to='IMAGES')

    def __str__(self):
        # Return a string representation of the profile object
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Override the save method to resize the profile image if needed
        super().save(*args, **kwargs)  # Call the parent class's save() method

        # Open the profile image using PIL
        img = Image.open(self.image.path)

        # Resize the image if its height or width exceeds 300 pixels
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)  # Save the resized image
