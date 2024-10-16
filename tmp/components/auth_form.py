from os import getenv

import reflex as rx
from dotenv import load_dotenv

from sturdy_palm_tree.appstate import AppState

load_dotenv()


class FormState(rx.State):
    form_data: dict = {}
    success: bool = False
    message: str = ""

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.message = ""

        if getenv("admin_login") == form_data["login"] and getenv("admin_password") == form_data["password"]:
            AppState.is_login = True

            return rx.redirect(path="/main")
        else:
            self.message = "Неверные логин или пароль"

            return rx.redirect(path="/login")


AUTH_FORM = rx.vstack(
    rx.form(
        rx.vstack(
            rx.input(
                placeholder="login",
                name="login",
                required=True,
            ),
            rx.input(
                placeholder="password",
                name="password",
                type="password",
                required=True,
            ),
            rx.button("Submit", type="submit"),
            align="center",
        ),
        on_submit=FormState.handle_submit,
        reset_on_submit=True,
    ),
    rx.divider(),
    rx.card(rx.text(FormState.message)),
)
