import flet as ft


def get_pie_chart(data: list[dict[str, str | int | float]]) -> ft.PieChart:
    return ft.PieChart(
        sections=[
            ft.PieChartSection(
                value=item["value"],
                title=item["title"],
                radius=10,
                border_side=ft.BorderSide(0, ft.colors.with_opacity(0, ft.colors.WHITE)),
                color=ft.colors.random_color()
            )
            for item in data
        ]
    )


def get_col_chart(title: str, data: list[dict[str, str | int | float]]) -> ft.BarChart:
    return ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x=item[0],
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=item[1]["value"],
                        tooltip=item[1]["value"],
                        border_radius=0,
                    )
                ],
            )
            for item in enumerate(data)
        ],
        border=ft.border.all(1, ft.colors.GREY_400),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=item[0], label=ft.Container(ft.Text(item[1]["title"]), padding=5)
                )
                for item in enumerate(data)
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text(title), title_size=40
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        interactive=True,
        expand=True,
        width=50,
    )
