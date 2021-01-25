Introdução

  O intuito deste trabalho é o desenvolvimento de uma pequena API através do framework do Python, Flask. Na API temos algumas funcionalidades como a criação de um relatório, a leitura dos relatórios já criados e também apagar um relatório. De referir que também se tentou desenvolver um método de procura de palavras existentes em relatórios. Porém, não se concluiu essa funcionalidade.

Desenvolvimento

  Em primeiro lugar, criou-se uma rota para a página de índice, onde se encontram botões que nos redirecionam para outras páginas, através das rotas criadas e com os respetivos templates, sendo elas relatórios, autores e procura.
  Tambem se criou uma hiperligação que redireciona para o respetivo github.
  Por forma a ser possível inserir um novo relatório na base de dados, desenvolveu-se uma função para o efeito (post_relatorio) estando esta identificada na linha anterior pela sua rota.
  De forma análoga, implementou-se a função get_relatorio para ser possível obter todos os relatórios já existentes na base de dados.
  Para possiblitar a leitura de um relatório na sua integra, adicionou-se a função get_relatorios_id bem como a rota da mesma. De forma semelhante, para possiblitar a sua eliminação, aplicou-se a função post_relatorio_id. 
  A funçao get_palavra está relacionada com a procura de palvras em relatórios, que infelizmente não ficou concluida.
    De referir que todos os templates criados na pasta templates estão diretamente ligados ao código em Python.
    A pasta static está presente de forma a ser possível a inserção de imagens. Neste caso foram utilizadas na  main page e na página estática de autores.
    
