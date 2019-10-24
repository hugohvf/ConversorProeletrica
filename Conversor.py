import re


with open('Dados.txt','r') as file:
    lines = file.read().split("\n")
    linhas = -1
    nome = "global"
    largura = "global"
    comprimento = "global"
    luminaria = "global"
    fluxoluminosouni = "global"
    utilizacao = "global"
    iluminacaonecessaria = "global"
    fatordearea = "global"
    fatordeutilizacao = "global"
    fatordeperdas = "global"
    previousline =  "global"
    l='2'
    s = ";"
    for line in lines:
        if line == "======================================================================":
            linhas+=1
            if linhas == 0:
                with open('Cálculo da Iluminação.csv', 'w') as f:

                    head = ("Ambiente","Largura(m)","Comprimento(m)","Luminária","Fluxo Luminoso Unitário","Classificação","Iluminação Necessária","Fator de Área","Fator de Utilização","Fator de Perdas","Fluxo Total","Número de Luminárias")
                    f.write(s.join(head)+"\n")
            if linhas > 0:
                with open('Cálculo da Iluminação.csv', 'a') as f:
                    e1 = ("=(C" + l + "*B" + l + "*G" + l + ")/(I" + l + "*J" + l + ")")
                    e2 = ("=K" + l + "/E" + l)
                    dados = (nome, largura,
                            comprimento, luminaria,
                            fluxoluminosouni, utilizacao, iluminacaonecessaria,
                            fatordearea, fatordeutilizacao,
                            fatordeperdas,e1,e2)
                    f.write(s.join(dados)+"\n")
                    l= str(int(l)+1)
        if line.split(":")[0] == "AMBIENTE":
            nome = line.split(":")[1][1:]
        if line.split("=")[0] == "Geometria: largura     ":
            largura = re.sub('[a-zA-Z:=" "]','',line)
            largura = re.sub('[.]',',',largura)
        if line.split("=")[0] == "           comprimento ":
            comprimento = re.sub('[a-zA-Z:=" "]', '', line)
            comprimento = re.sub('[.]', ',', comprimento)
        if line.split(":")[0] == "Luminária":
            luminaria = line.split(":")[1][1:]
        if previousline == "Utilização:":
            utilizacao = str(re.sub('[0-9.]','',line))[3:]
        if line.split("=")[0] == "           Fluxo luminoso unitário ":
            fluxoluminosouni = re.sub('[a-zA-Z:=" "á]', '', line)
            fluxoluminosouni = re.sub('[.]', ',', fluxoluminosouni)
        if line.split(":")[0] == "  Iluminação necessária":
            iluminacaonecessaria = re.sub('[a-zA-Z:=" "áçã]', '', line)
            iluminacaonecessaria = re.sub('[.]', ',', iluminacaonecessaria)
        if line.split(":")[0] == "Fator de Área":
            fatordearea = re.sub('[a-zA-Z:=" "Á]', '', line)
            fatordearea = re.sub('[.]',',',fatordearea)
        if line.split(":")[0] == "Fator de Utilização":
            fatordeutilizacao = re.sub('[a-zA-Z:=" "çã]', '', line)
            fatordeutilizacao = re.sub('[.]', ',', fatordeutilizacao)
        if line.split(":")[0] == "Fator de Perdas":
            fatordeperdas = re.sub('[a-zA-Z:=" "]', '', line)
            fatordeperdas = re.sub('[.]', ',', fatordeperdas)
        previousline = line
    print("Dados traduzidos!")

    # Further file processing goes here

''' Fechar arquivo
try:
    #processamento
finally:
    reader.close()
    
'r'	Open for reading (default)
'w'	Open for writing, truncating (overwriting) the file first
'rb' or 'wb'	Open in binary mode (read/write using byte data)
'''