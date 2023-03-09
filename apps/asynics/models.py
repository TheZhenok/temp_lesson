from django.db import models


# EXAMPLE
# {
#   "radio_id":107458,
#   "radio_name":"No Politics Radio",
#   "radio_image":"https:\/\/visitdpstudio.net\/radio_world\/upload\/85917184-2022-03-21.png",
#   "radio_url":"http:\/\/s2.radio.co\/sa843f32da\/listen",
#   "genre":"Hip Hop",
#   "country_name":"USA(America)",
#   "country_id":26
# }

class Station(models.Model):
    """Station model."""

    radio_id: int = models.IntegerField(
        verbose_name='радио айди'
    )
    radio_name: str = models.CharField(
        verbose_name='название радио',
        max_length=30,
        unique=True
    )
    radio_image: str = models.CharField(
        verbose_name='картинка радио',
        max_length=50
    )
    radio_url: str = models.URLField(
        verbose_name='юрл радио',
    )
    genre: str = models.CharField(
        verbose_name='жанр',
        max_length=30
    )
    country_name: str = models.CharField(
        verbose_name='название страны',
        max_length=65
    )
    country_id: int = models.IntegerField(
        verbose_name='айди страны'
    )

