import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de cadastro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    name_label = ft.Text("Digite seu nome:", size=16, width="bold")
    name_field = ft.TextField(width=400)
    
    email_label = ft.Text("Digite seu email:", size=16, width="bold")
    email_field = ft.TextField(width=400)
    
    message_label = ft.Text("Digite sua mensagem:", size=16, width="bold")
    message_field = ft.TextField(multiline=True, width=400, height=150)
    
    def send_form(e):
        if name_field.value and email_field.value and message_field.value:
            confirmation_message.value = "Formulário enviado com sucesso!"
            confirmation_message.color = "Green"
            
            name_field.value = ""
            email_field.value = ""
            message_field.value = ""
        else:
            confirmation_message.value = "Por favor, preencha todos os campos!"
            confirmation_message.color = "Red"
        page.update()
        
    confirmation_message = ft.Text("")
    send_button = ft.ElevatedButton(
        text="Enviar", 
        on_click=send_form,
        icon_color="white100",
        width=200, height= 50
    )
    
    central_form = ft.Column(
        [
            name_label,
            name_field,
            email_label,
            email_field,
            message_label,
            message_field,
            send_button,
            confirmation_message,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    page.add(central_form)

ft.app(target=main)