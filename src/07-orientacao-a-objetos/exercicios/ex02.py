""" Exercício 02 - Classe Projeto"""

from classes import projeto

dados_projeto1 = "0123213,VisLab,Latorre"
dados_projeto2 = "1231231,Criação de ChatBot,Vinicius Moura"
dados_projeto3 = "1231231,Jogo VR,Lara Torres"
projeto1 = projeto.Projeto(dados_projeto1)
projeto2 = projeto.Projeto(dados_projeto2)
projeto3 = projeto.Projeto(dados_projeto3)

projetos = [projeto1, projeto2, projeto3]

print(projetos)
print(projetos.count(projeto2))