import reflex as rx

from sturdy_palm_tree.src.pages import login, polls, audit, main_page, students
# student
from sturdy_palm_tree.appstate import auth_required, AppState

app = rx.App(state=AppState)

app.add_page(**main_page())
app.add_page(**login())
app.add_page(**polls())
app.add_page(**audit())
app.add_page(**students())


def student():
    return rx.container(rx.heading(f"Student"))


app.add_page(student, route="/student/{student_id}")
