manifestacoes = ['1#Guilherme#Reclamação#pouca luz#corredores com luzes fracas','2#Neymar#Sugestão#ter uma iluminação melhor#Seria bom se tivesse um iluminação melhor','3#Segundo#Elogio#Obrigado#area externa muito bonita']
opcao = 0
comprimentoLinha = 65
linha = '-' * comprimentoLinha
print('Bem vindo à Ouvidoria ABC!'.center(comprimentoLinha))
while opcao >= 1 or opcao <= 7:
 print(linha)
 print('MENU'.center(comprimentoLinha))
 print(linha)
 print('[1] Listar manifestações')
 print('[2] Listar sugestões')
 print('[3] Listar reclamações')
 print('[4] Listar elogios')
 print('[5] Nova manifestação')
 print('[6] Buscar manifestação por número de protocolo')
 print('[7] Sair')
 print(linha)
 opcao = int(input('Digite o número correspondente à opção desejada: '))
 print(linha)
 if opcao == 1:
   print('MANIFESTAÇÕES'.center(comprimentoLinha))
   print(linha)
   for manifestacao in manifestacoes:
     infos = manifestacao.split('#')
     print('Protocolo',infos[0])
     print('Nome: ',infos[1])
     print('Tipo: ',infos[2])
     print('Título: ',infos[3])
     print('Descrição: ',infos[4])
     print(linha)
 elif opcao == 2:
   print('SUGESTÕES'.center(comprimentoLinha))
   print(linha)
   for manifestacao in manifestacoes:
     infos = manifestacao.split('#')
     tipo  = infos[2]
     if tipo == 'Sugestão':
       print('Protocolo',infos[0])
       print('Nome: ',infos[1])
       print('Título: ',infos[3])
       print('Descrição: ',infos[4])
       print(linha)
 elif opcao == 3:
   print('RECLAMAÇÕES'.center(comprimentoLinha))
   print(linha)
   for manifestacao in manifestacoes:
     infos = manifestacao.split('#')
     tipo  = infos[2]
     if tipo == 'Reclamação':
       print('Protocolo',infos[0])
       print('Nome: ',infos[1])
       print('Título: ',infos[3])
       print('Descrição: ',infos[4])
       print(linha)
 elif opcao == 4:
   print('ELOGIOS'.center(comprimentoLinha))
   print(linha)
   for manifestacao in manifestacoes:
     infos = manifestacao.split('#')
     tipo  = infos[2]
     if tipo == 'Elogio':
       print('Protocolo',infos[0])
       print('Nome: ',infos[1])
       print('Título: ',infos[3])
       print('Descrição: ',infos[4])
       print(linha)
 elif opcao == 5:
   print('NOVA MANIFESTAÇÃO'.center(comprimentoLinha))
   print(linha)
   protocolo = len(manifestacoes) + 1
   opcaoTipo = 0
   tipo = ""
   nome = input('Digite seu nome: ')
   print('1) Sugestão 2) Reclamação 3) Elogio')
   while opcaoTipo <1 or opcaoTipo >3:
     opcaoTipo = int(input('Digite o número equivalente ao tipo de manifestação: '))
     if opcaoTipo == 1:
       tipo = "Sugestão"
     elif opcaoTipo == 2:
       tipo = "Reclamação"
     else:
       tipo = "Elogio"
   titulo = input('Digite o título da sua manifestação: ')
   descricao = input('Digite a descrição da sua manifestação: ')
   manifestacoes.append(str(protocolo) + '#'+nome+'#'+tipo+'#'+titulo+'#'+descricao)
 elif opcao == 6:
   print('Buscar manifestações por protocolo'.center(comprimentoLinha))
   print(linha)
   numProtocolo = int(input('Digite o número do protocolo: '))
   if numProtocolo > len(manifestacoes):
     print(linha)
     print('PROTOCOLO NÃO ENCONTRADO!'.center(comprimentoLinha))
   else:
    print(linha)
    infos = manifestacoes[numProtocolo - 1].split('#')
    print('Protocolo',infos[0])
    print('Nome: ',infos[1])
    print('Tipo: ',infos[2])
    print('Título: ',infos[3])
    print('Descrição: ',infos[4])
    print(linha)
 elif opcao == 7:
   print('Obrigado por utilizar o sistema de Ouvidoria!'.center(comprimentoLinha))
   break
 else:
   print('ENTRADA INVÁLIDA!'.center(comprimentoLinha))