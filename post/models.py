from math import radians, sin, cos, asin, sqrt

from common.base_model import BaseModel

from django.db import models

from user.models import User


class Post(BaseModel):
    source_latitude = models.FloatField()
    source_longitude = models.FloatField()
    destination_latitude = models.FloatField()
    destination_longitude = models.FloatField()
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def distance_in_km(self) -> float:
        EARTH_RADIUS = 6371.0
        lon1, lat1, lon2, lat2 = map(radians, [
            self.source_longitude,
            self.source_latitude,
            self.destination_longitude,
            self.destination_latitude
        ])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))

        return EARTH_RADIUS * c
