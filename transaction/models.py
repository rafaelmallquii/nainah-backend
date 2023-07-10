from django.db import models

# Create your models here.

class Transaction(models.Model):
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    credit_card_last_4 = models.CharField(max_length=4)
    status = models.CharField(max_length=20)
    response_message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Amount: {self.amount}"