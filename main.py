quiz = {
    1 : {
        "pergunta" : "Quantas letras tem a palavra Python?",
        "resposta" : "6"
    },
    2 : {
        "pergunta" : "Python é uma raça de qual animal?🐍",
        "resposta" : "cobra"
    },
    3 : {
        "pergunta" : "Python é famoso por suas *********** que podem ser importadas",
        "resposta" : "bibliotecas"
    }
}

pontuacao = 0
for pergunta in quiz:
    resposta = input(quiz[pergunta]['pergunta'] + "\t")
    if resposta == quiz[pergunta]['resposta']:
        print("ACERTOU!")
        pontuacao += 1
    else:
        print("ERROU!")

print("Sua pontuação foi:\t", pontuacao)
