import oracledb
import json


def connect_to_db():
    try:
        # Tentando estabelecer a conexão
        connection = oracledb.connect(user='rm559438', password='080598', dsn='oracle.fiap.com.br:1521/ORCL')
        print("Conexão estabelecida com sucesso!")
        return connection
    except oracledb.DatabaseError as e:
        # Captura erros de banco de dados e exibe mensagem de erro
        error, = e.args
        print("Erro ao conectar ao banco de dados:")
        print(f"Código do erro: {error.code}")
        print(f"Mensagem do erro: {error.message}")
        return None
    except Exception as e:
        # Captura outros tipos de exceções e exibe mensagem de erro
        print("Ocorreu um erro inesperado:")
        print(str(e))
        return None


# Função para cadastrar produtor
def insert_producers(connection):
        try:
            nome = input("Digite o nome do produtor: ")

            # Validação do CPF
            while True:
                cpf = input("Digite o CPF do produtor (11 dígitos): ")
                if len(cpf) == 11 and cpf.isdigit():
                    break
                else:
                    print("Erro: O CPF deve ter 11 dígitos numéricos.")

            # Validação do telefone
            telefone = input("Digite o telefone do produtor: ")

            # Validação do email
            while True:
                email = input("Digite o email do produtor: ")
                if "@" in email and "." in email:
                    break
                else:
                    print("Erro: Email inválido. Certifique-se de incluir '@' e '.'.")

            endereco = input("Digite o endereço do produtor: ")
            cidade = input("Digite a cidade do produtor: ")

            # Validação do estado
            while True:
                estado = input("Digite o estado do produtor (2 letras): ")
                if len(estado) == 2 and estado.isalpha():
                    break
                else:
                    print("Erro: O estado deve ter 2 letras.")

            nome_fazenda = input("Digite o nome da fazenda: ")
            area_hectares = float(input("Digite a área em hectares: "))

            # Validação do CEP
            while True:
                cep = input("Digite o CEP do produtor (8 dígitos): ")
                if len(cep) == 8 and cep.isdigit():
                    break
                else:
                    print("Erro: O CEP deve ter 8 dígitos numéricos.")

            # Inserindo os dados no banco
            cursor = connection.cursor()
            cursor.execute(""" 
                INSERT INTO PRODUTOR (nome, cpf, telefone, email, endereco, cidade, estado, nome_fazenda, area_hectares, pais, cep) 
                VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, 'Brasil', :10) 
            """, (nome, cpf, telefone, email, endereco, cidade, estado, nome_fazenda, area_hectares, cep))

            connection.commit()
            print("Produtor cadastrado com sucesso!")

        except oracledb.DatabaseError as e:
            error, = e.args
            print("Erro ao cadastrar produtor:")
            print(f"Código do erro: {error.code}")
            print(f"Mensagem do erro: {error.message}")
        except Exception as e:
            print("Ocorreu um erro inesperado:")
            print(str(e))
        finally:
            cursor.close()


