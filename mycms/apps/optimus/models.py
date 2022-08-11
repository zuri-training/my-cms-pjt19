from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
class Portfolio(models.Model):
    
    STATUS_CHOICE = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    # DB Fields
    slug = models.SlugField(max_length=300, unique=True, editable=False)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='Portfolio Templates'
    )
    publish = models.DateTimeField(default=timezone.now)

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default="draft"
    )

    class Meta:
        ordering = ("-published",)

    def save(self, *args, **Kwargs):
        self.slug = slugify(self.author)
        super().save(*args, **Kwargs)
        pass

    def __str__(self):
        return self.author