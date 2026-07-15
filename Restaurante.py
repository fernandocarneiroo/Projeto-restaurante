import os
import sys

restaurantes = [
    {'nome': 'Praça', 'categoria': 'japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'italiana', 'ativo': False},
]


def exibir_nome_do_programa():
    '''Exibe o nome estilizado do programa na tela.'''
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
    '''Exibe as opções disponíveis no menu principal.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    '''Exibe mensagem de finalização do aplicativo e encerra o programa.'''
    exibir_subtitulo('Finalizar App')
    print('Obrigado por usar o sistema de restaurantes!')
    sys.exit(0)


def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar ao menu principal.'''
    input('\nDigite uma tecla para voltar ao menu: ')


def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna ao menu principal.'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''Exibe um subtítulo estilizado na tela.'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Cadastra um novo restaurante na lista.'''
    exibir_subtitulo('Cadastro de novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ').strip()
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ').strip()

    if not nome_do_restaurante or not categoria:
        print('Nome e categoria são obrigatórios. Tente novamente.\n')
        voltar_ao_menu_principal()
        return

    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False,
    }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    '''Lista os restaurantes presentes na lista.'''
    exibir_subtitulo('Listando restaurantes')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}")
    print('-' * 55)

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Altera o estado ativo/desativado de um restaurante.'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ').strip()
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso'
                if restaurante['ativo']
                else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            )
            print(mensagem)
            break

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()


def escolher_opcoes():
    '''Solicita e executa a opção escolhida pelo usuário.'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    except ValueError:
        opcao_invalida()
        return

    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        alternar_estado_restaurante()
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        opcao_invalida()


def main():
    '''Função principal que inicia o programa.'''
    while True:
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcoes()


if __name__ == '__main__':
    main()
    