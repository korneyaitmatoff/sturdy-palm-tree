import flet as ft
from flet_route import Basket, Params

from sturdy_palm_tree import auth_required


@auth_required
def poll(page: ft.Page, params: Params, basket: Basket):
    print(params)
    print(basket)

    return ft.View(
        route="/poll",
        controls=[
            ft.Text("poll")
        ]
    )
