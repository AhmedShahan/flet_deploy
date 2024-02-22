import flet as ft

def main(pg:ft.Page):
    pg.title="Increment Decrement App"
    pg.theme_mode="dark"
    pg.bgcolor=ft.colors.BROWN_900
    pg.horizontal_alignment=ft.MainAxisAlignment.CENTER
    pg.window_max_height="500"
    pg.window_max_width="500"
    pg.vertical_alignment=ft.MainAxisAlignment.CENTER
    # pg.add(ft.Text("Increment Decrement App", size=30, text_align=ft.MainAxisAlignment.CENTER))

    def Plus(r):
        text.value=text.value+1
        pg.update()
    
    def minous(e):
        text.value=text.value-1
        pg.update()

    text=ft.Text(value=1,size=20)
    buttonMinous=ft.IconButton(icon=ft.icons.REMOVE, bgcolor="red",animate_offset=2, on_click=minous)
    buttonPlus=ft.IconButton(icon=ft.icons.ADD, bgcolor="green",animate_offset=2, on_click=Plus)

    # pg.add(buttonMinous)
    # pg.add(text)
    # pg.add(buttonPlus)
    pg.add(
        ft.Row(controls=[buttonPlus, text, buttonMinous], alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )
ft.app(target=main)