# Função para cadastrar produto
def insert_products(connection):
    try:
        nome_produto = input("Digite o nome do produto: ")
        if not nome_produto:
            raise ValueError("O nome do produto não pode ser vazio.")

        tipo = input("Digite o tipo do produto: ")
        if not tipo:
            raise ValueError("O tipo do produto não pode ser vazio.")

        descricao = input("Digite a descrição do produto: ")
        if not descricao:
            raise ValueError("A descrição do produto não pode ser vazia.")

        # Inserindo os dados no banco
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO PRODUTO (NOME, TIPO, DESCRICAO)
            VALUES (:1, :2, :3)
        """, (nome_produto, tipo, descricao))

        connection.commit()
        print("Produto cadastrado com sucesso!")

    except ValueError as ve:
        print(f"Erro de validação: {ve}")
    except oracledb.DatabaseError as e:
        error, = e.args
        print("Erro ao cadastrar produto:")
        print(f"Código do erro: {error.code}")
        print(f"Mensagem do erro: {error.message}")
    except Exception as e:
        print("Ocorreu um erro inesperado:")
        print(str(e))
    finally:
        cursor.close()


# Função para cadastrar comércio
def insert_commerce(connection):
    try:
        nome = input("Digite o nome do comércio: ")
        cidade = input("Digite a cidade do comércio: ")
        estado = input("Digite o estado do comércio (2 letras): ")
        pais = input("Digite o país do comércio: ")
        cep = input("Digite o CEP do comércio (8 dígitos): ")
        nome_localizacao = input("Digite o nome da localização do comércio: ")

        # Validação simples
        if len(estado) != 2:
            raise ValueError("O estado deve ter 2 letras.")
        if len(cep) != 8 or not cep.isdigit():
            raise ValueError("O CEP deve ter 8 dígitos e ser numérico.")

        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO COMERCIO (nome, cidade, estado, pais, cep, nome_localizacao)
            VALUES (:1, :2, :3, :4, :5, :6)
        """, (nome, cidade, estado, pais, cep, nome_localizacao))

        connection.commit()
        print("Comércio cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro ao cadastrar comércio: {e}")

    finally:
        cursor.close()


def main_menu():
    connection = connect_to_db()

    while True:
        print("\nMenu:")
        print("1. Cadastrar Produtor")
        print("2. Cadastrar Produto")
        print("3. Cadastrar Comércio")
        print("4. Listar Tabelas")
        print("5. Associações")  # Nova opção
        print("6. Listar Associações")  # Nova opção
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            insert_producers(connection)
        elif choice == '2':
            insert_products(connection)
        elif choice == '3':
            insert_commerce(connection)
        elif choice == '4':
            listing_menu(connection)
        elif choice == '5':
            association_menu(connection)
        elif choice == '6':
            listing_association_menu(connection)
        elif choice == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    connection.close()

def listing_association_menu(connection):
    while True:
        print("\nMenu de Associações:")
        print("1. Listar Associações de Produtores e Comércio")
        print("2. Listar Associações de Produtores e Produtos")
        print("3. Listar Associações de Produtos e Comércio")  # Nova opção
        print("0. Voltar")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            list_producer_commerce_associations(connection)
        elif choice == '2':
            list_producer_product_associations(connection)
        elif choice == '3':
            list_product_commerce_associations(connection)  # Função para listar produtos e comércio
        elif choice == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def list_product_commerce_associations(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT pc.produto_id, prod.nome AS produto_nome, pc.comercio_id, c.nome AS comercio_nome
        FROM PRODUTO_COMERCIO pc
        JOIN PRODUTO prod ON pc.produto_id = prod.produto_id
        JOIN COMERCIO c ON pc.comercio_id = c.comercio_id
    """)

    associations = cursor.fetchall()
    association_list = []

    print("\nLista de Associações entre Produtos e Comércio:")
    for row in associations:
        association = {
            "produto_id": row[0],
            "produto_nome": row[1],
            "comercio_id": row[2],
            "comercio_nome": row[3]
        }
        association_list.append(association)
        print(f"Produto ID: {association['produto_id']}, Nome: {association['produto_nome']} - "
              f"Comércio ID: {association['comercio_id']}, Nome: {association['comercio_nome']}")

    # Salvando a lista de associações em um arquivo JSON
    with open('../associacoes_produto_comercio.json', 'w', encoding='utf-8') as json_file:
        json.dump(association_list, json_file, ensure_ascii=False, indent=4)

    print("\nLista de associações salva em 'associacoes_produto_comercio.json'.")
    cursor.close()



def list_producer_product_associations(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT pp.produtor_id, p.nome AS produtor_nome, pp.produto_id, prod.nome AS produto_nome
        FROM PRODUTOR_PRODUTO pp
        JOIN PRODUTOR p ON pp.produtor_id = p.produtor_id
        JOIN PRODUTO prod ON pp.produto_id = prod.produto_id
    """)

    associations = cursor.fetchall()
    association_list = []

    print("\nLista de Associações entre Produtores e Produtos:")
    for row in associations:
        association = {
            "produtor_id": row[0],
            "produtor_nome": row[1],
            "produto_id": row[2],
            "produto_nome": row[3]
        }
        association_list.append(association)
        print(f"Produtor ID: {association['produtor_id']}, Nome: {association['produtor_nome']} - "
              f"Produto ID: {association['produto_id']}, Nome: {association['produto_nome']}")

    # Salvando a lista de associações em um arquivo JSON
    with open('../associacoes_produtor_produto.json', 'w', encoding='utf-8') as json_file:
        json.dump(association_list, json_file, ensure_ascii=False, indent=4)

    print("\nLista de associações salva em 'associacoes_produtor_produto.json'.")
    cursor.close()

