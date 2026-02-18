from django.db import models

from django.db import models
from users.models import User
from wines.models import Wine
from coltns.models import ClientCollection

class WineComment(models.Model): # For clients comments any wine
    """Model to store comments for wines."""
    client = models.ForeignKey(User,
    on_delete=models.CASCADE,
    limit_choices_to={'role':'client'},
    null=True,
    blank=True)

    wine = models.ForeignKey(
        Wine, on_delete=models.CASCADE
    )

    comment = models.TextField(max_length=250)
    comment_date = models.DateTimeField(auto_now_add=True)

class ClientCollectionCommment(models.Model): # For clients comments Other client collections
    """Model to store comments for collections."""
    client = models.ForeignKey(User, on_delete=models.CASCADE,
    limit_choices_to={'role':'client'},
    null=True,
    blank=True)

    clientcollection = models.ForeignKey(
        ClientCollection, on_delete=models.CASCADE,
    )

    comment = models.TextField(max_length=250)
    comment_date = models.DateTimeField(auto_now_add=True)    