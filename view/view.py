class EstoqueView:
    def mostrar_menu(self):
        print("===== Sistema de Gerenciamento de Estoque =====")
        print("1. Inserir Produto")
        print("2. Listar Produtos")
        print("3. Registrar Saída de Produto")
        print("4. Listar Produtos com Estoque Zerado")
        print("5. Registrar Devolução de Produto")
        print("6. Listar Produtos por Categoria")
        print("7. Sair")

    def obter_opcao(self):
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            return 0

    def obter_nome(self):
        return input("Nome do produto: ")

    def obter_tipo(self):
        return input("Tipo do produto: ")

    def obter_quantidade(self):
        try:
            quantidade = int(input("Quantidade do produto: "))
            return quantidade
        except ValueError:
            return 0

    def obter_funcionario(self):
        return input("Nome do funcionário: ")

    def obter_categoria(self):
        return input("Categoria a ser listada: ")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_produtos(self, produtos):
        if produtos:
            print("ID | Nome | Tipo | Quantidade")
            for produto in produtos:
                print(f"{produto[0]} | {produto[1]} | {produto[2]} | {produto[3]}")
        else:
            print("Nenhum produto encontrado.")