def list_producer_commerce_associations(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT pc.produtor_id, p.nome AS produtor_nome, pc.comercio_id, c.nome AS comercio_nome
        FROM PRODUTOR_COMERCIO pc
        JOIN PRODUTOR p ON pc.produtor_id = p.produtor_id
        JOIN COMERCIO c ON pc.comercio_id = c.comercio_id
    """)

    associations = cursor.fetchall()
    association_list = []

    print("\nLista de Associações entre Produtores e Comércio:")
    for row in associations:
        association = {
            "produtor_id": row[0],
            "produtor_nome": row[1],
            "comercio_id": row[2],
            "comercio_nome": row[3]
        }
        association_list.append(association)
        print(f"Produtor ID: {association['produtor_id']}, Nome: {association['produtor_nome']} - "
              f"Comércio ID: {association['comercio_id']}, Nome: {association['comercio_nome']}")

    # Salvando a lista de associações em um arquivo JSON
    with open('../associacoes_produtor_comercio.json', 'w', encoding='utf-8') as json_file:
        json.dump(association_list, json_file, ensure_ascii=False, indent=4)

    print("\nLista de associações salva em 'associacoes_produtor_comercio.json'.")
    cursor.close()


def list_producers(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM PRODUTOR")

        rows = cursor.fetchall()
        producers_list = []

        print("\nLista de Produtores:")
        for row in rows:
            producer = {
                "produtor_id": row[0],
                "nome": row[1],
                "cpf": row[2],
                "telefone": row[3],
                "email": row[4],
                "endereco": row[5],
                "cidade": row[6],
                "estado": row[7],
                "nome_fazenda": row[8],
                "area_hectares": row[9],
                "pais": row[10],
                "cep": row[11],
                "data_registro": row[12].strftime('%Y-%m-%d') if row[12] else None  # Formatar data
            }
            producers_list.append(producer)
            print(producer)

        # Salvando a lista de produtores em um arquivo JSON
        with open('../produtores.json', 'w', encoding='utf-8') as json_file:
            json.dump(producers_list, json_file, ensure_ascii=False, indent=4)
        print("\nLista de produtores salva em 'produtores.json'.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print("Erro ao listar produtores:")
        print(f"Código do erro: {error.code}")
        print(f"Mensagem do erro: {error.message}")
    finally:
        cursor.close()


def listing_menu(connection):
    while True:
        print("\nMenu de Listagem:")
        print("1. Listar Produtores")
        print("2. Listar Produtos")
        print("3. Listar Comércios")
        print("4. Voltar ao Menu Principal")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            list_producers(connection)
        elif choice == '2':
            list_products(connection)
        elif choice == '3':
            list_products(connection)
        elif choice == '4':
            break  # Volta para o menu principal
        else:
            print("Opção inválida, tente novamente.")

def list_products(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM PRODUTO")

        rows = cursor.fetchall()
        products_list = []

        print("\nLista de Produtos:")
        for row in rows:
            product = {
                "produt_id": row[0],
                "nome": row[1],
                "tipo": row[2],
                "descricao": row[3],
            }
            products_list.append(product)
            print(product)

        # Salvando a lista de produtos em um arquivo JSON
        with open('../comercios.json', 'w', encoding='utf-8') as json_file:
            json.dump(products_list, json_file, ensure_ascii=False, indent=4)
        print("\nLista de produtos salva em 'produtos.json'.")

    except Exception as e:
        print(f"Erro ao listar produtos: {e}")

    finally:
        cursor.close()

def list_commerces(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM COMERCIO")

        rows = cursor.fetchall()
        commerces_list = []

        print("\nLista de Comércio:")
        for row in rows:
            commerce = {
                "comercio_id": row[0],
                "nome": row[1],
                "cidade": row[2],
                "estado": row[3],
                "pais": row[4],
                "cep": row[5],
                "nome_localizacao": row[6]
            }
            commerces_list.append(commerce)
            print(commerce)

        # Salvando a lista de comercios em um arquivo JSON
        with open('../comercios.json', 'w', encoding='utf-8') as json_file:
            json.dump(commerces_list, json_file, ensure_ascii=False, indent=4)
        print("\nLista de comércios salva em 'comercios.json'.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print("Erro ao listar comercios:")
        print(f"Código do erro: {error.code}")
        print(f"Mensagem do erro: {error.message}")
    except Exception as e:
        print("Ocorreu um erro inesperado:")
        print(str(e))
    finally:
        cursor.close()

def association_menu(connection):
    while True:
        print("\nSubmenu de Associação de Tabelas:")
        print("1. Associar Produtor a Comércio")
        print("2. Associar Produtor a Produto")
        print("3. Associar Produto a Comércio")
        print("0. Voltar")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            associate_producer_commerce(connection)
        elif choice == '2':
            associate_producer_product(connection)
        elif choice == '3':
            associate_product_commerce(connection)
        elif choice == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


def associate_producer_commerce(connection):
    cursor = connection.cursor()

    # Listar produtores disponíveis
    while True:
        print("\nSelecione um produtor pela ID:")
        cursor.execute("SELECT * FROM PRODUTOR")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Nome: {row[1]}")  # Exibindo ID e Nome do produtor

        producer_id = input("Digite o ID do produtor: ")

        # Verificar se o produtor existe
        cursor.execute("SELECT COUNT(*) FROM PRODUTOR WHERE produtor_id = :1", (producer_id,))
        if cursor.fetchone()[0] > 0:
            break
        else:
            print("ID de produtor inválido. Tente novamente.")

    # Listar comércios disponíveis
    while True:
        print("\nSelecione um comércio pela ID:")
        cursor.execute("SELECT * FROM COMERCIO")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Nome: {row[1]}")  # Exibindo ID e Nome do comércio

        commerce_id = input("Digite o ID do comércio: ")

        # Verificar se o comércio existe
        cursor.execute("SELECT COUNT(*) FROM COMERCIO WHERE comercio_id = :1", (commerce_id,))
        if cursor.fetchone()[0] > 0:
            break
        else:
            print("ID de comércio inválido. Tente novamente.")

    # Inserindo a associação no banco de dados
    cursor.execute("""
        INSERT INTO PRODUTOR_COMERCIO (produtor_id, comercio_id) 
        VALUES (:1, :2)
    """, (producer_id, commerce_id))

    connection.commit()
    print("Associação de produtor a comércio criada com sucesso!")
    cursor.close()

def list_producer_commerce_associations(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT pc.produtor_id, p.nome AS produtor_nome, pc.comercio_id, c.nome AS comercio_nome
        FROM PRODUTOR_COMERCIO pc
        JOIN PRODUTOR p ON pc.produtor_id = p.produtor_id
        JOIN COMERCIO c ON pc.comercio_id = c.comercio_id
    """)

    associations = cursor.fetchall()
    association_list = []

    print("\nLista de Associações entre Produtores e Comércio:")
    for row in associations:
        association = {
            "produtor_id": row[0],
            "produtor_nome": row[1],
            "comercio_id": row[2],
            "comercio_nome": row[3]
        }
        association_list.append(association)
        print(f"Produtor ID: {association['produtor_id']}, Nome: {association['produtor_nome']} - "
              f"Comércio ID: {association['comercio_id']}, Nome: {association['comercio_nome']}")

    # Salvando a lista de associações em um arquivo JSON
    with open('../associacoes_produtor_comercio.json', 'w', encoding='utf-8') as json_file:
        json.dump(association_list, json_file, ensure_ascii=False, indent=4)

    print("\nLista de associações salva em 'associacoes_produtor_comercio.json'.")
    cursor.close()


