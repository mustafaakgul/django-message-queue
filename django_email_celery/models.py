from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelCore(BaseModel):
    core = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)