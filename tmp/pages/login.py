import reflex as rx

from sturdy_palm_tree.src.components.auth_form import AUTH_FORM


def login():
    return {
        "route": "/login",
        "component": rx.container(rx.heading("Login page"), AUTH_FORM),
    }
