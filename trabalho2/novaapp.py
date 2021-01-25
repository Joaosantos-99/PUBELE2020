from flask import Flask, render_template, request, redirect
import requests
import uuid
import shelve
from re import *

app = Flask(__name__)

'''
GET  /relatorios
- devolve uma página html com a lista dos relatórios que vamos enviar para a bd

GET  /relatorios/<id>
- devolve uma página html com informação relativa ao relatório com o identificador = id

POST /relatorios

- permite inserir um relatório na bd e redireciona para a rota /relatorios


Estrutura de um relatorio:

{
    id: number,
    title: string
    subtitle: string
    data:date
    autores: string
    subtitulo0: string
    descrição0: string
   

}

Estrutura da base de dados:

s = {
    id : {
        title: string
        subtitle: string
        data:date
        autores: string
        subtitulo0: string
        descrição0: string
      
    },
    ...
}
'''

@app.route('/')
def index():
    return render_template('indice.html')

@app.route('/autores')
def autores():
    return render_template('autores.html')

@app.route('/procura')
def procura():
    return render_template('procura.html')

@app.route('/relatorios', methods=['GET']) 
def get_relatorios():

    l = []
    
    with shelve.open('relatorios.db') as s:
        for(key,value) in s.items():
            r = {}
            r['id'] = key
            r['title'] = value['title']
            r['subtitle'] = value['subtitle']
            r['data'] = value['data']
            r['autores'] = value['autores']
            r['subtitulo0'] = value['subtitulo0']
            r['descricao0'] = value['descricao0']
            

            l.append(r) 

    
    return render_template('relatorios.html', title='relatorio', relatorios=l)


@app.route('/relatorios', methods=['POST'])
def post_relatorio():

    data = dict(request.form)
    data['autores']=data['autores'].replace('\n','<br>')
    data['descricao0']=data['descricao0'].replace('\n','<br>')
    
    with shelve.open('relatorios.db', writeback = True) as s:
        key = str(uuid.uuid1())
        s[key] = data

    return redirect('http://localhost:5000/relatorios')

@app.route('/procura',methods=['GET'])
def get_palavra():
	r=[]
	palavra=request.form
	with shelve.open('relatorios.db', writeback = True) as s:
		for report, info in s.items():
			s['id']=key
			for key in s:
				if key.find(palavra)!=-1:
					if key not in l:
						r.append(key)

						

	return render_template('procura.html', title='relatorio', relatorios=r)


@app.route('/relatorios/<id_>', methods=['GET'])
def get_relatorios_id(id_):

    with shelve.open('relatorios.db') as s:
        r = s[id_]
        r["id"] = id_

    return render_template('relatorio.html', relatorio=r)

@app.route('/relatorios/<id_>', methods=['POST'])
def post_relatorios_id(id_):
	r =dict(request.form)

	with shelve.open('relatorios.db', writeback = True) as s:
		del(s[id_])

	return redirect('http://localhost:5000/relatorios')


