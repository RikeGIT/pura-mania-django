from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nome

class Complemento(models.Model):
    nome = models.CharField(max_length=100)
    adicional = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.nome} (+R${self.adicional})"

class Prato(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='pratos/', blank=True, null=True)
    disponivel = models.BooleanField(default=True)
    complementos = models.ManyToManyField(Complemento, blank=True, related_name='pratos')
    tags = models.ManyToManyField(Tag, blank=True, related_name='pratos')

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    complementos = models.ManyToManyField(Complemento, blank=True)

    def get_preco_total(self):
        total = self.prato.preco
        total += sum(c.adicional for c in self.complementos.all())
        return total * self.quantidade
