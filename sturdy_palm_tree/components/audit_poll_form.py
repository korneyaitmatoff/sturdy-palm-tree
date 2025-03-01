import flet as ft

from config import db_config
from sturdy_palm_tree.src.api.service import AuditPollService
from sturdy_palm_tree.src.api.core import tables
from sturdy_palm_tree.src.api.models import AuditPoll


def audit_poll_form(page: ft.Page, s_id: int):
    def _onclick(e):
        if None in (
                field_1.value,
                field_2.value,
                field_3.value,
                field_4.value,
                field_5.value,
                field_6.value,
                field_7.value,
                field_8.value,
                field_9.value,
                field_10.value,
        ):
            page.snack_bar = ft.SnackBar(ft.Text("Заполните все поля"))
            page.snack_bar.open = True
        else:
            AuditPollService(table=tables.AuditPolls, **db_config).create(
                data=dict(
                    AuditPoll(
                        field_1=int(field_1.value),
                        field_2=int(field_2.value),
                        field_3=int(field_3.value),
                        field_4=int(field_4.value),
                        field_5=int(field_5.value),
                        field_6=int(field_6.value),
                        field_7=int(field_7.value),
                        field_8=int(field_8.value),
                        field_9=int(field_9.value),
                        field_10=int(field_10.value),
                        s_id=int(s_id),
                    )
                )
            )

            page.snack_bar = ft.SnackBar(ft.Text("Опрос был отправлен"))
            page.snack_bar.open = True
            btn.disabled = True
            btn.text = "Опрос отправлен"

        page.update()

    return ft.Container(
        ft.Column(
            controls=[
                field_1 := ft.Dropdown(
                    width=700,
                    label="Как часто Вы употребляете алкогольные напитки?",
                    options=[
                        ft.dropdown.Option(text="Никогда", key="0"),
                        ft.dropdown.Option(text="Раз в месяц или реже", key="1"),
                        ft.dropdown.Option(text="2-4 раза в месяц", key="2"),
                        ft.dropdown.Option(text="2-3 раза в неделю", key="3"),
                        ft.dropdown.Option(text="4 раза в неделю и чаще", key="4"),
                    ],
                ),
                field_2 := ft.Dropdown(
                    width=700,
                    label="Сколько алкогольных напитков (стандартных порций) Вы употребляете в типичный день, когда "
                          "выпиваете?",
                    options=[
                        ft.dropdown.Option(text="1 или 2 стандартных порции", key="0"),
                        ft.dropdown.Option(text="3 или 4 стандартных порции", key="1"),
                        ft.dropdown.Option(text="5 или 6 стандартных порций", key="2"),
                        ft.dropdown.Option(text="7 или 9 стандартных порций", key="3"),
                        ft.dropdown.Option(
                            text="10 или более стандартных порций", key="4"
                        ),
                    ],
                ),
                field_3 := ft.Dropdown(
                    width=700,
                    label="Как часто Вы употребляете как минимум 1,5 л пива, или как минимум 180 мл крепкого алкоголя, "
                          "или как минимум бутылку вина или шампанского (750 мл) в течение 24 часов?",
                    options=[
                        ft.dropdown.Option(text="Никогда", key="0"),
                        ft.dropdown.Option(text="Реже одного раза в месяц", key="1"),
                        ft.dropdown.Option(text="Ежемесячно", key="2"),
                        ft.dropdown.Option(text="Еженедельно", key="3"),
                        ft.dropdown.Option(
                            text="Ежедневно или почти ежедневно", key="4"
                        ),
                    ],
                ),
                field_4 := ft.Dropdown(
                    width=700,
                    label="Как часто за последние 12 месяцев Вы не смогли остановиться, начав употреблять алкогольные напитки?",
                    options=[
                        ft.dropdown.Option(text="Никогда", key="0"),
                        ft.dropdown.Option(text="Менее, чем 1 раз в месяц", key="1"),
                        ft.dropdown.Option(text="1 раз в месяц (ежемесячно)", key="2"),
                        ft.dropdown.Option(
                            text="1 раз в неделю (еженедельно)", key="3"
                        ),
                        ft.dropdown.Option(
                            text="Ежедневно или почти ежедневно", key="4"
                        ),
                    ],
                ),
                field_5 := ft.Dropdown(
                    width=700,
                    label="Как часто за последние 12 месяцев из-за выпивки Вы не сделали то, что от Вас обычно ожидалось?",
                    options=[
                        ft.dropdown.Option(text="Никогда", key="0"),
                        ft.dropdown.Option(text="Менее, чем 1 раз в месяц", key="1"),
                        ft.dropdown.Option(text="1 раз в месяц (ежемесячно)", key="2"),
                        ft.dropdown.Option(
                            text="1 раз в неделю (еженедельно)", key="3"
                        ),
                        ft.dropdown.Option(
                            text="Ежедневно или почти ежедневно", key="4"
                        ),
                    ],
                ),
                field_6 := ft.Dropdown(
                    width=700,
                    label="Как часто за последние 12 месяцев Вам необходимо было выпить утром, чтобы прийти в себя после выпивки "
                          "(опохмелиться)",
                    options=[
                        ft.dropdown.Option(text="Никогда", key="0"),
                        ft.dropdown.Option(text="Менее, чем 1 раз в месяц", key="1"),
                        ft.dropdown.Option(text="1 раз в месяц (ежемесячно)", key="2"),
                        ft.dropdown.Option(
                            text="1 раз в неделю (еженедельно)", key="3"
                        ),
                        ft.dropdown.Option(
                            text="Ежедневно или почти ежедневно", key="4"
                        ),
                    ],
                ),
                field_7 := ft.Dropdown(
                    width=700,
                    label="Как часто за последние 12 месяцев Вы испытывали чувство вины или сожаления после выпивки?",
                    options=[
                        ft.dropdown.Option(text="Никогда", key="0"),
                        ft.dropdown.Option(text="Менее, чем 1 раз в месяц", key="1"),
                        ft.dropdown.Option(text="1 раз в месяц (ежемесячно)", key="2"),
                        ft.dropdown.Option(
                            text="1 раз в неделю (еженедельно)", key="3"
                        ),
                        ft.dropdown.Option(
                            text="Ежедневно или почти ежедневно", key="4"
                        ),
                    ],
                ),
                field_8 := ft.Dropdown(
                    width=700,
                    label="Как часто за последние 12 месяцев Вы были неспособны вспомнить, что было накануне, из-за того, что Вы "
                          "выпивали?",
                    options=[
                        ft.dropdown.Option(text="Никогда", key="0"),
                        ft.dropdown.Option(text="Менее, чем 1 раз в месяц", key="1"),
                        ft.dropdown.Option(text="1 раз в месяц (ежемесячно)", key="2"),
                        ft.dropdown.Option(
                            text="1 раз в неделю (еженедельно)", key="3"
                        ),
                        ft.dropdown.Option(
                            text="Ежедневно или почти ежедневно", key="4"
                        ),
                    ],
                ),
                field_9 := ft.Dropdown(
                    width=700,
                    label="Являлось ли Ваше употребление алкогольных напитков причиной травмы у Вас или других людей?",
                    options=[
                        ft.dropdown.Option(text="Никогда", key="0"),
                        ft.dropdown.Option(
                            text="Да, но это было более, чем год назад", key="2"
                        ),
                        ft.dropdown.Option(text="Да, в течение этого года", key="4"),
                    ],
                ),
                field_10 := ft.Dropdown(
                    width=700,
                    label="Случалось ли, что Ваш близкий человек или родственник, друг или врач беспокоился насчет употребления "
                          "Вами алкоголя или советовал выпивать меньше?",
                    options=[
                        ft.dropdown.Option(text="Никогда", key="0"),
                        ft.dropdown.Option(
                            text="Да, но это было более, чем год назад", key="2"
                        ),
                        ft.dropdown.Option(text="Да, в течение этого года", key="4"),
                    ],
                ),
                btn := ft.CupertinoButton(text="Отправить", on_click=_onclick),
            ],
            spacing=20,
        ),
        alignment=ft.alignment.center,
    )
