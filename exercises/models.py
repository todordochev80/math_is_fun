from django.db import models



class OperationChoices(models.TextChoices):
    ADD = 'Add', 'Add'
    SUBTRACT = 'Subtract', 'Subtract'
    MULTIPLY = 'Multiply', 'Multiply'
    DIVIDE = 'Divide', 'Divide'


