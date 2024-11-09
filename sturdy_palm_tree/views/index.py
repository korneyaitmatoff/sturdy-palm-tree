import flet as ft
from flet_route import Basket, Params

from sturdy_palm_tree import auth_required
from sturdy_palm_tree.components import bottom_bar, get_pie_chart, get_col_chart

from sturdy_palm_tree.src.api.depends import students_service

@auth_required
def index(page: ft.Page, params: Params, basket: Basket):
    pie_chart = get_pie_chart(
        data=[
            {
                "title": "50% склонны к алкоголизму",
                "value": 50,
            },
            {
                "title": "50% находятся вне зоне риска",
                "value": 50,
            },
        ]
    )

    chart = get_col_chart(
        title="LEFT AXIS",
        data=[
            {
                "title": "pepe",
                "value": 10,
            },
            {
                "title": "pepe",
                "value": 20,
            },
            {
                "title": "pepe",
                "value": 30,
            },
            {
                "title": "pepe",
                "value": 140,
            },
        ])

    get_avg_audit_group_by_dates_chart = get_col_chart(
        title="Динамика среднего балла шкалы AUDIT",
        data=students_service.get_avg_audit_group_by_dates()
    )

    get_students_group_by_stress_chart = get_col_chart(
        title="Влияние стресса на алкоголизм.\n Риск алкоголизма, %",
        data=students_service.get_students_group_by_stress()
    )

    get_students_group_by_perf_chart = get_col_chart(
        title="Зависимость риска алкоголзима от успеваемости",
        data=students_service.get_students_group_by_perf()
    )

    get_students_group_by_age_chart = get_col_chart(
        title="Влияние возраста на алкоголизм. Возрастные группы.",
        data=students_service.get_students_group_by_age()
    )

    get_students_group_by_gender_chart = get_col_chart(
        title="Соотношение студентов в зоне риска по половому признаку.",
        data=students_service.get_students_group_by_gender()
    )

    get_students_group_by_alco_depends_chart = get_col_chart(
        title="Кол-во студентов, находящихся в разных группах риска",
        data=students_service.get_students_group_by_alco_depends()
    )

    return ft.View(
        route="/",
        controls=[
            ft.Row(
                controls=[get_avg_audit_group_by_dates_chart],
                alignment=ft.alignment.center
            ),
            ft.Row(
                controls=[get_students_group_by_stress_chart],
                alignment=ft.alignment.center
            ),
            ft.Row(
                controls=[get_students_group_by_perf_chart],
                alignment=ft.alignment.center
            ),
            ft.Row(
                controls=[get_students_group_by_age_chart],
                alignment=ft.alignment.center
            ),
            ft.Row(
                controls=[get_students_group_by_gender_chart],
                alignment=ft.alignment.center
            ),
            ft.Row(
                controls=[get_students_group_by_alco_depends_chart],
                alignment=ft.alignment.center
            ),
        ],
        scroll=ft.ScrollMode.ALWAYS,
        bottom_appbar=bottom_bar(page=page),
        spacing=100,
        padding=30
    )
