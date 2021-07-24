from django.db import models


class Porteiro(models.Model):

    usuario = models.OneToOneField(
        "usuarios.Usuario",
        verbose_name="Usuário",
        on_delete=models.CASCADE
    )

    nome_completo = models.CharField(
        verbose_name="Nome Completo", max_length=194,
    )

    CPF = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name="telefone de contato",
        max_length=11,
        blank=True
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
    )

    class Meta:

        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"

    def __str__(self):
        return self.nome_completo
