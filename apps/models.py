from django.db.models import Model, CharField
from django_resized import ResizedImageField


class Product(Model):
    image = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='users/images',
                              default='users/default.jpg')
    title = CharField(max_length=255)
    blocks = CharField(max_length=255)

    def __str__(self):
        return self.title
