import flet as ft
from home_page import home_page
from blocos_page import blocos_page
from Blockchain.blockchain import Block, Blockchain


def main(page: ft.Page):
    page.title = "UENEM"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 760
    page.window_height = 580
    page.window_resizable = False
    page.window_maximizable = False

    blockchain = Blockchain(4)

    def mudar_rota(rota):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_page(page, blockchain))
        elif page.route == "/blocos":
            page.views.append(blocos_page(page, blockchain))
        page.update()

    def voltar_view(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = mudar_rota
    page.on_view_pop = voltar_view
    page.go(page.route)


ft.app(target=main)
