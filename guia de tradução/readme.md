1.  Crie uma conta no github.

2.  O primeiro passo para tradução será encontrar o jogo que você quer
    começar, por exemplo, “pack 6”.

![](.//media/image1.png)

3.  Ao entrar na pasta do jogo você provavelmente ira encontrar um
    arquivo Localization.json que será responsavel pelas palavras do
    menu do jogo. E a pasta games que é mais importante, vamos entrar
    nela para esse guia.

![](.//media/image2.png)

4.  Aqui encontramos todos os jogos relacionados a essa versão do jogo,
    vamos escolher o PushTheButton para esse exemplo.

![](.//media/image3.png)

5.  Dentro encontramos 2 arquivos, Localization que novamente está
    responsavel pela tradução de menus na maioria dos casos, e a pasta
    ‘content’ que nesse caso é o local que se encontra o conteudo de
    dentro do jogo.

![](.//media/image4.png)

6.  Nesse exemplo encontramos varios arquivos, cada um responsavel por
    alguma coisa, vamos usar o JokeBoatAnimal.jet para esse exemplo:

![](.//media/image5.png)

7.  Alguns arquivos se encontram em apenas 1 de texto de uma forma que
    fica dificil traduzir, para esse arquivo teremos que realizar alguns
    passos adicionais, caso contrario poderiamos proceguir para os proximos passos.
    Seguimos copiando o conteudo todo usando as teclas Ctrl+A (
    selecionar todo texto) e Ctrl+C, ou podemos dar 2 clicks na linha e
    depois CTRL+C.

![](.//media/image6.png)

8.  Começamos copiando todo conteudo para o site
    <https://jsonformatter.curiousconcept.com> e clicar em process, para
    que ele deixe o arquivo com uma formatação mais agradavel.

![](.//media/image7.png)

9.  Clicamos no icone copiar, para copiar o texto formatado

![](.//media/image8.png)
10.  Voltamos para o github e clicamos no botão editar

![](.//media/image9.png)

11.  Uso o comando Ctrl+A + delete para deletar todo texto, e em seguida
    colo o novo texto formatado no lugar do antigo texto.

![](.//media/image10.png)

12.  Agora com o texto melhor formatado conseguimos realizar a tradução.

![](.//media/image11.png)

13.  Para realizar a tradução basta subistituir as palavras do jogo que
    estão em ingles, e para isso é necessario ter um cuidado inicial
    para entender quais palavras que são relacionadas ao jogo e quais
    são “chaves” do arquivo, normalmente o arquivo está no seguinte
    formato:\
    “chave”:”palavra a ser traduzida”\
    não devemos mecher em nenhuma chave, apenas nas palavras do jogo,
    para ilustrar em vermelho as chaves e palavras que não devem ser
    traduzidas- e em azul a palavra do jogo que foi traduzida.

![](.//media/image12.png)

14.  Após realizar a tradução (perceba que não é necessario traduzir tudo
    de uma vez, você pode fazer isso aos poucos), você pode escrever uma
    descrição do que foi feito e enviar.

![](.//media/image13.png)

15.  Após clicar no botão enviar, você podera ter uma visualização do que
    foi removido, modificado e alterado de acordo com as cores. Em
    sequencia clicamos no botão “Create pull request”

![](.//media/image14.png)

16\. Aqui temos a mesma tela do passo 14, para você colocar informações
do que foi feito.\
clicamos no botão “Create pull request” para enviar a requisição.

![](.//media/image15.png)

17. Pronto, enviamos nossa primeira tradução, agora será preciso esperar
    que a mesma seja aceita e o arquivo original será modificado,
    obrigado!

![](.//media/image16.png)

18. **Caso encontre algum problema favor entrar em contato.**


