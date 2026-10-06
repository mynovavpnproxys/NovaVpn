from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class NovaVPN(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="NOVA VPN",
            font_size="32sp",
            bold=True
        )

        status = Label(
            text="وضعیت: آماده اتصال",
            font_size="20sp"
        )

        connect_button = Button(
            text="اتصال سریع",
            font_size="22sp",
            size_hint=(1, 0.25)
        )

        def connect(instance):
            status.text = "وضعیت: اتصال برقرار شد"

        connect_button.bind(on_press=connect)

        layout.add_widget(title)
        layout.add_widget(status)
        layout.add_widget(connect_button)

        return layout


if __name__ == "__main__":
    NovaVPN().run()
