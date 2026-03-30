import flet as ft


def main(page: ft.Page):
    page.title = "Event Planner"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#111827"
    page.padding = 20

    page.window.width = 900
    page.window.height = 620
    page.window.min_width = 700
    page.window.min_height = 500

    titulo = ft.Text(
        "Event Planner",
        size=28,
        weight=ft.FontWeight.BOLD,
        color="#F9FAFB",
    )

    subtitulo = ft.Text(
        "Preencha os dados do evento",
        size=14,
        color="#9CA3AF",
    )

    nome_evento = ft.TextField(
        label="Nome do evento",
        bgcolor="#1F2937",
        border_color="#374151",
        color="#F9FAFB",
    )
    local_evento = ft.TextField(
        label="Local",
        bgcolor="#1F2937",
        border_color="#374151",
        color="#F9FAFB",
    )
    convidados = ft.TextField(
        label="Convidados (separados por virgula)",
        multiline=True,
        min_lines=2,
        max_lines=4,
        bgcolor="#1F2937",
        border_color="#374151",
        color="#F9FAFB",
    )
    valor_total = ft.TextField(
        label="Valor total (R$)",
        keyboard_type=ft.KeyboardType.NUMBER,
        bgcolor="#1F2937",
        border_color="#374151",
        color="#F9FAFB",
    )
    qtd_pessoas = ft.TextField(
        label="Quantidade de pessoas",
        keyboard_type=ft.KeyboardType.NUMBER,
        bgcolor="#1F2937",
        border_color="#374151",
        color="#F9FAFB",
    )

    resultado = ft.Text("", size=16, color="#93C5FD")

    def calcular(_):
        try:
            total = float(valor_total.value.replace(",", "."))
            qtd = int(qtd_pessoas.value)
            if qtd <= 0:
                raise ValueError
            por_pessoa = total / qtd
            resultado.value = f"Cada pessoa paga: R$ {por_pessoa:.2f}"
        except Exception:
            resultado.value = "Preencha valor total e quantidade corretamente."
        page.update()

    card = ft.Container(
        content=ft.Column(
            [
                titulo,
                subtitulo,
                ft.Divider(color="#374151"),
                nome_evento,
                local_evento,
                convidados,
                ft.Row([valor_total, qtd_pessoas], spacing=12),
                ft.ElevatedButton("Calcular divisao", on_click=calcular),
                resultado,
            ],
            spacing=12,
        ),
        padding=20,
        border_radius=12,
        bgcolor="#0F172A",
        border=ft.border.all(1, "#374151"),
    )

    page.add(card)


if __name__ == "__main__":
    ft.app(target=main)
