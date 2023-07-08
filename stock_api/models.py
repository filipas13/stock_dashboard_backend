from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        return self.symbol

class StockProfile(models.Model):
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField()
    industry = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        return self.stock.symbol

class StockQuote(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='quotes')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    # Add other fields as needed

    def __str__(self):
        return f"{self.stock.symbol} - {self.date}"
