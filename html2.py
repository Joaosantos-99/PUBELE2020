from re import *
import jinja2  as j2
from bs4 import BeautifulSoup

def TEMPLATE2(info):
    template = j2.Template("""
<!DOCTYPE html>
<html>
    <head>
        <title> {{title}} </title>   
        <meta charset="utf-8"/>

    </head>
    <body>
    	<center><img src="UM.png" alt="logo UM" width=180 height=120></center>
        <h1><center> {{subtitle0}}</center> </h1>
        <p> <center>{{date}}</center> </p>
        <h2><center>Autores</center></h2>
        
        <ul>
            <center> {% for el in team %}
                 <p>{{el['name']}} : {{el['number']}}</p>
                {% endfor %}</center> 

           
        </ul>
        <ul>
            {% for el in substitles %}
                <h2>{{el['subtitle']}}</h2>
                <p>{{el['description']}}</p>
                {% endfor %}
        </ul>
    </body>

</html>
""")
    return(template.render(info))

def TEMPLATE3(info):
    template = j2.Template("""
<!DOCTYPE html>
<html>
    <head>
        <title> ÍNDICE </title>   
        <meta charset="utf-8"/>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>
    <body>
    <br><br>
        <center><img src="UM.png" alt="logo UM" width=180 height=120></center>
        <br><br>
        <br><br>
        <center><h1>ÍNDICE</h1></center>
        <br><br>
        <hr>
        
        {% for t in title %}

        <center><p><a href="html{{title.index(t)+1}}.html" title="Go to tp{{title.index(t)+1}}" target="blank">{{t}}</a></p></center>
        {% endfor %}

        <center><p><a href="SDVGSDGFSDDF" title="Go to codigo" target="blank">Visit github</a></p></center>

        {% for t in hashtags %}

        <center><a href="html{{hashtags.index(t)+1}}.html" title="Go to tp{{hashtags.index(t)+1}}" target="blank">{{t}}</a></center>
        {% endfor %}



        
    </body>

</html>
""")
    return(template.render(info))

def extraihashtag(report):

    a = BeautifulSoup(report,"xml")
    for el in a.find_all("hashtags"):
        return el.text

def extraititle(report):

    a = BeautifulSoup(report,"xml")
    for el in a.find_all("title"):
        return el.text

def extraireport():
    l = []
    f = refile('xml1.xml') #abre o ficheiro xml
    soup= BeautifulSoup(f, "xml")  # "abre-o" com o beautifulsoup
    lista_reports= soup.find_all("report") #retorna uma lista que os divide na palavra "report"
    return lista_reports

def extract2():

    with open("xml1.xml") as f:
        report=f.read() 

    info = []

    for tag,miolo in findall(r'<(.*?)>(.*?)</\1>',report):
        info.append((tag,miolo))


    print(info)


def refile(filename): # devolve texto

    with open(filename) as f:
        report=f.read()

    return report 



def extract_dict(L,report):
# recebe uma lista com tags e devolve um dicionario com o que está dentro dessas tags
    infoDict={}
    for el in L:
        v=search(rf'<{el}(.*?)>((?:.|\n)*?)</{el}>',report)
        # |\n é para incluir o newline na procura e ?: é para dizer que os parentesis no (?:.|\n) não sao para
        #   atribuir a um grupo, sao apenas para indicar prioridade
        if v:
            infoDict[el]=v[2]
    return infoDict

def extrai_listaH(xml,tag): #apenas recorre a esta função para tirar o conteudo das subtags

    info = []

    for miolo in findall(rf'<{tag}(.*?)>((?:.|\n)*?)</{tag}>',xml): #retorna uma lista de strings com o conteudo das tags
        info.append(miolo)

    return info


def dtd():
    with open('report.dtd') as f:
        content=f.read()
    l=[]
    for tag in findall('<!ELEMENT +(\w+)',content):  #findall vai apanhar os caracteres devido ao \w até ao espaço e exceto o que está fora dos parenteses
        
        l.append(tag)
    return(l)

def main():

    lista_reports=extraireport()
    i=1
    lista=dtd()
    t={'title':[], 'hashtags': []}
    for report in lista_reports:
        
        report = str(report)
         
        report = sub('[\n\t]*', '', report)    
        dic = extract_dict(lista,report)  #fornecer a lista da funcao dtd com as tags 
        aux = extrai_listaH(dic['team'],'element')
        aux1 = extrai_listaH(dic['substitles'],'sub')
        dic['team'] = [extract_dict(['name','number'],str(el)) for el in aux]
        dic['substitles'] = [extract_dict(['subtitle','description'],str(el)) for el in aux1]
        t['title'].append(extraititle(report))
        t['hashtags'].append(extraihashtag(report))
        with open(f'html{i}.html', 'w') as f:
            f.write(TEMPLATE2(dic))
        i=i+1

        with open (f'index.html', 'w') as file:
            file.write(TEMPLATE3(t))

main()
   