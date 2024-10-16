import reflex as rx


def polls():
    return {"route": "/polls", "component": rx.container(rx.heading("Polls page"))}
