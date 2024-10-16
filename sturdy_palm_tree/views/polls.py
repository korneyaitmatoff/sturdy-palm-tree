import flet as ft
from flet_route import Basket, Params

from sturdy_palm_tree import auth_required
from sturdy_palm_tree.components import bottom_bar, poll_table


@auth_required
def polls(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        route="/polls",
        controls=[
            bottom_bar(page=page),
            poll_table(page=page)
        ]
    )
