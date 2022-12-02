from django.db import models

# Create your models here.

# Create a model for the post categories 
class PostCategory(models.Model):
    category_name = models.CharField(max_length = 150, verbose_name = 'Category name')
    category_description = models.TextField(verbose_name = 'Description', blank = True, null = True)
    def __str__(self):
        return self.category_name


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# create a model to post on blog 
class BlogPost(models.Model):
    post_title = models.CharField(max_length =150)
    post_category = models.ForeignKey(PostCategory, on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    post_contents = models.TextField()
    class Meta:
        ordering  = ['-created_date']
    def __str__(self):
        return self.post_title

