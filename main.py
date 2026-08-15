from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ZoroAI(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="⚔️ ZORO AI",
            font_size=30,
            size_hint_y=None,
            height=60
        )

        self.chat = Label(
            text="Zoro AI ready!\n\nApna message type karo.",
            font_size=18
        )

        self.input_box = TextInput(
            hint_text="Message likho...",
            multiline=False,
            size_hint_y=None,
            height=55
        )

        button = Button(
            text="SEND",
            size_hint_y=None,
            height=55
        )

        button.bind(on_press=self.send_message)

        layout.add_widget(title)
        layout.add_widget(self.chat)
        layout.add_widget(self.input_box)
        layout.add_widget(button)

        return layout

    def send_message(self, instance):
        message = self.input_box.text.strip()

        if message:
            self.chat.text = "You: " + message + "\n\nZoro: Message received! ⚔️"
            self.input_box.text = ""


if __name__ == "__main__":
    ZoroAI().run()
