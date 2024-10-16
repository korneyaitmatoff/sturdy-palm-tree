import flet as ft


def auth_required(func):
    def wrapper(page: ft.Page, *args, **kwargs):
        print(kwargs)
        if not page.session.contains_key("is_auth"):
            return page.go(route="/login")
        else:
            return func(page, *args, **kwargs)

    return wrapper
