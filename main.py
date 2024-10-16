import flet as ft
from flet_route import Routing, path

from sturdy_palm_tree.views import (
    index,
    login,
    polls,
    audit,
    poll,
    student,
    students,
)


def main(page: ft.Page):
    page.title = "sturdy-palm-tree"
    app_routes = [
        path(
            url="/",
            clear=True,
            view=index
        ),
        path(
            url="/login",
            clear=True,
            view=login
        ),
        path(
            url="/polls",
            clear=True,
            view=polls
        ),
        path(
            url="/students",
            clear=True,
            view=students
        ),
        path(
            url="/student/:sid",
            clear=True,
            view=student
        ),
        path(
            url="/audit/:s_id",
            clear=True,
            view=audit
        ),
        path(
            url="/",
            clear=True,
            view=index
        ),
    ]

    Routing(
        page=page,
        app_routes=app_routes
    )

    if not page.session.contains_key("is_auth"):
        page.go(route="/login")
    else:
        page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
