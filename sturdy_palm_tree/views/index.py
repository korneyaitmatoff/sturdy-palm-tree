import flet as ft
from flet_route import Basket, Params

from sturdy_palm_tree import auth_required
from sturdy_palm_tree.components import bottom_bar


@auth_required
def index(page: ft.Page, params: Params, basket: Basket):
    print(params)
    print(basket)

    normal_border = ft.BorderSide(0, ft.colors.with_opacity(0, ft.colors.WHITE))
    hovered_border = ft.BorderSide(6, ft.colors.WHITE)

    pie_chart = ft.PieChart(
        sections=[
            ft.PieChartSection(
                50,
                title="50% склонны к алкоголизму",
                color=ft.colors.RED,
                radius=80,
                border_side=normal_border,
            ),
            ft.PieChartSection(
                50,
                title="50% находятся вне зоне риска",
                color=ft.colors.GREEN,
                radius=70,
                border_side=normal_border,
            ),
        ],
        sections_space=1,
        center_space_radius=0,
        expand=True,
    )

    chart = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=40,
                        width=40,
                        tooltip="01.01.2024",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=100,
                        width=40,
                        tooltip="01.04.2024",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=30,
                        width=40,
                        tooltip="01.07.2024",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=3,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=60,
                        width=40,
                        tooltip="01.10.2024",
                        border_radius=0,
                    ),
                ],
            ),
        ],
        border=ft.border.all(1, ft.colors.GREY_400),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("График прогресса алкоголизма у школьников"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0, label=ft.Container(ft.Text("01.01.2024"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text("01.03.2024"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text("01.07.2024"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=3, label=ft.Container(ft.Text("01.10.2024"), padding=10)
                ),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=110,
        interactive=True,
        expand=True,
    )

    return ft.View(
        route="/",
        controls=[
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("Количество студентов: 10.\nКоличество пройденных опросов: 30"),
                            pie_chart,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            chart
                        ]
                    ),
                ]
            ),
            bottom_bar(page=page)
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
