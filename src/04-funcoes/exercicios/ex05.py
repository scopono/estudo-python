""" Exercício 05 - IMC"""

def calcular_imc(individuo):
    peso = individuo['peso']
    altura = individuo['altura']
    return peso/(altura * altura)

def obter_classificacao(imc):
    if imc < 18.5:
        return f'Você está abaixo do peso, com IMC de {imc}'
    elif 18.5 <= imc <= 24.9:
        return f'Você está no peso ideal, com IMC de {imc}'
    elif 25.0 <= imc <= 29.9:
        return f'Você está com excesso de peso, com IMC de {imc}'
    elif 30.0 <= imc <= 34.9:
        return f'Você está com obesidade de classe 1, com IMC de {imc}'
    elif 35.0 <= imc <= 39.9:
        return f'Você está com obesidade de classe 2, com IMC de {imc}'
    else:
        return f'Você está com obesidade de classe 3, com IMC de {imc}'

def situacao_individuo(imc):
    peso = individuo['peso']
    if imc < 18.5:
        quilos_ganhar = 18.5 * peso/imc - peso # Calcula quantos pesos deve ganhar através de regra de três
        return f'Você deve ganhar {quilos_ganhar} quilos para chegar no peso ideal.'
    elif 18.5 <= imc <= 24.9:
        return 'Mantenha o seu peso.'
    else:
        quilos_perder = peso - 24.5 * peso/imc # Calcula quantos pesos deve perder através de regra de três
        return f'Você deve perder {quilos_perder} quilos para chegar no peso ideal.'
    
individuo = {
    'peso': 0,
    'altura': 0

}
    
individuo['peso'] = float(input('Insira o seu peso: '))
individuo['altura'] = float(input('Insira a sua altura: '))

imc = calcular_imc(individuo)
classificacao = obter_classificacao(imc)
situacao = situacao_individuo(imc)

print(classificacao)
print(situacao)
                          
