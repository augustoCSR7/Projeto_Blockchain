import flet as ft
from Pages.home_page import home_page
from Pages.blocos_page import blocos_page


def main(page: ft.Page):
    page.title = "UENEM"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 760
    page.window.height = 580
    page.window.resizable = False
    page.window.maximizable = False


    def mudar_rota(rota):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_page(page))
        elif page.route == "/blocos":
            page.views.append(blocos_page(page))
        page.update()

    def voltar_view(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = mudar_rota
    page.on_view_pop = voltar_view
    page.go(page.route)


ft.app(target=main)
