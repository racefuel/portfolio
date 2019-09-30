from django.db import models

# Create blog model (title, publication date, blog text/body, image-optional)
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    def shortened(self):
        return self.body[:160]

    def cust_pub_date(self):
        return self.pub_date.strftime("%b %e, %Y")
