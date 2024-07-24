import flet as ft
from Blockchain.blockchain import buscar_todos_os_alunos, buscar_aluno_por_id, buscar_alunos_por_edicao
from Blockchain.utils import pinata_receive

def format_block(aluno):
    return ft.Card(
        content=ft.Container(
            bgcolor=ft.colors.WHITE,
            padding=16,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(1, color=ft.colors.BLACK12),
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src_base64=pinata_receive(aluno[4]),
                            width=150,
                            height=150,
                            border_radius=ft.border_radius.all(8)
                        ),
                        margin=ft.margin.only(right=12)
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
                        ],
                        spacing=4
                    )
                ],
                alignment=ft.MainAxisAlignment.START
            )
        ),
        margin=ft.margin.only(bottom=16),
        width=600
    )

def blocos_page(page: ft.Page):
    def buscar_por_id(e):
        id = int(input_id.value)
        alunos = buscar_aluno_por_id(id)
        atualizar_lista(alunos)

    def buscar_por_edicao(e):
        edicao = input_edicao.value
        alunos = buscar_alunos_por_edicao(edicao)
        atualizar_lista(alunos)

    def buscar_todos(e):
        alunos = buscar_todos_os_alunos()
        atualizar_lista(alunos)

    def atualizar_lista(alunos):
        formatted_blocks = [format_block(aluno) for aluno in alunos]
        lista_view.controls = formatted_blocks
        page.update()

    input_id = ft.TextField(label="Buscar por ID", width=200)
    btn_buscar_id = ft.ElevatedButton("Buscar", on_click=buscar_por_id)

    input_edicao = ft.TextField(label="Buscar por Edição", width=200)
    btn_buscar_edicao = ft.ElevatedButton("Buscar", on_click=buscar_por_edicao)

    btn_buscar_todos = ft.ElevatedButton("Buscar Todos", on_click=buscar_todos)

    # Buscar todos os alunos inicialmente
    alunos = buscar_todos_os_alunos()
    formatted_blocks = [format_block(aluno) for aluno in alunos]

    lista_view = ft.ListView(
        expand=True,
        spacing=16,
        controls=formatted_blocks,
        padding=16,
        auto_scroll=True
    )

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
        ft.Column(
            controls=[
                ft.Row(
                    controls=[input_id, btn_buscar_id, input_edicao, btn_buscar_edicao],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=16
                ),
                ft.Row(
                    controls=[btn_buscar_todos],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=16
                ),
                lista_view
            ],
            spacing=16,
            expand=True
        )
    ]

    return ft.View("/blocos", view_content)