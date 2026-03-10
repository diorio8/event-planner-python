import flet as ft

def main(page: ft.Page):
    # Aqui a gente define o nome que aparece na barra da janela
    page.title = "Meu Primeiro App - Vitoria"
    
    # Vamos mudar o tema para escuro (mais bonito!)
    page.theme_mode = ft.ThemeMode.DARK
    
    # Adicionando um texto e um botão só para testar
    page.add(
        ft.Text("O Organizador de Rolês está nascendo!", size=30, color="blue"),
        ft.ElevatedButton("Clique aqui para começar")
    )

# Esse comando aqui embaixo é o que dá o 'play' no app
ft.app(target=main)