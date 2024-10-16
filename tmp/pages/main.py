import reflex as rx

from sturdy_palm_tree.appstate import auth_required


def main_page():
    return {
        "route": "/main",
        "component": rx.container(
            rx.heading("Main page"),
            rx.container(
                rx.vstack(
                    rx.container(
                        rx.button(
                            "Студенты",
                            on_click=lambda: rx.redirect("/students")
                        ),
                    ),
                    rx.container(
                        rx.button(
                            "Опросы",
                            on_click=lambda: rx.redirect("/polls")
                        ),
                    )
                )
            )
        )
    }
