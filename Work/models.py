from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey
from django.utils.safestring import mark_safe
from django.forms import ModelForm
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


class Work(models.Model):
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
    work = models.ForeignKey(Work,on_delete=models.CASCADE)
    images = models.ImageField(blank=True, upload_to='image/')

    def __str__(self):
        return self.title
    def image_tag(self):
        if self.images:
            return mark_safe(f'<img src="{self.images.url}" height="50"/>')
        else:
            return
    image_tag.short_description = 'images'

class Basvuru(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    referans = models.TextField(max_length=200)
    cv = models.FileField(blank=True, upload_to='images/')
    firmaHakkindaDusunduklerin = models.CharField (blank=True, max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.referans

class BasvuruForm(ModelForm):
    class Meta:
        model = Basvuru
        fields = ['referans','work','status']


class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    product = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    subject = models.CharField(max_length=50)
    comment = models.TextField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment']