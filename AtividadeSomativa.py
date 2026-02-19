import json

# Função para carregar dados de um arquivo JSON
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Função para salvar dados em um arquivo JSON
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

# Função genérica para inclusão
def incluir(module_name, **kwargs):
    module = carregar_dados(f'{module_name}.json')
    for registro in module:
        if registro['codigo'] == kwargs['codigo']:
            print(f"Erro: Código '{kwargs['codigo']}' já existe em '{module_name}'.")
            return
    module.append(kwargs)
    salvar_dados(f'{module_name}.json', module)
    print(f"Registro incluído com sucesso em '{module_name}'.")

# Função genérica para listar registros
def listar(module_name):
    module = carregar_dados(f'{module_name}.json')
    if module:
        for registro in module:
            print(registro)
    else:
        print(f"Nenhum registro encontrado em '{module_name}'.")

# Função genérica para atualizar registros
def atualizar(module_name, codigo, **kwargs):
    module = carregar_dados(f'{module_name}.json')
    for registro in module:
        if registro['codigo'] == codigo:
            registro.update(kwargs)
            salvar_dados(f'{module_name}.json', module)
            print(f"Registro atualizado com sucesso em '{module_name}'.")
            return
    print(f"Erro: Código '{codigo}' não encontrado em '{module_name}'.")

# Função genérica para excluir registros
def excluir(module_name, codigo):
    module = carregar_dados(f'{module_name}.json')
    for registro in module:
        if registro['codigo'] == codigo:
            module.remove(registro)
            salvar_dados(f'{module_name}.json', module)
            print(f"Registro excluído com sucesso em '{module_name}'.")
            return
    print(f"Erro: Código '{codigo}' não encontrado em '{module_name}'.")

# Menus específicos para cada módulo
def menu_operacoes(module_name):
    while True:
        print(f"\n--- Menu de Operações - {module_name.capitalize()} ---")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("9. Voltar")
        opcao = int(input("Escolha uma ação: "))

        if opcao == 1:
            codigo = int(input("Código: "))
            if module_name == 'matriculas':
                codigo_estudante = int(input("Código do estudante: "))
                incluir(module_name, codigo=codigo, codigo_estudante=codigo_estudante)
            elif module_name == 'turmas':
                codigo_professor = int(input("Código do professor: "))
                codigo_disciplina = int(input("Código da disciplina: "))
                incluir(module_name, codigo=codigo, codigo_professor=codigo_professor, codigo_disciplina=codigo_disciplina)
            else:
                nome = input(f"Nome do {module_name[:-1]}: ")
                cpf = input(f"CPF do {module_name[:-1]}: ") if module_name != 'disciplinas' else None
                incluir(module_name, codigo=codigo, nome=nome, cpf=cpf)

        elif opcao == 2:
            listar(module_name)

        elif opcao == 3:
            codigo = int(input("Código: "))
            if module_name == 'matriculas':
                codigo_estudante = int(input("Novo código do estudante: "))
                atualizar(module_name, codigo, codigo_estudante=codigo_estudante)
            elif module_name == 'turmas':
                codigo_professor = int(input("Novo código do professor: "))
                codigo_disciplina = int(input("Novo código da disciplina: "))
                atualizar(module_name, codigo, codigo_professor=codigo_professor, codigo_disciplina=codigo_disciplina)
            else:
                nome = input(f"Novo nome do {module_name[:-1]}: ")
                cpf = input(f"Novo CPF do {module_name[:-1]}: ") if module_name != 'disciplinas' else None
                atualizar(module_name, codigo, nome=nome, cpf=cpf)

        elif opcao == 4:
            codigo = int(input("Código: "))
            excluir(module_name, codigo)

        elif opcao == 9:
            break
        else:
            print("Opção inválida.")

# Menu principal
def menu_principal():
    while True:
        print("\n--- Sistema de Gestão Acadêmica ---")
        print("1. Gerenciar Estudantes")
        print("2. Gerenciar Disciplinas")
        print("3. Gerenciar Professores")
        print("4. Gerenciar Turmas")
        print("5. Gerenciar Matrículas")
        print("9. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            menu_operacoes('estudantes')
        elif opcao == 2:
            menu_operacoes('disciplinas')
        elif opcao == 3:
            menu_operacoes('professores')
        elif opcao == 4:
            menu_operacoes('turmas')
        elif opcao == 5:
            menu_operacoes('matriculas')
        elif opcao == 9:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

# Executar o menu principal
if __name__ == "__main__":
    menu_principal()
