from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    published_on = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_on=timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey("blog.Post",related_name='comments')
    author=models.CharField(max_length=300)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("post_list")
