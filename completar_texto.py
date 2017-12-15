# Encoding
# coding: latin-1

# Regras do jogo

# 1. O jogo precisa fornecer três níveis de dificuldade para o usuário.
# 2. O texto precisa ter pelo menos 4 lacunas para serem preenchidas.
# 3. Ao acertar a palavra, o jogo repete a frase com a lacuna preenchida com a resposta correta.
# 4. Ao errar, o jogo solicita que o usuário tente novamente.
# 5. O jogo acaba quando o usuário acertar todas as palavras ou quando o número de tentativas se esgotar.

# O quiz será sobre frases marcantes de cinema. Cada frase será referente à um filme.
# Nos níveis médio e difícil serão perguntados também o nome do ator e do personagem.

# Frases de cada nível do quiz
texto_facil = """A frase "Eu ___1___ gente morta." ficou famosa no filme "O sexto ___2___".
Já a frase "A primeira ___3___ no ___4___ da ___5___ é não falar sobre o ___4___ da ___5___" foi dita no filme "O ___4___ da ___5___".
"""
texto_medio = """A frase "Eu ___1___ gente morta." ficou famosa no filme "O sexto ___2___" e foi dita pelo personagem ___3___.
Já a frase "A primeira ___4___ no ___5___ da ___6___ é não falar sobre o ___5___ da ___6___" foi dita no filme "O ___5___ da ___6___" pelo personagem ___7___.
"""
texto_dificil = """A frase "Eu ___1___ gente morta." ficou famosa no filme "O sexto ___2___" e foi dita pelo personagem ___3___, interpretado por ___4___ ___5___.
Já a frase "A primeira ___6___ no ___7___ da ___8___ é não falar sobre o ___7___ da ___8___" foi dita no filme "O ___7___ da ___8___" pelo personagem ___9___, intepretado por ___10___ ___11___.
"""

# Juntando textos em uma lista
textos = [texto_facil, texto_medio, texto_dificil]

# Respostas
# Facil: 1-Vejo, 2-sentido, 3-regra, 4-clube, 5-luta
# Medio: 1-Vejo, 2-sentido, 3-Cole, 4-regra, 5-clube, 6-luta, 7-Tyler
# Dificil: 1-Vejo, 2-sentido, 3-Cole, 4-Haley, 5- Joel, 6-regra, 7-clube, 8-luta, 9-Tyler, 10-Brad, 11-Pitt

resp_facil = ["vejo","sentido","regra","clube","luta"]
resp_medio = ["vejo","sentido","Cole","regra","clube","luta","Tyler"]
resp_dificil = ["vejo","sentido","Cole","Haley","Joel","regra","clube","luta","Tyler","Brad","Pitt"]

# Juntando respostas em uma lista
respostas = [resp_facil,resp_medio,resp_dificil]

# Definindo os niveis
niveis = ["fácil","médio","difícil"]

# Funcao de definicao do texto dos niveis para informar o usuario as opcoes disponiveis
# Inputs:
#   - niveis: lista de niveis disponiveis para o jogo
# Outputs:
#   - niveis_jogo: texto contendo a lista de niveis separada por virgula
def texto_niveis(niveis):
    niveis_jogo = ""
    for qtd_niveis in niveis:
        niveis_jogo += qtd_niveis + ", "
    if niveis_jogo[-2] == ",":
        niveis_jogo = niveis_jogo[:-2] + "."
    return niveis_jogo

# Solicitando o nivel ao jogador
# Inputs:
#   - niveis: lista de niveis definidos para o quiz
# Outputs:
#   - nivel_usuario: texto do nivel escolhido pelo usuario
def nivel_usuario(niveis):
    # Pergunta ao usuario qual nivel do jogo
    nivel_usuario = raw_input("Os níveis disponíveis são: " + texto_niveis(niveis) + " Escolha um deles: ")
    # Teste para garantir que o jogador escolheu um nivel valido
    while nivel_usuario not in niveis:
        nivel_usuario = raw_input("Os níveis disponíveis são: " + texto_niveis(niveis) + " Escolha um deles: ")
    return nivel_usuario

