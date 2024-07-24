from web3 import Web3
from Blockchain.keys import ABI_CONTRATO, REDE, CONTRATO, CONTA, PRIVATE_KEY

# Conectar ao provedor
rede_url = REDE
web3 = Web3(Web3.HTTPProvider(rede_url))

# Verificar conexão
if not web3.is_connected():
    print("Não foi possível conectar ao provedor.")
    exit()

contrato_endereco = CONTRATO
contrato_abi = ABI_CONTRATO

# Criar uma instância do contrato
contrato = web3.eth.contract(address=contrato_endereco, abi=contrato_abi)

# Adicionar um aluno
def adicionar_aluno(id, nome, edicao, pontos, img_hash):
    try:
        conta = CONTA
        nonce = web3.eth.get_transaction_count(conta)
        tx = contrato.functions.adicionarAluno(id, nome, edicao, pontos, img_hash).build_transaction({
            'from': conta,
            'gas': 2000000,
            'gasPrice': web3.to_wei('50', 'gwei'),
            'nonce': nonce
        })

        # Assinar a transação
        private_key = PRIVATE_KEY
        signed_tx = web3.eth.account.sign_transaction(tx, private_key)

        # Enviar a transação
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transação enviada: {tx_hash.hex()}")

        # Esperar a transação ser minerada e obter o recibo
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        # Verificar se a transação foi bem-sucedida
        if tx_receipt.status == 1:
            print("Transação concluída com sucesso!")
            return True, tx_hash.hex()
        else:
            print("Transação falhou!")
            return False, None

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False

# Buscar alunos por ID
def buscar_aluno_por_id(id):
    try:
        alunos = contrato.functions.buscarAlunoPorID(id).call()
        return alunos
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Buscar todos os alunos de uma edição
def buscar_alunos_por_edicao(edicao):
    try:
        alunos = contrato.functions.buscarAlunosPorEdicao(edicao).call()
        return alunos
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Buscar todos os registros de alunos
def buscar_todos_os_alunos():
    try:
        alunos = contrato.functions.buscarTodosOsAlunos().call()
        return alunos

    except Exception as e:
        print(f"Ocorreu um erro: {e}")