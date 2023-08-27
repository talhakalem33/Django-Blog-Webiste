from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    summary = RichTextField()
    content = RichTextField()
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True, help_text="Zorunlu değil")
    isactive = models.BooleanField(default=False, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True, blank=True )
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"