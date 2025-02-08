import flet as ft

from flet_localisation import FletLocalisation


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Container(
            height=150,
            width=300,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.PURPLE_200,
            content=FletLocalisation(
                tooltip="My new FletLocalisation Control tooltip",
                value="My new FletLocalisation Flet Control",
            ),
        ),
    )


ft.app(main)
