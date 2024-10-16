import reflex as rx

from sturdy_palm_tree.src.polls import AuditPoll

class AuditPollState(rx.State):
    def handle(self, data: dict):
        poll = {key: getattr(AuditPoll, f"{key.capitalize()}Enum").get_value_by_text(
            poll=getattr(AuditPoll, f"{key.capitalize()}Enum"), text=data[key]) for key in data}


def audit():
    fields = AuditPoll.get_fields()
    form = []

    for key in fields:
        stack = [rx.heading(fields[key].title)]
        radios = []
        for val in fields[key].annotation:
            radios.append(val.value.text)
        stack.append(rx.radio(radios, required=True, name=key))
        form.append(rx.vstack(*stack))

    return {
        "route": "/audit",
        "component": rx.container(
            rx.vstack(
                rx.form(
                    *form,
                    rx.button("Отправить", type="submit"),
                    on_submit=AuditPollState.handle,
                    reset_on_submit=True,
                ),
            )
        )
    }
