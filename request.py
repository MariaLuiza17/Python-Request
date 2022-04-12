import requests
import json
import re

requisicao = requests.get("https://g1.globo.com")
print(requisicao)
print(requisicao.json())



'''Consegui usar o REQUEST e o REGEX porém, não consegui fazer a Expressação Regular (regex) ler o conteúdo do site.
Assisti muitas vídeo aulas, porém é um conteúdo bem grande, e não deu pra aprender tudo em 24h, e eu nunca tinha usado essa biblioteca e esses métodos para pegar informações em sites antes, por isso não sei como 'juntar' isso tudo.
Mas aqui está o que eu conseguir aprender e fazer. Vou continuar estudando o assunto e não vou conseguir relaxar até conseguir fazer hahaha.'''