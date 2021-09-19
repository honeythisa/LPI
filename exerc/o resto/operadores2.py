x = "="
print("{}INDICAÇÕES DE FILMES{}".format(x*50,x*50) )
print ('- Ação e Aventura; \n'
       '- Ação e Comédia; \n'
       '- Comédia e Romance; \n'
       '- Drama e Romance; \n'
       '- Drama e Terror; ')
pedido = input('Para receber uma indicação, escolha um dos 2 gêneros de filmes acima, e escreva aqui ->: ')
y = "-"

if pedido == ("Ação e Aventura" or "Aventura e Ação"): print("{}> Resgate".format(y*80) )

if pedido == ("Ação e Comédia" or "Comédia e Ação"): print("{}> Jumanji: Próxima Fase".format(y*80) )

if pedido == ("Comédia e Romance" or "Romance e Comédia"): print("{}> Megarromântico".format(y*80) )

if pedido == ("Drama e Romance" or "Romance e Drama"): print("{}> Como eu era antes de você".format(y*80) )

if pedido == ("Drama e Terror" or "Terror e Drama"): print("{}> Campo do Medo".format(y*80) )

