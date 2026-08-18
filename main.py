from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import datetime
import webbrowser

class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        
        self.label = Label(text="Jarvis: Ready, Sir!", size_hint_y=0.7, font_size='18sp')
        self.add_widget(self.label)
        
        self.input_text = TextInput(hint_text="Type: jarvis open youtube", multiline=False, size_hint_y=0.15)
        self.add_widget(self.input_text)
        
        self.btn = Button(text="Send Command", size_hint_y=0.15, background_color=(0, 0.5, 1, 1))
        self.btn.bind(on_press=self.process_command)
        self.add_widget(self.btn)

    def process_command(self, instance):
        query = self.input_text.text.lower()
        self.input_text.text = ""
        
        if 'jarvis' in query:
            command = query.replace("jarvis", "").strip()

            if 'hi' in command or 'hello' in command:
                self.label.text = "Jarvis: Hello Sir! How can I assist you?"
            elif 'the time' in command:
                now = datetime.datetime.now().strftime('%H:%M:%S')
                self.label.text = f"Jarvis: Sir, time is {now}"
            elif 'open youtube' in command:
                self.label.text = "Jarvis: Opening YouTube..."
                webbrowser.open("https://www.youtube.com")
            elif 'open google' in command:
                self.label.text = "Jarvis: Opening Google..."
                webbrowser.open("https://www.google.com")
            else:
                self.label.text = f"Jarvis: Searching Google for {command}..."
                webbrowser.open(f"https://www.google.com/search?q={command}")
        else:
            self.label.text = "Jarvis: Please start command with 'jarvis'"

class JarvisApp(App):
    def build(self):
        return JarvisUI()

if __name__ == '__main__':
    JarvisApp().run()
