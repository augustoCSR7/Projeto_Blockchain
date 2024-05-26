import flet as ft

def format_block(block):
    return ft.Text(
        f"Index: {block.index}\n"
        f"Timestamp: {block.timestamp}\n"
        f"Previous Hash: {block.previous_hash}\n"
        f"Data: {block.data}\n"
        f"Nonce: {block.nonce}\n"
        f"Hash: {block.hash}\n"
    )

def blocos_page(page: ft.Page, blockchain):
    formatted_blocks = [format_block(block) for block in blockchain.chain]

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
            spacing=10,
            controls=formatted_blocks,
        )
    ]

    return ft.View("/blocos", view_content)