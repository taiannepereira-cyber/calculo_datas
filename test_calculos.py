from datetime import date, timedelta
from calculos import calcular_idade, dias_ate_data
def test_calcular_idade():
     hoje = date.today()
     nascimento = date(hoje.year -20,hoje.month,hoje.day)
     assert calcular_idade(nascimento)==20      
 
def test_dias_ate_data():
     futuro = date.today() +timedelta(days = 10)
     assert dias_ate_data (futuro)==10
from calculos import dias_passados
def test_dias_passados():
     passado = date.today() - timedelta (days=5)
     assert dias_passados(passado) == 5