
from django.db import models

# Create your models here.
    
# models.py 추가
class Accomodation(models.Model):
    roomID = models.TextField()
    room_name = models.TextField()
    city = models.TextField(null=True , blank = True)
    location = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    accomodation_type = models.TextField(null=True , blank = True)
    min_price = models.IntegerField(null=True , blank = True)
    rating = models.FloatField((null=True , blank = True)
    general_review = models.TextField(null=True , blank = True)
    total_review_num = models.IntegerField(null=True , blank = True)
    image_link = models.URLField(null=True)
    img_link_2 = models.URLField(null=True , blank = True)
    img_link_3 = models.URLField(null=True , blank = True)
    img_link_4 = models.URLField(null=True , blank = True)
    img_link_5 = models.URLField(null=True , blank = True)

    def __str__(self):
        return self.room_name

    def update(self, list):
        self.roomID = list[0]
        self.room_name = list[1]
        self.city = list[2]
        self.location = list[3]
        self.latitude = list[4]
        self.longitude = list[5]
        self.accomodation_type = list[6]
        self.min_price = list[7]
        self.rating = list[8]
        self.general_review = list[9]
        self.total_review_num = list[10]
        self.image_link = list[11]
        self.img_link_2 = list[12]
        self.img_link_3 = list[13]
        self.img_link_4 = list[14]
        self.img_link_5 = list[15]