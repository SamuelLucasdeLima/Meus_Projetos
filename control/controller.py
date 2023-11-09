from model.model import EstoqueModel

class EstoqueController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def executar(self):
        self.view.mostrar_menu()
        opcao = self.view.obter_opcao()

        if opcao == 1:
            nome = self.view.obter_nome()
            tipo = self.view.obter_tipo()
            quantidade = self.view.obter_quantidade()
            self.model.registrar_entrada(nome, tipo, quantidade)
            self.view.mostrar_mensagem("Produto inserido com sucesso!")
        elif opcao == 2:
            produtos = self.model.listar_produtos()
            self.view.mostrar_produtos(produtos)
        elif opcao == 4:
            produtos_zerados = self.model.listar_produto_zerado()
            self.view.mostrar_produtos(produtos_zerados)
        elif opcao == 5:
            nome = self.view.obter_nome()
            tipo = self.view.obter_tipo()
            quantidade = self.view.obter_quantidade()
            produto = self.model.obter_produto_por_nome_tipo(nome, tipo)
            if produto:
                if tipo.lower() == 'alimentício' 'alimenticio' :
                    self.view.mostrar_mensagem("Produto alimentício consumido, não pode ser devolvido.")
                elif quantidade <= 0:
                    self.view.mostrar_mensagem("A quantidade de devolução deve ser maior que zero.")
                else:
                    estoque_atual = produto[3]
                    if quantidade > estoque_atual:
                        self.view.mostrar_mensagem("A quantidade de devolução não pode ser maior que a quantidade em estoque.")
                    else:
                        self.model.registrar_devolucao(nome, tipo, quantidade)
                        self.view.mostrar_mensagem("Devolução registrada com sucesso.")
            else:
                self.view.mostrar_mensagem("Produto não encontrado.")
        elif opcao == 6:
            self.listar_produtos_por_categoria()
        elif opcao == 7:
            self.model.fechar_conexao()
            self.view.mostrar_mensagem("Saindo do sistema.")
        elif opcao == 3:
            nome = self.view.obter_nome()
            tipo = self.view.obter_tipo()
            quantidade = self.view.obter_quantidade()
            funcionario = self.view.obter_funcionario()
            if tipo.lower() == 'alimentício' and quantidade < 0:
                self.view.mostrar_mensagem("Produto alimentício consumido, não pode ser devolvido.")
            else:
                self.model.registrar_saida(nome, tipo, quantidade, funcionario)
                self.view.mostrar_mensagem("Saída registrada com sucesso.")
        elif opcao == 8:
            funcionario = self.view.obter_funcionario()
            ferramenta_id = self.view.obter_ferramenta_id()
            self.model.registrar_pegou_ferramenta(funcionario, ferramenta_id)
            self.view.mostrar_mensagem("Registro de quem pegou ferramenta feito com sucesso.")
        else:
            self.view.mostrar_mensagem("Opção inválida. Tente novamente.")

    def listar_produtos_por_categoria(self):
        categoria = self.view.obter_categoria()
        produtos = self.model.listar_produtos_por_categoria(categoria)
        self.view.mostrar_produtos(produtos)
