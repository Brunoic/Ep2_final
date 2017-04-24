# -*- coding: utf-8 -*-
import json
import random

with open("inspermons.json","r") as arquivo:
    inspermons=json.load(arquivo)

def sorte():
    x= random.randint(0,100)
    if x in range (0,30):
        return "dobro"
    else:
        return "normal"
        
def batalha(insp_desejado,insp_inimigo,sorte):
    if sorte == "dobro":
        poder = insp_desejado["poder"]*2
    else:
        poder = insp_desejado["poder"]
    minha_vida = insp_desejado["vida"]
    inimigo_vida = insp_inimigo["vida"]
    while minha_vida > 0 and inimigo_vida > 0:
        insp_inimigo["vida"]=insp_inimigo["vida"] - (poder + insp_inimigo["defesa"])
        print ("Ataque! vida do inimigo restante: {0}".format(insp_inimigo["vida"]))
        if insp_inimigo["vida"]<=0:
            return "venceu"
        insp_desejado["vida"]=insp_desejado["vida"] - ( insp_inimigo["poder"] - insp_desejado["defesa"])
        print ("Ataque do adversario , vida restante: {0}".format(insp_desejado["vida"]))
        if insp_desejado["vida"]<=0:
            return "perdeu"
def fugir():
    fuga = random.randint(0,100)
    if fuga in range(0,50):
        return "sucesso"
    else:
        return"falha"
    

horário=int(input("Que horas são? (Somente horas cheias e horário brasileiro)"))
if 1<=horário<=12:
    print("Bom dia! Bem-vindo ao jogo Inspermóns!")
elif 13<=horário<=18:
    print("Boa tarde! Bem-vindo ao jogo Inspermóns!")
else:
    19<=horário<=24
    print("Boa noite! Bem-vindo ao jogo Inspermóns!")

print("Os seguintes inspermóns vem com o jogo: picaxu, xamando e pidijet. Let´s begin!")

insperdéx=[]
inspermons_novos=[{"nome":"mayazard","poder":30,"vida":120,"defesa":9},
                  {"nome":"pterodact","poder":20,"vida":150,"defesa":15},
                  {"nome":"watah","poder":10,"vida":220,"defesa":10},
                  {"nome":"bodzin","poder":15,"vida":90,"defesa":13},
                  {"nome":"machokado","poder":45,"vida":80,"defesa":9},
                  {"nome":"staryme", "poder":25,"vida":160,"defesa":10},
                  {"nome":"Pidgeota","poder":30,"vida":150,"defesa":12},
                  {"nome":"vulpixel","poder":20,"vida":190,"defesa":20},]
print("0 = picaxu, 1 = xamando, 2 = pidijet")        
meu_insp = int(input("Qual inspermón você deseja ser?"))
insp_desejado = inspermons[meu_insp]

while True:
    pergunta=input("Você deseja passear ou dormir,ou ir ao insperdex?")
    if pergunta == "dormir":
        print("Até mais!")
        break
    elif pergunta == "insperdex":
        a = ("você possue os seguintes pokemons {0}".format(insperdéx))
        print(a)
    elif pergunta == "passear":
        print("Enfrente a batalha que está por vir!")
        insp_inimigo=random.choice(inspermons_novos)
        print("Seu inimigo é: {0}".format(insp_inimigo["nome"]))
        decidir = input("Voce deseja fugir?(sim ou nao)")
        if decidir == "sim":
            if fugir == "sucesso":
                print ("Fuga concluida com sucesso")
                break
            else: 
                print("Falha na fuga , voce foi derrotado")
                insp_desejado["vida"]=insp_desejado["vida"] - insp_inimigo["poder"] + insp_desejado["defesa"]
        else:
            resultado = batalha(insp_desejado,insp_inimigo,sorte)
            if resultado == "perdeu":
                print("Você foi derrotado!")
            if resultado == "venceu":
                print("Voce venceu!")
                insperdéx.append(insp_inimigo["nome"])
                print("Seu insperdèx agora contém {0}".format(insperdéx))
                
                
               
                

    
