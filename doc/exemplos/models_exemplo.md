# TIPOS DE DADOS EXISTENTES NO DJANGO
    Nesse exemplo é utilizado a classe padrão User do Django para exemplificar os relacionamentos.
    
## Classe Exemplo   
    ```py
    from django.db import models
    from django.contrib.auth.models import User

    class OutraClasse(models.Model):
        # Campos da outra classe
        pass

    class Exemplo(models.Model):
        # Campos de texto
        texto_curto = models.CharField(max_length=50)
        texto_longo = models.TextField()

        # Campos numéricos
        inteiro = models.IntegerField()
        decimal = models.DecimalField(max_digits=5, decimal_places=2)
        ponto_flutuante = models.FloatField()

        # Campo booleano
        ativo = models.BooleanField()

        # Campo de data e hora
        data_hora = models.DateTimeField()

        # Campo de data
        data = models.DateField()

        # Campo de hora
        hora = models.TimeField()

        # Campo de escolha
        opcoes = models.CharField(max_length=10, choices=[('A', 'Opção A'), ('B', 'Opção B')])

        # Campo de relacionamento Many-to-One
        relacionamento = models.ForeignKey(OutraClasse, on_delete=models.CASCADE)

        # Campo de relacionamento One-to-One
        outro_relacionamento = models.OneToOneField(User, on_delete=models.CASCADE)

        # Campo de relacionamento Many-to-Many
        muitos_para_muitos = models.ManyToManyField(OutraClasse)

        # Campo de arquivo
        arquivo = models.FileField(upload_to='arquivos/')

        # Campo JSON
        dados_json = models.JSONField()

        # Campo de senha
        senha = models.CharField(max_length=128)

        def __str__(self):
            return self.texto_curto
```