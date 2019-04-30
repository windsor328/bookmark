from django.db import models

class Bookmark(models.Model):
    site_name = models.CharField(max_length = 50)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add = True)
    contents = models.TextField(blank=True)

    def __str__(self):
        return "Site name :" + self.site_name +", URL: "+self.url

    
    class Meta:
        ordering = ['site_name']