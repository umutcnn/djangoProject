from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from ckeditor_uploader.fields import RichTextUploadingField
class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=400)
    keywords = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

'''def get_absolute_url(self):
    return reverse('category_works', kwargs={'slug': self.slug})
'''


class work(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #category tablosu ile ilişkilendirme
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=300)
    keywords = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    wage = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    gmail = models.CharField(max_length=200)
    parent = ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    facebook = models.CharField (blank=True, max_length=55)
    twitter = models.CharField (blank=True, max_length=55)
    linkedin = models.CharField (blank=True, max_length=55)

    def __str__(self):
        return self.title
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return
    image_tag.short_description = 'image'

class Images(models.Model):
    title = models.CharField(max_length=50, blank=True)
    work = models.ForeignKey(work,on_delete=models.CASCADE)
    images = models.ImageField(blank=True, upload_to='image/')

    def __str__(self):
        return self.title
    def image_tag(self):
        if self.images:
            return mark_safe(f'<img src="{self.images.url}" height="50"/>')
        else:
            return
    image_tag.short_description = 'images'
class BasvuruYap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work = models.ForeignKey(work,on_delete=models.CASCADE)
    email = models.CharField(blank=True, max_length=15)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    job = models.CharField (blank=True, max_length=150)
    firmaHakkindaDusunduklerin = models.CharField (blank=True, max_length=150)
    deneyim = models.CharField (blank=True, max_length=55)
    referans = models.CharField (blank=True, max_length=55)
    cv = models.FileField(blank=True, upload_to='images/')