def associate_producer_product(connection):
    cursor = connection.cursor()

    # Listar produtores disponíveis
    while True:
        print("\nSelecione um produtor pela ID:")
        cursor.execute("SELECT produtor_id, nome FROM PRODUTOR")  # Selecionar apenas os campos necessários
        rows = cursor.fetchall()

        # Verificar se existem produtores disponíveis
        if not rows:
            print("Não há produtores cadastrados.")
            return  # Retorna se não houver produtores

        for row in rows:
            print(f"ID: {row[0]}, Nome: {row[1]}")  # Exibindo ID e Nome do produtor

        producer_id = input("Digite o ID do produtor: ")

        # Verificar se o produtor existe
        cursor.execute("SELECT COUNT(*) FROM PRODUTOR WHERE produtor_id = :1", (producer_id,))
        if cursor.fetchone()[0] > 0:
            break
        else:
            print("ID de produtor inválido. Tente novamente.")

    # Listar produtos disponíveis
    while True:
        print("\nSelecione um produto pela ID:")
        cursor.execute("SELECT produto_id, nome FROM PRODUTO")  # Selecionar apenas os campos necessários
        rows = cursor.fetchall()

        # Verificar se existem produtos disponíveis
        if not rows:
            print("Não há produtos cadastrados.")
            return  # Retorna se não houver produtos

        for row in rows:
            print(f"ID: {row[0]}, Nome: {row[1]}")  # Exibindo ID e Nome do produto

        product_id = input("Digite o ID do produto: ")

        # Verificar se o produto existe
        cursor.execute("SELECT COUNT(*) FROM PRODUTO WHERE produto_id = :1", (product_id,))
        if cursor.fetchone()[0] > 0:
            break
        else:
            print("ID de produto inválido. Tente novamente.")

    # Inserindo a associação no banco de dados
    cursor.execute("""
        INSERT INTO PRODUTOR_PRODUTO (produtor_id, produto_id) 
        VALUES (:1, :2)
    """, (producer_id, product_id))

    connection.commit()
    print("Associação de produtor a produto criada com sucesso!")
    cursor.close()

