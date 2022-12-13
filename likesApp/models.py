from django.db import models

# Create your models here.

class Like(models.Model):
    user = models.ForeignKey('usersApp.User', on_delete=models.CASCADE)
    post = models.ForeignKey('postsApp.Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'likes'
        unique_together = ('user', 'post')