# Interface do organizador de eventos (Flet).
# Dark mode simples: formulário + cálculo da divisão da conta.

import flet as ft

from planner import calcular_valor_por_pessoa


def main(page: ft.Page):
    # --- Janela e página ---
    page.title = "Event Planner"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#111827"  # fundo geral (cinza escuro)
    page.padding = 20

    # Tamanho inicial da janela (app desktop); limites mínimos ao redimensionar.
    page.window.width = 900
    page.window.height = 620
    page.window.min_width = 700
    page.window.min_height = 500

    # --- Cabeçalho do formulário ---
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

    # --- Campos (valores digitados ficam em .value) ---
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

    # Mensagem de saída após clicar em "Calcular divisao".
    resultado = ft.Text("", size=16, color="#93C5FD")

    def calcular(_):
        # Divide o valor total pelo número de pessoas.
        # Aceita vírgula como separador decimal (ex.: "50,50").
        try:
            total = float(valor_total.value.replace(",", "."))
            qtd = int(qtd_pessoas.value)
            por_pessoa = calcular_valor_por_pessoa(total, qtd)
            resultado.value = f"Cada pessoa paga: R$ {por_pessoa:.2f}"
        except Exception:
            resultado.value = "Preencha valor total e quantidade corretamente."
        page.update()  # atualiza a tela com o novo texto do resultado

    # --- Card: agrupa título, campos e botão em um bloco com borda ---
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


# Só inicia a janela quando você roda: python app.py
# (importar este arquivo não abre o app).
if __name__ == "__main__":
    ft.run(main)