def associate_product_commerce(connection):
    cursor = connection.cursor()

    # Listar produtos disponíveis
    while True:
        print("\nSelecione um produto pela ID:")
        cursor.execute("SELECT * FROM PRODUTO")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Nome: {row[1]}")  # Exibindo ID e Nome do produto

        product_id = input("Digite o ID do produto: ")

        # Verificar se o produto existe
        cursor.execute("SELECT COUNT(*) FROM PRODUTO WHERE produto_id = :1", (product_id,))
        if cursor.fetchone()[0] > 0:
            break
        else:
            print("ID de produto inválido. Tente novamente.")

    # Listar comércios disponíveis
    while True:
        print("\nSelecione um comércio pela ID:")
        cursor.execute("SELECT * FROM COMERCIO")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Nome: {row[1]}")  # Exibindo ID e Nome do comércio

        commerce_id = input("Digite o ID do comércio: ")

        # Verificar se o comércio existe
        cursor.execute("SELECT COUNT(*) FROM COMERCIO WHERE comercio_id = :1", (commerce_id,))
        if cursor.fetchone()[0] > 0:
            break
        else:
            print("ID de comércio inválido. Tente novamente.")

    # Inserindo a associação no banco de dados
    cursor.execute("""
        INSERT INTO PRODUTO_COMERCIO (produto_id, comercio_id) 
        VALUES (:1, :2)
    """, (product_id, commerce_id))

    connection.commit()
    print("Associação de produto a comércio criada com sucesso!")
    cursor.close()


if __name__ == "__main__":
    main_menu()
