from Blockchain.blockchain import Block, Blockchain
from CV.main_cv import processar_imagem
import time

if __name__ == "__main__":
    blockchain = Blockchain(2)

    imagem = "Gabaritos/gabarito_augusto.jpeg"
    pontuacao_augusto = processar_imagem(imagem)
    print(f'Pontuação do Augusto: {pontuacao_augusto}\n')

    blockchain.add_block(Block(1, time.time(), blockchain.get_latest_block().hash, f"PONTUAÇÃO DO AUGUSTO = {pontuacao_augusto}"))

    blockchain.add_block(Block(2, time.time(), blockchain.get_latest_block().hash, "Sylvain Saurel"))

    print(blockchain)

    # print("Blockchain é válida? ")
    # if not blockchain.is_blockchain_valid():
    #     print("Não é válida!!!")
    # else:
    #     print("Sim, é válida!!!")
