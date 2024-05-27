import flet as ft
import base64
import cv2
from tkinter import filedialog
import tkinter as tk
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
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    root.destroy()  # Destroi a janela do Tkinter após selecionar o arquivo
    return file_path


gabarito = None


def home_page(page: ft.Page, blockchain):
    def on_select_image(e):
        global gabarito
        file_path = open_file_dialog()
        if file_path:  # Verificar se um arquivo foi selecionado
            image_display.update_image(file_path)
            points.value, gabarito = processar_imagem(file_path)

            page.update()

    def abrir_gabarito_cv(e):
        global gabarito
        if gabarito is not None:
            cv2.imshow('Gabarito', gabarito)
            key = cv2.waitKey(0)
            cv2.destroyAllWindows()

    image_display = ImageDisplay()

    select_image_button = ft.ElevatedButton(
        text="Selecionar Imagem",
        on_click=on_select_image,
    )

    abrir_gabarito = ft.ElevatedButton(
        text="Abrir Gabarito",
        on_click=abrir_gabarito_cv,
    )
    identificador = ft.TextField(label="Identificador")
    nome = ft.TextField(label="Nome")
    edition = ft.TextField(label="Edição")

    points = ft.TextField(value="-1", text_align=ft.TextAlign.RIGHT, width=100)
    points.disabled = True

    def button_clicked():
        if points.value == "-1" or len(identificador.value) == 0 or len(nome.value) == 0 or len(edition.value) == 0:
            pass
        else:
            data = f"'{identificador.value}', '{nome.value}', '{edition.value}', {points.value}"
            block = blockchain.new_block(data)
            if blockchain.is_valid_new_block(block, blockchain.get_latest_block()):
                blockchain.add_block(block)
                page.go("/blocos")

    submit_block = ft.ElevatedButton(
        text="Criar Bloco",
        on_click=lambda _: button_clicked(),
    )

    return ft.View(
        "/",
        [
            ft.AppBar(
                title=ft.Text("Início"),
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
                                    abrir_gabarito,
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
