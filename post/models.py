from django.db import models


class Post(models.Model):
    pass

    def __str__(self) -> str:
        return super().__str__()

class Comment(models.Model):
    pass

    def __str__(self) -> str:
        return super().__str__()

class Reaction(models.Model):
    pass

    def __str__(self) -> str:
        return super().__str__()

