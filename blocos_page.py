import flet as ft
from datetime import datetime
from contracts import buscar_todos_os_alunos
from utils import pinata_receive

def format_block(aluno):
    return ft.Card(
        content=ft.Container(
            bgcolor=ft.colors.WHITE,
            padding=16,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(1, color=ft.colors.BLACK12),  # Usando cor básica para a borda
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src_base64=pinata_receive(aluno[4]),
                            width=150,
                            height=150,
                            #fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.all(8)
                        ),
                        margin=ft.margin.only(right=12)  # Ajuste da margem com um contêiner
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                f"ID: {aluno[0]}",
                                weight=ft.FontWeight.BOLD,
                                size=18,
                                color=ft.colors.BLACK
                            ),
                            ft.Text(
                                f"Nome: {aluno[1]}",
                                size=16,
                                color=ft.colors.BLACK
                            ),
                            ft.Text(
                                f"Edição: {aluno[2]}",
                                size=16,
                                color=ft.colors.BLACK
                            ),
                            ft.Text(
                                f"Pontos: {aluno[3]}",
                                size=16,
                                color=ft.colors.BLACK
                            ),
                            # ft.Text(
                            #     f"Hash: {aluno[4]}",
                            #     size=14,
                            #     color=ft.colors.GRAY
                            # ),
                        ],
                        spacing=4
                    )
                ],
                alignment=ft.MainAxisAlignment.START
            )
        ),
        margin=ft.margin.only(bottom=16),
        width=600  # Definindo uma largura fixa em pixels
    )

def blocos_page(page: ft.Page):
    alunos = buscar_todos_os_alunos()

    # Formatar os alunos em blocos
    formatted_blocks = [format_block(aluno) for aluno in alunos]

    # Definir o conteúdo da página
    view_content = [
        ft.AppBar(
            title=ft.Text("Blocos"),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.ElevatedButton(
                    "Início",
                    on_click=lambda _: page.go("/"),
                ),
            ],
        ),
        ft.ListView(
            expand=True,
            spacing=16,
            controls=formatted_blocks,
            padding=16
        )
    ]

    return ft.View("/blocos", view_content)