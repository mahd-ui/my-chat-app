import flet as ft

def main(page: ft.Page):
    page.title = "تطبيق دردشة"
    chat = ft.Column()
    new_message = ft.TextField(hint_text="اكتب رسالتك هنا...", expand=True)

    def send_click(e):
        chat.controls.append(ft.Text(new_message.value))
        new_message.value = ""
        page.update()

    page.add(
        ft.Text("مرحباً بك في الدردشة", size=30, weight="bold"),
        chat,
        ft.Row([new_message, ft.ElevatedButton("إرسال", on_click=send_click)])
    )

ft.run(main)
