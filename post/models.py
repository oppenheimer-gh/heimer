from math import radians, sin, cos, asin, sqrt

from common.base_model import BaseModel

from django.db import models

from user.models import User, Mentor


class Post(BaseModel):
    source_latitude = models.FloatField()
    source_longitude = models.FloatField()
    source_country = models.CharField(max_length=255, null=True, blank=True)
    destination_latitude = models.FloatField()
    destination_longitude = models.FloatField()
    destination_country = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    comments_count = models.IntegerField(default=0)

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

    @property
    def available_mentors(self):
        if self.user.is_mentor:
            return Mentor.objects.none()

        users = User.objects.filter(is_mentor=True)

        matching_both = Mentor.objects.filter(
            user__in=users,
            is_available=True,
            user__posts__source_country=self.source_country,
            user__posts__destination_country=self.destination_country
        )

        matching_destination_only = Mentor.objects.filter(
            user__in=users,
            is_available=True,
            user__posts__destination_country=self.destination_country
        ).exclude(
            id__in=matching_both.values_list('id', flat=True)
        )

        return matching_both.union(matching_destination_only)


    def __str__(self):
        return f"{self.message[:64]} (author: {self.user.username})"
