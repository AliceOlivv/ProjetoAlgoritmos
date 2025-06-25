
import inquirer
#lembrar pip install inquirer
import funções

pergunta = [
    inquirer.List(
        'inicio',
        message="O que deseja fazer?",
        choices=[
            'Pesquisa de Produto ou Agendamento de serviço',
            'Cadastramento de novos produtos ou serviços',
            'Gerenciamento de Estoque',
            'Remoção de produto ou serviço',
            'Resumo Mensal'
        ]
    )
]

resposta = inquirer.prompt(pergunta)

if resposta["inicio"]== "Pesquisa de Produto ou Agendamento de serviço":
        
    prod_ou_serv = [
        inquirer.List(
            'escolha',
            message="O que deseja fazer?",
            choices=[
                'Pesquisa de Produto',
                'Agendamento de Serviço',
            ]
        )
    ]

    resposta2=inquirer.prompt(prod_ou_serv)

    if resposta2["escolha"]== "Pesquisa de Produto":

        funções.PesquisaDeProdutos()

    #elif resposta2["escolha"]== "Agendamento de serviço"
             
elif resposta["inicio"]== "Cadastramento de novos produtos ou serviços":
      
    cadastramento = [
         inquirer.List(
            'cadastro',
            message="Deseja fazer um novo cadastramento de qual setor?",
            choices=[
                'Produtos',
                'Serviços',
            ]
        )
    ]

    resposta3=inquirer.prompt(cadastramento)

    if resposta3["cadastro"]=="Produtos":
        funções.CadastrarProdutos()

    if resposta3["cadastro"]=="Serviços":
        funções.CadastrarServiço()
         
elif resposta["inicio"]== "Gerenciamento de Estoque":

    gerenciamento = [
         inquirer.List(
            'estoque',
            message="O que deseja fazer ?",
            choices=[
                'Adicionar produto',
                'Remover produto',
            ]
        )
    ] 

    resposta4=inquirer.prompt(gerenciamento)

    if resposta4["estoque"]=="Adicionar produto":
         funções.AdicionarProdutoAoEstoque()
         
    if resposta4["estoque"]=="Remover produto":
         funções.RemoverProdutoDoEstoque()

elif resposta["inicio"]== "Remoção de produto ou serviço":
      
    cadastramento = [
         inquirer.List(
            'remover',
            message="Deseja fazer a remoção de qual setor?",
            choices=[
                'Produtos',
                'Serviços',
            ]
        )
    ]

    resposta5=inquirer.prompt(cadastramento)

    if resposta5["remover"]=="Produtos":
        funções.RemovercadastroProduto()

    if resposta5["remover"]=="Serviços":
        funções.RemovercadastroServico()

#if resposta["inicio"]== "Resumo Mensal":
         

      
      

            
input("")