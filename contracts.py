from web3 import Web3
from abi import ABI_CONTRATO

# Conectar ao provedor (Ganache ou outro provedor)
ganache_url = "http://localhost:7545"  # Substitua pela URL do seu provedor
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Verificar conexão
if not web3.is_connected():
    print("Não foi possível conectar ao provedor.")
    exit()

# Endereço do contrato e ABI (substitua pelos valores corretos)
contrato_endereco = "0xeA3B9851071Ee852ad084e5d201Fe02cDC08145c"  # Endereço do contrato implantado
contrato_abi = ABI_CONTRATO

# Criar uma instância do contrato
contrato = web3.eth.contract(address=contrato_endereco, abi=contrato_abi)

# Adicionar um aluno
def adicionar_aluno(id, nome, edicao, pontos, img_hash):
    try:
        conta = "0xe3520D0e5Fa63A104bFfee2107aFEEC79dbb9AD6"  # Substitua pelo endereço da conta
        nonce = web3.eth.get_transaction_count(conta)
        tx = contrato.functions.adicionarAluno(id, nome, edicao, pontos, img_hash).build_transaction({
            'from': conta,
            'gas': 2000000,
            'gasPrice': web3.to_wei('50', 'gwei'),
            'nonce': nonce
        })

        # Assinar a transação
        private_key = "0x651511d33437ecbff3ac39882bc5bdbfa6b3d5e59807413873fc8c7b1d3d40c7"
        signed_tx = web3.eth.account.sign_transaction(tx, private_key)

        # Enviar a transação
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transação enviada: {tx_hash.hex()}")

        # Esperar a transação ser minerada e obter o recibo
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        # Verificar se a transação foi bem-sucedida
        if tx_receipt.status == 1:
            print("Transação concluída com sucesso!")
            return True
        else:
            print("Transação falhou!")
            return False

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False

# Buscar alunos por ID
def buscar_aluno_por_id(id):
    alunos = contrato.functions.buscarAlunoPorID(id).call()
    for aluno in alunos:
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Edição: {aluno[2]}")
        print(f"Pontos: {aluno[3]}")
        print(f"Imagem Hash: {aluno[4]}")
        print("----------")

# Buscar todos os alunos de uma edição
def buscar_alunos_por_edicao(edicao):
    alunos = contrato.functions.buscarAlunosPorEdicao(edicao).call()
    for aluno in alunos:
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Edição: {aluno[2]}")
        print(f"Pontos: {aluno[3]}")
        print(f"Imagem Hash: {aluno[4]}")
        print("----------")

# Buscar todos os registros de alunos
def buscar_todos_os_alunos():
    try:
        # Buscar todos os registros de alunos
        alunos = contrato.functions.buscarTodosOsAlunos().call()

        return alunos
        
        # Iterar sobre a lista de alunos e imprimir as informações
        for aluno in alunos:
            print(f"ID: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Edição: {aluno[2]}")
            print(f"Pontos: {aluno[3]}")
            print(f"Imagem Hash: {aluno[4]}")
            print("----------")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# Exemplos de uso
#adicionar_aluno(11, "João", "2024", 10, "hash_da_imagem")
#buscar_aluno_por_id(1)
#buscar_alunos_por_edicao("2024")
#buscar_todos_os_alunos()
