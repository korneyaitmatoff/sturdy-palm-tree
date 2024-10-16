import reflex as rx


class AppState(rx.State):
    """App state"""

    is_login = False


def auth_required(func):
    def wrapper(*args, **kwargs):
        try:
            print(AppState.is_login)
            if not AppState.is_login:
                rx.redirect("/login")
            return func(*args, **kwargs)
        except TypeError as e:
            print(e)

    return wrapper
