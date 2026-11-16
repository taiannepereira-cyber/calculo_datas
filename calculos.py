from datetime import date 

def calcular_idade (data_nascimento):
         hoje = date.today()
         idade = hoje.year - data_nascimento.year
    
         if (hoje.month,hoje.day)< (data_nascimento.month,data_nascimento.day):
                idade -= 1
         
         return idade

def dias_ate_data (data_futura):
         hoje = date.today()
         return(data_futura - hoje).days

def dias_passados(data_passada):
         hoje = date.today()
         return(hoje - data_passada).days