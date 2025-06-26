import customtkinter as ctk
import funcoes
from CTkMessagebox import CTkMessagebox
import funçõespdf 
#precisa fazer o pip do customtkinter e o ctkmessagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk): 
    def __init__(self): 
        super().__init__() 
        self.title("Sistema de Estoque - Loja Arcanjo") 
        self.geometry("800x700") 
        self.tela_menu_inicial() 

    def tela_menu_inicial(self):
        for itens in self.winfo_children():
            itens.destroy()

        # Cria um quadro centralizado com cantos arredondados
        janela = ctk.CTkFrame(self, corner_radius=15)
        janela.pack(pady=50, padx=50, fill="both", expand=True)

        # Título do sistema
        ctk.CTkLabel(
                    janela,
                    text="Loja Arcanjo",
                    font=("Helvetica", 26, "bold")
                    ).pack(pady=(30, 10))

        ctk.CTkLabel(
                    janela,
                    text="Menu Principal",
                    font=("Helvetica", 18)
                    ).pack(pady=(0, 30))
    

        ctk.CTkButton(janela, 
                      text="Cadastrar produto", 
                      command=self.abrir_tela_cadastro, 
                      width=220, 
                      height=30, 
                      font=("Helvetica", 14)).pack(pady=10)
        ctk.CTkButton(janela, 
                      text= "Cadastrar Serviço", 
                      command=self.abrir_tela_cadastroserviço, 
                      width=220, 
                      height=30, 
                      font=("Helvetica", 14)).pack(pady=10)
        ctk.CTkButton(janela, 
                      text= "Pesquisar produto", 
                      command=self.abrir_tela_de_pesquisa, 
                      width=220, 
                      height=30, 
                      font=("Helvetica", 14)).pack(pady=10)
        ctk.CTkButton(janela, 
                      text= "Adicionar produto", 
                      command=self.abrir_tela_adicionar_produto, 
                      width=220, 
                      height=30, 
                      font=("Helvetica", 14)).pack(pady=10)
        ctk.CTkButton(janela, 
                      text= "Retirar produto", 
                      command=self.abrir_tela_remover_produto, 
                      width=220, 
                      height=30, 
                      font=("Helvetica", 14)).pack(pady=10)
        ctk.CTkButton(janela,
                      text="Remover produto",
                      command=self.abrir_tela_removerprod_cadastrado,
                      width=220,
                      height=30,
                      font=("Helvetica", 14)).pack(pady=10)
        ctk.CTkButton(janela,
                      text="Remover serviço",
                      command= self.abrir_tela_removerserv_cadastrado,
                      width=220,
                      height=30,
                      font=("Helvetica", 14)).pack(pady=10)
        ctk.CTkButton(janela, #Tem que ter 2 pra poder salvar antes e mostrar dps, pq so mostra o que existir
                    text="Abrir PDF",
                    command=funçõespdf.abrirPDF,
                    width=220,
                    height=30,
                    font=("Helvetica", 14)).pack(pady=(10))
        ctk.CTkButton(janela,
                    text="Iniciar Análise",
                    command=self.botao_salvar_data,
                    width=220,
                    height=30,
                    font=("Helvetica", 14)).pack(pady=(10))


    def abrir_tela_cadastro(self):
        for item in self.winfo_children():
            item.destroy()

        janela = ctk.CTkFrame(self, corner_radius=15) #Cria um CTkFrame, que é tipo uma “caixinha” onde os campos vão ficar dentro, deixa as bordas arredondadas.
        janela.pack(pady=40, padx=40, fill="both", expand=True)
        #pady=40 → espaço em cima e embaixo,
        #padx=40 → espaço à esquerda e à direita,
        #fill="both" → o frame pode crescer em largura e altura,
        #expand=True → faz ele ocupar o centro da janela.
        ctk.CTkLabel(janela, text="Cadastrar Produto", font=("Helvetica", 20, "bold")).pack(pady=15)
        #width=300 define a largura da caixa.
        #pack(pady=8) adiciona espaço entre os campos.
        self.nome_entrada = ctk.CTkEntry(janela, placeholder_text="Nome do Produto", width=300)
        self.nome_entrada.pack(pady=8)

        self.valor_entrada = ctk.CTkEntry(janela, placeholder_text="Valor", width=300)
        self.valor_entrada.pack(pady=8)

        self.estoque_entrada = ctk.CTkEntry(janela, placeholder_text="Estoque", width=300)
        self.estoque_entrada.pack(pady=8)

        self.codigo_entrada = ctk.CTkEntry(janela, placeholder_text="Código", width=300)
        self.codigo_entrada.pack(pady=8)

        self.valororiginal_entrada = ctk.CTkEntry(janela, placeholder_text="Valor Original", width=300)
        self.valororiginal_entrada.pack(pady=8)

        self.msg_erro = ctk.CTkLabel(janela, text="", text_color="red", font=("Helvetica", 12))
        self.msg_erro.pack(pady=5)


        def cadastrar():
            nome = self.nome_entrada.get()
            valor = self.valor_entrada.get()
            estoque = self.estoque_entrada.get()
            codigo = self.codigo_entrada.get()
            valor_original = self.valororiginal_entrada.get()

            self.msg_erro.configure(text="")  # limpa p sempre mostrar só o erro atual

            if not (nome and valor and estoque and codigo and valor_original):
                self.msg_erro.configure(text="Preencha todos os campos!")
                return

            try:
                valor = float(valor)
                estoque = int(estoque)
                codigo = int(codigo)
                valor_original = float(valor_original)

            except ValueError:
                self.msg_erro.configure(text="Valor, estoque, código e o valor original devem ser números.")
                return

            resultado = funcoes.CadastrarProdutos(nome, valor, estoque, codigo, valor_original)
            if resultado == "existe":
                CTkMessagebox(title="Aviso", message="Produto já existe!", icon="warning")
            else:
                CTkMessagebox(title="Sucesso", message="Produto cadastrado com sucesso!", icon="check")
                self.nome_entrada.delete(0, ctk.END)
                self.valor_entrada.delete(0, ctk.END)
                self.estoque_entrada.delete(0, ctk.END)
                self.codigo_entrada.delete(0, ctk.END)
                self.valororiginal_entrada.delete(0, ctk.END)

        alinharbtn = ctk.CTkFrame(janela, fg_color="transparent")
        alinharbtn.pack(pady=15)

        ctk.CTkButton(alinharbtn, text="Cadastrar", command=cadastrar, width=140).pack(side="left", padx=10)
        ctk.CTkButton(alinharbtn, text="Voltar ao Menu", command=self.tela_menu_inicial, width=140).pack(side="left", padx=10)

    def abrir_tela_cadastroserviço(self):
        for itens in self.winfo_children(): 
            itens.destroy() 

        janela = ctk.CTkFrame(self, corner_radius=15) 
        janela.pack(pady=70, padx=70, fill="both", expand=True)

        ctk.CTkLabel(janela, text="Cadastrar Serviço", font=("Helvetica", 20, "bold")).pack(pady=15)
        self.serviço_entrada = ctk.CTkEntry(janela, placeholder_text= "Nome do serviço", width=300)
        self.serviço_entrada.pack(pady=8)

        self.valor_serviço_entrada = ctk.CTkEntry(janela, placeholder_text= "Valor", width=300 )
        self.valor_serviço_entrada.pack(pady=8)

        self.codigo_serviço_entrada = ctk.CTkEntry(janela, placeholder_text= "Código", width=300)
        self.codigo_serviço_entrada.pack(pady=8)

        self.msg_erro = ctk.CTkLabel(janela, text="", text_color="red", font=("Helvetica", 12))
        self.msg_erro.pack(pady=3)
        
        def cadastrarserv():
            serviço = self.serviço_entrada.get()
            valor_serviço = self.valor_serviço_entrada.get()
            codigo_serviço = self.codigo_serviço_entrada.get()

            self.msg_erro.configure(text="")  # limpa p sempre mostrar só o erro atual

            if not(serviço and valor_serviço and codigo_serviço):
                self.msg_erro.configure(text="Preencha todos os campos!")
                return
            
            try:
                valor_serviço= float(valor_serviço)
                codigo_serviço= int(codigo_serviço)
            except ValueError:
                self.msg_erro.configure(text="Valor e codigo devem ser números!")
                return 
            resultadosev = funcoes.CadastrarServiço(serviço, valor_serviço, codigo_serviço)
            if resultadosev == "existe":
                CTkMessagebox(title="Aviso", message="Serviço já existe!", icon="warning")
            else: #resultado é o return de "sucesso"
                CTkMessagebox(title="Sucesso", message="Serviço Cadastrado!", icon="check")
                self.serviço_entrada.delete(0, ctk.END)
                self.valor_serviço_entrada.delete(0, ctk.END)
                self.codigo_serviço_entrada.delete(0, ctk.END)

        alinharbtn = ctk.CTkFrame(janela, fg_color="transparent")
        alinharbtn.pack(pady=15)

        ctk.CTkButton(alinharbtn, text="Cadastrar", command=cadastrarserv).pack(side="left", padx=10)
        ctk.CTkButton(alinharbtn, text="Voltar ao Menu", command=self.tela_menu_inicial).pack(side="left", padx=10)

    def abrir_tela_de_pesquisa(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        janela = ctk.CTkFrame(self, corner_radius=15) 
        janela.pack(pady=130, padx=130, fill="both", expand=True)

        ctk.CTkLabel(janela, text="Pesquisa de produtos", font=("Helvetica", 20, "bold")).pack(pady=15)
        self.codigo_entrada = ctk.CTkEntry(janela, placeholder_text="Código do produto", width=300)
        self.codigo_entrada.pack(pady=8)

        self.msg_erro = ctk.CTkLabel(janela, text="", text_color="red", font=("Helvetica", 12))
        self.msg_erro.pack(pady=5)

        def pesquisar():
            codigo = self.codigo_entrada.get()

            self.msg_erro.configure(text="")

            if not codigo:
                self.msg_erro.configure(text="Preencha todos os campos!")
                return

            if not codigo.isdigit():
                self.msg_erro.configure(text="O codigo deve ser números!")
                return
            codigo = int(codigo)

            resultadopesq = funcoes.PesquisaDeProdutos(codigo) #retorna uma tupla com os dados do produto se encontrar, ou None se não encontrar.

            if resultadopesq: #resultado não é None ou vazio
                nome, valor, estoque, _, valor_original, _ = resultadopesq
                CTkMessagebox(
                title="Produto Encontrado!",
                message=f"Nome: {nome}\nValor: R$ {valor:.2f}\nEstoque: {estoque}\nValor original: {valor_original}",
                icon="check"
                )
                self.codigo_entrada.delete(0, ctk.END)
            else:
                CTkMessagebox(title="Erro", message="Produto não encontrado", icon="cancel")

        alinharbtn = ctk.CTkFrame(janela, fg_color="transparent")
        alinharbtn.pack(pady=15)
        
        ctk.CTkButton(alinharbtn, text="Pesquisar produto", command=pesquisar).pack(side="left", padx=10)
        ctk.CTkButton(alinharbtn, text="Voltar ao menu", command=self.tela_menu_inicial).pack(side="left", padx=10)

    def abrir_tela_adicionar_produto(self):
        for widget in self.winfo_children():
            widget.destroy()

        janela = ctk.CTkFrame(self, corner_radius=15) 
        janela.pack(pady=100, padx=100, fill="both", expand=True)
        
        ctk.CTkLabel(janela, text= "Adicionar produtos", font=("Helvetica", 20, "bold")).pack(pady=15)
        self.codigoprod_entrada = ctk.CTkEntry(janela, placeholder_text="Código do produto",  width=300)
        self.codigoprod_entrada.pack(pady=8)

        self.quantidade_entrada = ctk.CTkEntry(janela, placeholder_text="Quantidade a Adicionar",  width=300)
        self.quantidade_entrada.pack(pady=8)

        self.msg_erro = ctk.CTkLabel(janela, text="", text_color="red", font=("Helvetica", 12))
        self.msg_erro.pack(pady=5)


        def adicionar_estoque():
            codigo = self.codigoprod_entrada.get()
            quantidade = self.quantidade_entrada.get()

            self.msg_erro.configure(text="")
    
            if not (codigo and quantidade):
                self.msg_erro.configure(text="Preencha todos os campos!")
                return

            if not (codigo.isdigit() and quantidade.isdigit()):
                self.msg_erro.configure(text="O codigo e a quantidade devem ser números!")
                return
            
            codigo = int(codigo)
            quantidade = int(quantidade)
            resultado_adc_prod = funcoes.AdicionarProdutoAoEstoque(codigo, quantidade)
            if resultado_adc_prod is not None:
                nome, valor, estoque,_, novo_estoque = resultado_adc_prod
                CTkMessagebox(
                title="Produto Adicionado!",
                message=f"Nome: {nome}\nValor: R$ {valor}\nEstoque anterior: {estoque}\nEstoque atual: {novo_estoque}",
                icon="check"
                )
                self.codigoprod_entrada.delete(0, ctk.END)
                self.quantidade_entrada.delete(0, ctk.END)
            else:
                CTkMessagebox(title="Erro", 
                              message="Produto não encontrado!\nAdicione-o ou digite novamente o código",
                              icon="cancel"
                              )
                self.codigoprod_entrada.delete(0, ctk.END)
                self.quantidade_entrada.delete(0, ctk.END)


        alinharbtn = ctk.CTkFrame(janela, fg_color="transparent")
        alinharbtn.pack(pady=15)

        ctk.CTkButton(alinharbtn, text="Adicionar Estoque", command=adicionar_estoque).pack(side="left", padx=10)
        ctk.CTkButton(alinharbtn, text="Voltar ao Menu", command=self.tela_menu_inicial).pack(side="left", padx=10)

    def abrir_tela_remover_produto(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        janela = ctk.CTkFrame(self, corner_radius=15) 
        janela.pack(pady=70, padx=70, fill="both", expand=True)

        ctk.CTkLabel(janela, text= "Remover produtos", font=("Helvetica", 20, "bold")).pack(pady=15)
        self.codigoproduto_entrada = ctk.CTkEntry(janela, placeholder_text="Código do produto", width=300)
        self.codigoproduto_entrada.pack(pady=8)

        self.quantidaderemov_entrada = ctk.CTkEntry(janela, placeholder_text="Quantidade a retirar", width=300)
        self.quantidaderemov_entrada.pack(pady=8)

        self.msg_erro = ctk.CTkLabel(janela, text="", text_color="red", font=("Helvetica", 12))
        self.msg_erro.pack(pady=5)

        def remover_estoque():
            codigo = self.codigoproduto_entrada.get()
            quantidade = self.quantidaderemov_entrada.get()

            self.msg_erro.configure(text="")

            if not (codigo and quantidade):
                self.msg_erro.configure(text="Preencha todos os campos!")
                return

            if not (codigo.isdigit() and quantidade.isdigit()):
                self.msg_erro.configure(text="O codigo e a quantidade devem ser números!")
                return
            
            codigo = int(codigo)
            quantidade = int(quantidade)
            resultado_remov_produto = funcoes.RemoverProdutoAoEstoque(codigo, quantidade)

            if resultado_remov_produto is None:
                CTkMessagebox(title="Erro", 
                              message="Produto não encontrado!\nAdicione-o ou digite novamente o código",
                              icon="cancel"
                              )
                self.codigoproduto_entrada.delete(0, ctk.END)
                self.quantidaderemov_entrada.delete(0, ctk.END)
            else:
                if resultado_remov_produto == "quantidade_maior":
                    CTkMessagebox(title="Erro", 
                                  message="Quantidade maior que o estoque disponível!", 
                                  icon="cancel")
                    self.codigoproduto_entrada.delete(0, ctk.END)
                    self.quantidaderemov_entrada.delete(0, ctk.END)
                    
                else:
                    nome, valor, estoque_antigo, _, estoque_novo = resultado_remov_produto
                    CTkMessagebox(title="Produto removido!",
                                message=f"Nome: {nome}\nValor: R$ {valor}\nEstoque anterior: {estoque_antigo}\nEstoque atual: {estoque_novo}",
                                icon="check"
                                )
                    self.codigoproduto_entrada.delete(0, ctk.END)
                    self.quantidaderemov_entrada.delete(0, ctk.END)

        alinharbtn = ctk.CTkFrame(janela, fg_color="transparent")
        alinharbtn.pack(pady=15)

        ctk.CTkButton(alinharbtn, text="Remover Estoque", command=remover_estoque).pack(side="left", padx=10)
        ctk.CTkButton(alinharbtn, text="Voltar ao Menu", command=self.tela_menu_inicial).pack(side="left", padx=10)
        

    def abrir_tela_removerprod_cadastrado(self):
        for item in self.winfo_children():
            item.destroy()

        janela = ctk.CTkFrame(self, corner_radius=15) 
        janela.pack(pady=50, padx=50, fill="both", expand=True)

        ctk.CTkLabel(janela, text="Remover cadastro", font=("Helvetica", 20, "bold")).pack(pady=15)
        self.codigoprod_entrada = ctk.CTkEntry(janela, placeholder_text="Código do produto", width=300)
        self.codigoprod_entrada.pack(pady=8)

        self.msg_erro = ctk.CTkLabel(janela, text="", text_color="red", font=("Helvetica", 12))
        self.msg_erro.pack(pady=5)

        def remover_cadastroprod():
            codigo_produto = self.codigoprod_entrada.get()

            self.msg_erro.configure(text="")

            if not (codigo_produto):
                self.msg_erro.configure(text="Preencha todos os campos!")
                return

            if not (codigo_produto.isdigit()):
                self.msg_erro.configure(text="O código deve ser um número!")
                return


            codigo_produto = int(codigo_produto)
            resultadoremovcadastro_prod = funcoes.RemoverCadastroProduto(codigo_produto)

            if resultadoremovcadastro_prod is None:
                 CTkMessagebox(title="Erro", 
                              message="Produto não encontrado!\nAdicione-o ou digite novamente o código",
                              icon="cancel"
                              )
                 self.codigoprod_entrada.delete(0, ctk.END)
                
            else: 
                nome, valor, _,_ = resultadoremovcadastro_prod
                CTkMessagebox(title="Produto removido!",
                                message=f"Nome: {nome}\nValor: R$ {valor}",
                                icon="check"
                                )
                self.codigoprod_entrada.delete(0, ctk.END) 
        
        alinharbtn = ctk.CTkFrame(janela, fg_color="transparent")
        alinharbtn.pack(pady=15)

        ctk.CTkButton(alinharbtn, text="Remover produto", command=remover_cadastroprod).pack(side="left", padx=10)
        ctk.CTkButton(alinharbtn, text="Voltar ao Menu", command=self.tela_menu_inicial).pack(side="left", padx=10)

    def abrir_tela_removerserv_cadastrado(self):
        for item in self.winfo_children():
            item.destroy()

        janela = ctk.CTkFrame(self, corner_radius=15) 
        janela.pack(pady=50, padx=50, fill="both", expand=True)

        ctk.CTkLabel(janela, text="Remover cadastro", font=("Helvetica", 20, "bold")).pack(pady=15)
        self.codigoserv_entrada = ctk.CTkEntry(janela, placeholder_text="Código do serviço", width=300)
        self.codigoserv_entrada.pack(pady=8)

        self.msg_erro = ctk.CTkLabel(janela, text="", text_color="red", font=("Helvetica", 12))
        self.msg_erro.pack(pady=5)

        def remover_cadastroserv():
            codigo_serviço = self.codigoserv_entrada.get()

            self.msg_erro.configure(text="")

            if not (codigo_serviço):
                self.msg_erro.configure(text="Preencha todos os campos!")
                return

            if not (codigo_serviço.isdigit()):
                self.msg_erro.configure(text="O código deve ser um número!")
                return


            codigo_serviço = int(codigo_serviço)
            resultadoremovcadastro_serv = funcoes.RemoverCadastroserviço(codigo_serviço)

            if resultadoremovcadastro_serv is None:
                 CTkMessagebox(title="Erro", 
                              message="Produto não encontrado!\nAdicione-o ou digite novamente o código",
                              icon="cancel"
                              )
                 self.codigoserv_entrada.delete(0, ctk.END)
                
            else: 
                nome, valor, _ = resultadoremovcadastro_serv
                CTkMessagebox(title="Produto removido!",
                                message=f"Nome: {nome}\nValor: R$ {valor}",
                                icon="check"
                                )
                self.codigoserv_entrada.delete(0, ctk.END) 
        
        alinharbtn = ctk.CTkFrame(janela, fg_color="transparent")
        alinharbtn.pack(pady=15)

        ctk.CTkButton(alinharbtn, text="Remover serviço", command=remover_cadastroserv).pack(side="left", padx=10)
        ctk.CTkButton(alinharbtn, text="Voltar ao Menu", command=self.tela_menu_inicial).pack(side="left", padx=10)

    def botao_salvar_data(self):
        for item in self.winfo_children():
            item.destroy()

        janela = ctk.CTkFrame(self, corner_radius=15)
        janela.pack(pady=70, padx=70, fill="both", expand=True)

        ctk.CTkLabel(janela, text="Iniciar Análise", font=("Helvetica", 20, "bold")).pack(pady=15)

        ctk.CTkLabel(janela, text="Digite a data de início (ddmmaaaa):", font=("Helvetica", 14)).pack(pady=10)

        self.entrada_data = ctk.CTkEntry(janela, placeholder_text="Ex: 24062025", width=300)
        self.entrada_data.pack(pady=10)

        self.despesasfixas_entrada = ctk.CTkEntry(janela, placeholder_text="Despesas fixas", width=300)
        self.despesasfixas_entrada.pack(pady=10)

        self.despesasvariaveis_entrada = ctk.CTkEntry(janela, placeholder_text="Despesas variaveis", width=300)
        self.despesasvariaveis_entrada.pack(pady=10)

        self.msg_erro = ctk.CTkLabel(janela, text="", text_color="red", font=("Helvetica", 12))
        self.msg_erro.pack(pady=5)

        def salvar_data():
            data_str = self.entrada_data.get()
            despesasfixas = self.despesasfixas_entrada.get()
            despesasvariaveis = self.despesasvariaveis_entrada.get()
            
            self.msg_erro.configure(text="")  # limpa erro anterior

            if len(data_str) != 8 or not data_str.isdigit():
                self.msg_erro.configure(text="Data inválida. Use o formato ddmmaaaa.")
                return

            if not despesasfixas or not despesasvariaveis:
                self.msg_erro.configure(text="Preencha os campos de despesas!")
                return

            try:
                despesasfixas = float(despesasfixas.replace(",", ".")) 
                despesasvariaveis = float(despesasvariaveis.replace(",", "."))

                data_convertida = funçõespdf.dataForma1(int(data_str))
                self.data_inicio_analise = data_convertida

                # Salva os dados no banco de dados
                funçõespdf.salvarDados(data_convertida, despesasfixas, despesasvariaveis)

                CTkMessagebox(
                    title="Sucesso",
                    message=f"Data e despesas salvas!\nData: {data_str[:2]}/{data_str[2:4]}/{data_str[4:]}\nFixas: R$ {despesasfixas:.2f}\nVariáveis: R$ {despesasvariaveis:.2f}",
                    icon="check"
        )

                self.entrada_data.delete(0, ctk.END)
                self.despesasfixas_entrada.delete(0, ctk.END)
                self.despesasvariaveis_entrada.delete(0, ctk.END)

            except ValueError:
                self.msg_erro.configure(text="As despesas devem ser números válidos (ex: 1200.50)")
            except Exception as e:
                self.msg_erro.configure(text=f"Erro inesperado: {e}")


        alinharbtn = ctk.CTkFrame(janela, fg_color="transparent")
        alinharbtn.pack(pady=15)

        ctk.CTkButton(alinharbtn, text="Salvar Data", command=salvar_data, width=140).pack(side="left", padx=10)
        ctk.CTkButton(alinharbtn, text="Voltar ao Menu", command=self.tela_menu_inicial, width=140).pack(side="left", padx=10)

app = App()
app.mainloop()