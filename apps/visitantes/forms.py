from django import forms
from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):

    class Meta:
        model = Visitante
        # alterar para exibir somente os campos permitidos
        fields = [
            "nome_complete", "cpf", "data_nascimento", "numero_casa", "placa_veiculo"
        ]

        error_messages = {
            "nome_complete": {
                "required": "o nome completo do visistante é obrigatório para o registro"
            },
            "cpf": {
                "required": "o CPF do visistante é obrigatório para o registro"
            },
            "data_nascinento": {
                "required": "a data_nascimento do visistante é obrigatório para o registro",
                "invalid": "Informar data com formato valido (DD/MM/YYYY)"
            },

            "numero_casa": {
                "required": "Por favor, informne o numero da casa a ser visitada"
            }
        }


class AutorizaVisitanteForm(forms.ModelForm):

    # para sobrescreve no formulario o atributo morador_responsavel
    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel"
        ]

        error_messages = {
            "morador_responsavel": {
                "requered": "Por favor, informe o nome do morador responsavel por autorizar a entrada"
            }
        }
