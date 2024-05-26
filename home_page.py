import flet as ft
import base64
import cv2
from tkinter import Tk, filedialog
import threading
import time
from Blockchain.blockchain import Block, Blockchain
from CV.main_cv import processar_imagem


class ImageDisplay(ft.UserControl):
    def build(self):
        self.img = ft.Image(
            border_radius=ft.border_radius.all(20),
            src="https://via.placeholder.com/400x400?text=No+Image"  # Imagem estática inicial
        )
        return self.img

    def update_image(self, image_path):
        if image_path:
            image = cv2.imread(image_path)
            if image is None:
                raise Exception("Erro ao carregar a imagem. Verifique o caminho.")

            # Redimensionar a imagem para caber na interface
            frame = cv2.resize(image, (400, 400))

            # Codificar a imagem em base64
            _, im_arr = cv2.imencode('.png', frame)
            im_b64 = base64.b64encode(im_arr).decode("utf-8")

            # Atualizar a fonte da imagem
            self.img.src_base64 = im_b64
            self.update()

    def update_image_from_frame(self, frame):
        # Redimensionar a imagem para caber na interface
        frame = cv2.resize(frame, (400, 400))

        # Codificar a imagem em base64
        _, im_arr = cv2.imencode('.png', frame)
        im_b64 = base64.b64encode(im_arr).decode("utf-8")

        # Atualizar a fonte da imagem
        self.img.src_base64 = im_b64
        self.update()


def open_file_dialog():
    Tk().withdraw()  # Ocultar a janela principal do Tkinter
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    return file_path


def home_page(page: ft.Page, blockchain):
    print(blockchain)

    def on_select_image(e):
        file_path = open_file_dialog()
        if file_path:  # Verificar se um arquivo foi selecionado
            image_display.update_image(file_path)
            points.value, teste = processar_imagem(file_path)
            page.update()

    def on_connect_webcam(e):
        def capture_webcam():
            cap = cv2.VideoCapture("http://192.168.0.10:8080/video")
            if not cap.isOpened():
                print("Erro ao abrir a webcam.")
                return

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                image_display.update_image_from_frame(frame)
                time.sleep(1 / 30)  # Atualizar a 30 FPS

            cap.release()

        threading.Thread(target=capture_webcam).start()

    image_display = ImageDisplay()

    select_image_button = ft.ElevatedButton(
        text="Selecionar Imagem",
        on_click=on_select_image,
    )

    connect_webcam_button = ft.ElevatedButton(
        text="Conectar Webcam",
        on_click=on_connect_webcam,
    )
    identificador = ft.TextField(label="Identificador")
    nome = ft.TextField(label="Nome")
    edition = ft.TextField(label="Edição")

    points = ft.TextField(value="-1", text_align=ft.TextAlign.RIGHT, width=100)
    points.disabled = True

    def button_clicked():
        blockchain.add_block(
            Block(1, time.time(), blockchain.get_latest_block().hash,
                  f"Candidato: '{identificador.value}', '{nome.value}', '{edition.value}', {points.value}"))

    submit_block = ft.ElevatedButton(
        text="Criar Bloco",
        on_click=lambda _: button_clicked(),
    )

    return ft.View(
        "/",
        [
            ft.AppBar(
                title=ft.Text("UENEM"),
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.ElevatedButton(
                        "Visualizar Blocos",
                        on_click=lambda _: page.go("/blocos"),
                    ),
                ],
            ),
            ft.Row(
                [
                    # Primeira coluna com o card e os botões
                    ft.Column(
                        [
                            ft.Card(
                                width=400,
                                height=400,
                                elevation=30,
                                content=ft.Container(
                                    bgcolor=ft.colors.WHITE24,
                                    padding=10,
                                    border_radius=ft.border_radius.all(20),
                                    content=ft.Column([
                                        image_display,
                                    ]),
                                )
                            ),
                            ft.Row(
                                [
                                    select_image_button,
                                    connect_webcam_button,
                                ],
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    # Segunda coluna com os TextFields
                    ft.Column(
                        [
                            ft.Card(
                                content=ft.Container(
                                    bgcolor=ft.colors.WHITE24,
                                    padding=6,
                                    border_radius=ft.border_radius.all(20),
                                    content=identificador,
                                )
                            ),
                            ft.Card(
                                content=ft.Container(
                                    bgcolor=ft.colors.WHITE24,
                                    padding=6,
                                    border_radius=ft.border_radius.all(20),
                                    content=nome,
                                )
                            ),
                            ft.Card(
                                content=ft.Container(
                                    bgcolor=ft.colors.WHITE24,
                                    padding=6,
                                    border_radius=ft.border_radius.all(20),
                                    content=edition,
                                )
                            ),
                            ft.Row([ft.Card(
                                content=ft.Container(
                                    bgcolor=ft.colors.WHITE24,
                                    padding=6,
                                    border_radius=ft.border_radius.all(20),
                                    content=ft.Row([
                                        ft.Text("Pontos:"),
                                        points,
                                    ]), )
                            ),
                                submit_block,
                            ]
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
    )
