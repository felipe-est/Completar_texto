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

# Respostas
# Facil: 1-Vejo, 2-sentido, 3-regra, 4-clube, 5-luta
# Medio: 1-Vejo, 2-sentido, 3-Cole, 4-regra, 5-clube, 6-luta, 7-Tyler
# Dificil: 1-Vejo, 2-sentido, 3-Cole, 4-Haley, 5- Joel, 6-regra, 7-clube, 8-luta, 9-Tyler, 10-Brad, 11-Pitt

resp_facil = ["vejo","sentido","regra","clube","luta"]
resp_medio = ["vejo","sentido","Cole","regra","clube","luta","Tyler"]
resp_dificil = ["vejo","sentido","Cole","Haley","Joel","regra","clube","luta","Tyler","Brad","Pitt"]

#print texto_facil
#print texto_medio
#print texto_dificil

# Definindo texto inicial do quiz e solicitando o nivel ao jogador

print """Bem vindo ao Quiz sobre filmes.
Você consegue de completar as frases corretamente?"""

nivel = raw_input("Os níveis são facil, medio ou dificil. Escolha um nível: ")

# Teste para garantir que o jogador escolheu um nivel valido
if nivel == "facil":
    print texto_facil
elif nivel == "medio":
    print texto_medio
elif nivel == "dificil":
    print texto_dificil
else:
    print "Escolha entre os niveis facil, medio ou dificil."

# Definindo funcao do jogo

def subst(nivel):
    if nivel == "facil":
        resp=resp_facil
        texto=texto_facil
        texto_split=texto_facil.split()

    if nivel == "medio":
            resp=resp_medio
            texto=texto_medio
            texto_split=texto_medio.split()

    if nivel == "dificil":
            resp=resp_dificil
            texto=texto_dificil
            texto_split=texto_dificil.split()
    # Iniciando contador das lacunas. Esse contador irá até o total de lacunas do nível.
    i = 1
    # Iniciando loop while para perguntar a resposta de cada lacuna
    while i <= len(resp):
        # Definindo o texto de cada lacuna iterativamente
        palavra = "___"+str(i)+"___"
        # Iniciando contador para cada palavra do texto a ser preenchido
        # Se encontrar uma lacuna, o programa pede uma resposta e só continua se o jogador acertar
        p = 0
        # Iniciando loop para cada palavra do texto
        while p < len(texto_split):
            # Se a lacuna estiver no texto, solicita respota do usuário
            if palavra in texto_split[p]:
                # Solicitando resposta do usuario
                troca = raw_input("A palavra " + palavra + "é: ")
                # Loop para solicitar nova resposta em caso de erro
                while troca not in resp[i-1]:
                    print "Tente novamente"
                    print texto
                    troca = raw_input("A palavra " + palavra + "é: ")
                # Em caso de acerto, substitui a lacuna, printa o texto com a lacuna preenchida
                texto = texto.replace(palavra, troca)
                texto_split=texto.split()
                print "Você acertou"
                print texto
            p += 1
        i += 1
    # Ao acertar tudo, o jogo acaba
    return "Parabéns! Você ganhou!"

print subst(nivel)
