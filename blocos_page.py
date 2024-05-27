import flet as ft
import time
from datetime import datetime

def format_block(block):
    # Converte o timestamp em segundos para um objeto datetime
    timestamp_int = int(block.timestamp)
    dt_object = datetime.fromtimestamp(timestamp_int)

    return ft.Card(
        content=ft.Container(
            bgcolor=ft.colors.WHITE24,
            padding=6,
            border_radius=ft.border_radius.all(20),
            content=ft.Text(
                f"Index: {block.get_index()}\n"
                f"Timestamp: {dt_object.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Previous Hash: {block.previous_hash}\n"
                f"Data: {block.data}\n"
                f"Nonce: {block.nonce}\n"
                f"Hash: {block.hash}\n"
            ),
        )
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
