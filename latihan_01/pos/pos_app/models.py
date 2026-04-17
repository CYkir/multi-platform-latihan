from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TableResto(models.Model):
    status_choices = (
        ('Aktif', 'Aktif'),
        ('Tidak Aktif', 'Tidak Aktif'),
    )
    
    status_table_choices = (
        ('Kosong', 'Kosong'),
        ('Terisi', 'Terisi'),
    )
    
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)
    table_status = models.CharField(max_length=15, choices=status_table_choices, default='Kosong')
    status = models.CharField(max_length=15, choices=status_choices, default='Aktif')
    # user_created = models.CharField(max_length=100, blank=True, null=True)
    # user_updated = models.CharField(max_length=100, blank=True, null=True)
    user_created = models.ForeignKey(User, related_name='user_created_table_resto', blank=True, null=True, on_delete=models.SET_NULL)
    user_updated = models.ForeignKey(User, related_name='user_updated_table_resto', blank=True, null=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
