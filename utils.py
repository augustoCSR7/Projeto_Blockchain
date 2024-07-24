from PIL import Image
import numpy as np
import io
import requests
import base64

# Converter a matriz binária para uma imagem PNG
def matrix_to_png_buffer(matrix):
    # Garantir que a matriz seja uint8
    if matrix.dtype != np.uint8:
        matrix = matrix.astype(np.uint8)

    # Criar a imagem com PIL
    image = Image.fromarray(matrix, mode='L')  # 'L' para imagens em escala de cinza

    # Salvar a imagem em um buffer de memória
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)  # Voltar para o início do buffer
    return buffer

def pinata_send(png_buffer):

    jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI4OTJhMTVhZS00YzRlLTQ1OWUtYmZlYy1lNjQzMGI1NjlhOTUiLCJlbWFpbCI6Imxhci5zbmYyMUB1ZWEuZWR1LmJyIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiRlJBMSJ9LHsiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImZmYWI3N2M2YjBmN2FjNGU3NWQ4Iiwic2NvcGVkS2V5U2VjcmV0IjoiZmE5MGVlZTZlNzE4NGE1OTAwZjFkOTQ4M2M1NDRmNzA3ZWQ5MzQ2MzNjMDMyMTBiMDIxYmM0ZDFjZWY4MWMwOCIsImV4cCI6MTc1MzMxODI1OH0.E9GFSgZTnuT902f7ejX4ocWwCQtt722JiGqwS36vlzQ'

    headers = {
        'Authorization': f'Bearer {jwt}',
    }

    files = {
        'file': ('imagem_binarizada.png', png_buffer, 'image/png')
    }

    response = requests.post('https://api.pinata.cloud/pinning/pinFileToIPFS', headers=headers, files=files)


    return response.json().get('IpfsHash')

def pinata_receive(cid):
    try:
        ipfs_gateway_url = f'https://turquoise-generous-hedgehog-935.mypinata.cloud/ipfs/{cid}'

        # Fazer a requisição
        response = requests.get(ipfs_gateway_url)

        # Carregar a imagem em memória
        image = Image.open(io.BytesIO(response.content))

        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return image_base64
    
    except Exception as e:
        print(f"Ocorreu um erro ao pedir imagem: {e}")

# Criar o buffer de memória
#png_buffer = matrix_to_png_buffer(imgTh)