# Recebe o nível escolhido pelo usuario em texto e retorna o nivel escolhido em numero
# Inputs:
#   - nivel_usuario: niveis escolhido pelo usuario em texto
# Outputs:
#   - nivel_usuario_num: nivel escolhido pelo usuario em numero
def nivel_usuario_num(nivel_usuario):
    # Loop para verificar a posicao do nivel escolhido dentro da lista e retorno do nivel em numero
    n_nivel = 0
    nivel_usuario_num = 0
    while n_nivel < len(niveis):
        if nivel_usuario == niveis[n_nivel]:
            nivel_usuario_num = n_nivel
        n_nivel += 1
    return nivel_usuario_num


# Definindo funcao que verifica se resposta está correta
# Inputs:
#   - palavra: texto da lacuna correspondente à tentativa do usuario
#   - texto: texto do quiz com a lacuna ainda nao preenchida
#   - resposta: lista das respostas corretas para verificar se o usuario acertou
#   - lacunas: numero referente à lacuna que o usuario está respondendo
# Outputs
#   - texto: texto com a lacuna preenchida caso o usuario acerte
# Caso o usuario nao acerte, a funcao perguntara a resposta novamente

def verifica (palavra, texto, resposta, lacunas):
    if palavra in texto:
        # Solicitando resposta do usuario
        troca = raw_input("A palavra " + palavra + "é: ")
        # Loop para solicitar nova resposta em caso de erro
        while troca != resposta[lacunas-1]: # -1 porque o numero de lacunas começa em 1 e o python em 0
            print """
Tente novamente, você errou :/
            """
            print texto
            troca = raw_input("A palavra " + palavra + "é: ")
        # Em caso de acerto, substitui a lacuna, printa o texto com a lacuna preenchida
        texto = texto.replace(palavra, troca)
        print """
Você acertou!! :)
"""
        print texto
    return texto


# Definindo funcao do jogo
# Inputs:
#   - niveis: lista de niveis disponiveis
#   - respostas: lista de respostas disponiveis
#   - textos: lista de textos com lacunas disponiveis
# Mostrará o texto do nivel escolhido e perguntará a resposta da primeira lacuna
# Em caso de acerto, passa para a proxima. Em caso de erro, pede nova tentativa ao usuario
# Output:
#   - Mensagem de parabens por completar o jogo

def jogo(niveis, respostas, textos):

    print """
Bem vindo ao Quiz sobre filmes.

Você consegue de completar as frases corretamente?
    """

    # Definicao de nivel pelo usuario
    nivel_escolhido = nivel_usuario_num(nivel_usuario(niveis))

    # Definicao dos textos de quiz e resposta do nivel selecionado
    resp = respostas[nivel_escolhido]
    texto = textos[nivel_escolhido]

    # Print do texto escolhido pelo usuario
    print """
O jogo começou!

Tente completar as frases abaixo do nível """ + niveis[nivel_escolhido] + """!
    """
    print texto

    # Iniciando contador das lacunas. Esse contador irá até o total de lacunas do nível.
    cont_lacunas = 1
    # Iniciando loop while para perguntar a resposta de cada lacuna
    while cont_lacunas <= len(resp):
        # Definindo o texto de cada lacuna iterativamente
        lacuna = "___"+str(cont_lacunas)+"___"
        # Se encontrar uma lacuna, o programa pede uma resposta e só continua se o jogador acertar
        # Se a lacuna estiver no texto, solicita respota do usuário
        texto = verifica(lacuna,texto,resp,cont_lacunas)
        cont_lacunas += 1
    # Ao acertar tudo, o jogo acaba
    return "Parabéns! Você ganhou!"

print jogo(niveis, respostas, textos)
