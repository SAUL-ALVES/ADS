from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.descricao

# python manage.py makemigrations
# python manage.py migrate

# CREATE TABLE produtos_produto (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     descricao VARCHAR(100),
#     preco DECIMAL(10,2)
# );