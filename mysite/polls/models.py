
from django.db import models

# Create your models here.
    
# models.py 추가
class Accomodation(models.Model):
    roomID = models.TextField()
    room_name = models.TextField()
    location = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    accomodation_type = models.TextField(null=True)
    min_price = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    general_review = models.TextField(null=True)
    total_review_num = models.IntegerField(null=True)
    image_link = models.URLField(null=True)
    img_link_2 = models.URLField(null=True)
    img_link_3 = models.URLField(null=True)
    img_link_4 = models.URLField(null=True)
    img_link_5 = models.URLField(null=True)

    def __str__(self):
        return self.room_name

    def update(self, list):
        self.roomID = list[0]
        self.room_name = list[1]
        self.location = list[2]
        self.latitude = list[3]
        self.longitude = list[4]
        self.accomodation_type = list[5]
        self.min_price = list[6]
        self.rating = list[7]
        self.general_review = list[8]
        self.total_review_num = list[9]
        self.image_link = list[10]
        self.img_link_2 = list[11]
        self.img_link_3 = list[12]
        self.img_link_4 = list[13]
        self.img_link_5 = list[14]