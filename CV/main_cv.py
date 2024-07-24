
import os
import cv2
import pickle
import CV.extrairGabarito as exG

def carregar_pickle(nome_arquivo):
    pasta_atual = os.path.dirname(__file__)  # Diretório onde o script Python está localizado
    caminho_arquivo = os.path.join(pasta_atual, nome_arquivo)
    
    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado na pasta {pasta_atual}.")
        return None
    except pickle.PickleError:
        print(f"Erro ao carregar o arquivo {nome_arquivo}.")
        return None

# Carregar os dados dos arquivos pickle
campos = carregar_pickle('campos.pkl')
resp = carregar_pickle('resp.pkl')

if campos is None or resp is None:
    raise SystemExit("Erro ao carregar os dados dos arquivos pickle.")

# Respostas corretas para comparação
respostasCorretas = ["1-A", "2-C", "3-B", "4-D", "5-A"]


def processar_imagem(image_path):
    # Carregar e redimensionar a imagem
    imagem = cv2.imread(image_path)
    imagem = cv2.resize(imagem, (500, 700))

    # Extrair gabarito e contorno
    gabarito, bbox = exG.extrairMaiorCtn(imagem)

    # Converter gabarito para escala de cinza e aplicar limiarização
    imgGray = cv2.cvtColor(gabarito, cv2.COLOR_BGR2GRAY)
    ret, imgTh = cv2.threshold(imgGray, 70, 255, cv2.THRESH_BINARY_INV)

    # Desenhar retângulo em torno do contorno detectado
    cv2.rectangle(imagem, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 3)

    respostas = []

    # Processar cada campo para extrair as respostas
    for id, vg in enumerate(campos):
        x = int(vg[0])
        y = int(vg[1])
        w = int(vg[2])
        h = int(vg[3])
        cv2.rectangle(gabarito, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imgTh, (x, y), (x + w, y + h), (255, 255, 255), 1)
        campo = imgTh[y:y + h, x:x + w]
        height, width = campo.shape[:2]
        tamanho = height * width
        pretos = cv2.countNonZero(campo)
        percentual = round((pretos / tamanho) * 100, 2)
        if percentual >= 15:
            cv2.rectangle(gabarito, (x, y), (x + w, y + h), (255, 0, 0), 2)
            respostas.append(resp[id])

    erros = 0
    acertos = 0

    # Verificar se o número de respostas coincide com o esperado
    if len(respostas) == len(respostasCorretas):
        for num, res in enumerate(respostas):
            if res == respostasCorretas[num]:
                acertos += 1
            else:
                erros += 1

        pontuacao = int(acertos * 2)

        return pontuacao, imgTh

    return 0, imgTh