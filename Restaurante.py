import os

restaurantes = [{'nome':'Praça', 'categoria':'japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'pizza', 'ativo':True}, 
                {'nome':'Cantina', 'categoria':'italiana', 'ativo':False}]

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
      
          """)

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principa '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Altenar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu princiapl
    
    '''
    input('\nDigite uma tecla para voltar ao menu ')

    main()

def opcao_invalida():
     ''' Exibe mensagem de opção inválida e retornar ao menu pricipal
     
     Outputs:
    - Retorna ao menu princiapl

     '''

     print('Opção inválida!\n')

     voltar_ao_menu_principal()

def exibir_subtitulo(texto):
     
     ''' Exibe um subtitulo estilizado na tela
     
     inputs: 
     - texto: str - O texto do subtitulo
     '''
     os.system('cls')
     linha = '*' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()

def cadastrar_novo_restaurante():
     '''Essa função é responsavel por cadastrar um novo restaurante
     
     Inputs:
     - Nome do restaurante 
     - Categoria

     Output:

     - Adiciona um novo restaurante a lista de restaurantes 
     
     '''
     exibir_subtitulo('Cadastro de novos restaurante')
     nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
     categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
     dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
     restaurantes.append(dados_do_restaurante)
     print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')

     voltar_ao_menu_principal()
	
def listar_restaurantes():
     ''' Lista os restaurantes presentes na lista
     
     Outputs: 
     - Exoibe a lista de restaurantes na tela
     -'''
     exibir_subtitulo('Listando restarante')

     print(f'{'Nome do restaurante'.ljust(22)} | {'categoria'.ljust(21)} | {'status'}')
     for restaurante in restaurantes:
         nome_restaurante = restaurante['nome']
         categoria = restaurante['categoria']
         ativo = 'ativado' if restaurante['ativo'] else 'desativo'
         print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)}  | {ativo}')

     voltar_ao_menu_principal()

def alternar_estado_restaurante():
     '''Altera o estado ativo/desativado de um restaurante
     
     Outputs:
     - Exibe a mensagem indicando Sucesso da operação
     '''
     exibir_subtitulo('Alternando estado do restaurante')
     nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
     restaurante_encontrado = False

     for restaurante in restaurantes:
         if nome_restaurante == restaurante['nome']:
             restaurante_encontrado = True
             restaurante['ativo'] = not restaurante['ativo']
             mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativo com sucesso'
             print(mensagem)
     if not restaurante_encontrado:
          print('O restaurante não foi encontrado')

     voltar_ao_menu_principal()

def escolher_opcoes():
    ''' Solicita e executa a opção escolhida pela usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:	
            opçao_escolhida = int(input('Escolha uma opção: '))
            # opcao_escolhida = int(opcao_escolhida)

            if opçao_escolhida == 1: 
                cadastrar_novo_restaurante()
            elif opçao_escolhida == 2: 
                listar_restaurantes()
            elif opçao_escolhida == 3: 
                alternar_estado_restaurante()
            elif opçao_escolhida == 4: 
                finalizar_app()
            else:
                opcao_invalida()
    except: 
     opcao_invalida()
     
def main():
    ''' Função principal que inicia o programa 
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
	main()
   
    