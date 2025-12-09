"""
Простое приложение для заметок
"""

import os
import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class NotesApp(App):
    def build(self):
        # Файл для хранения заметок
        self.notes_file = "notes.txt"
        
        # Основной макет
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Устанавливаем фон
        with layout.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # Светло-серый фон
            self.rect = Rectangle(size=Window.size, pos=layout.pos)
        
        # Заголовок
        title = Label(
            text="📝 Мои Заметки",
            font_size='28sp',
            size_hint=(1, 0.1),
            bold=True,
            color=(0.2, 0.2, 0.2, 1)
        )
        
        # Поле для ввода новой заметки
        self.text_input = TextInput(
            hint_text="Напишите вашу заметку здесь...",
            size_hint=(1, 0.3),
            multiline=True,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=[10, 10]
        )
        
        # Кнопки
        buttons_layout = BoxLayout(size_hint=(1, 0.08), spacing=5)
        
        save_btn = Button(
            text="Сохранить",
            background_color=(0.3, 0.7, 0.3, 1),
            background_normal=''
        )
        save_btn.bind(on_press=self.save_note)
        
        clear_btn = Button(
            text="Очистить",
            background_color=(0.8, 0.3, 0.3, 1),
            background_normal=''
        )
        clear_btn.bind(on_press=self.clear_input)
        
        buttons_layout.add_widget(save_btn)
        buttons_layout.add_widget(clear_btn)
        
        # Область для отображения заметок
        scroll = ScrollView(size_hint=(1, 0.5))
        self.notes_container = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None
        )
        self.notes_container.bind(minimum_height=self.notes_container.setter('height'))
        scroll.add_widget(self.notes_container)
        
        # Собираем интерфейс
        layout.add_widget(title)
        layout.add_widget(self.text_input)
        layout.add_widget(buttons_layout)
        
        # Статус
        self.status_label = Label(
            text="Все заметки:",
            size_hint=(1, 0.05),
            font_size='16sp',
            color=(0.3, 0.3, 0.3, 1)
        )
        layout.add_widget(self.status_label)
        layout.add_widget(scroll)
        
        # Загружаем существующие заметки
        self.load_and_display_notes()
        
        return layout
    
    def save_note(self, instance):
        """Сохраняет новую заметку"""
        note_text = self.text_input.text.strip()
        
        if not note_text:
            self.status_label.text = "Ошибка: заметка пустая!"
            self.status_label.color = (1, 0, 0, 1)
            return
        
        try:
            # Добавляем дату
            timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
            note_with_date = f"[{timestamp}] {note_text}"
            
            # Сохраняем в файл
            with open(self.notes_file, 'a', encoding='utf-8') as f:
                f.write(note_with_date + "\n---\n")
            
            # Очищаем поле и обновляем список
            self.text_input.text = ""
            self.load_and_display_notes()
            
            self.status_label.text = f"Заметка сохранена! Всего: {self.count_notes()}"
            self.status_label.color = (0, 0.5, 0, 1)
            
        except Exception as e:
            self.status_label.text = f"Ошибка сохранения: {str(e)}"
            self.status_label.color = (1, 0, 0, 1)
    
    def clear_input(self, instance):
        """Очищает поле ввода"""
        self.text_input.text = ""
        self.status_label.text = "Поле очищено"
        self.status_label.color = (0.5, 0.5, 0.5, 1)
    
    def load_and_display_notes(self):
        """Загружает и отображает все заметки"""
        self.notes_container.clear_widgets()
        
        if not os.path.exists(self.notes_file):
            # Если файла нет, создаем его
            with open(self.notes_file, 'w', encoding='utf-8') as f:
                f.write("")
            
            empty_label = Label(
                text="Заметок пока нет.\nДобавьте первую!",
                size_hint_y=None,
                height=100,
                color=(0.5, 0.5, 0.5, 1),
                font_size='18sp',
                halign='center'
            )
            empty_label.bind(size=empty_label.setter('text_size'))
            self.notes_container.add_widget(empty_label)
            return
        
        try:
            with open(self.notes_file, 'r', encoding='utf-8') as f:
                notes_content = f.read()
            
            if not notes_content.strip():
                empty_label = Label(
                    text="Заметок пока нет.\nДобавьте первую!",
                    size_hint_y=None,
                    height=100,
                    color=(0.5, 0.5, 0.5, 1),
                    font_size='18sp'
                )
                self.notes_container.add_widget(empty_label)
                return
            
            # Разделяем заметки
            notes = [n.strip() for n in notes_content.split('---') if n.strip()]
            
            for note in reversed(notes):  # Новые заметки сверху
                if note:
                    note_label = Label(
                        text=note,
                        size_hint_y=None,
                        height=80,
                        text_size=(Window.width - 40, None),
                        halign='left',
                        valign='top',
                        color=(0.1, 0.1, 0.1, 1),
                        font_size='16sp',
                        padding=[10, 10]
                    )
                    note_label.bind(size=note_label.setter('text_size'))
                    
                    # Фон для заметки
                    with note_label.canvas.before:
                        Color(1, 1, 1, 1)  # Белый фон
                        Rectangle(
                            pos=(note_label.x + 5, note_label.y + 5),
                            size=(note_label.width - 10, note_label.height - 10)
                        )
                    
                    self.notes_container.add_widget(note_label)
                    
            # Обновляем статус
            self.status_label.text = f"Все заметки: {len(notes)}"
            self.status_label.color = (0, 0, 0, 1)
            
        except Exception as e:
            error_label = Label(
                text=f"Ошибка загрузки заметок:\n{str(e)}",
                size_hint_y=None,
                height=60,
                color=(1, 0, 0, 1)
            )
            self.notes_container.add_widget(error_label)
    
    def count_notes(self):
        """Считает количество заметок"""
        if not os.path.exists(self.notes_file):
            return 0
        
        try:
            with open(self.notes_file, 'r', encoding='utf-8') as f:
                content = f.read()
            notes = [n for n in content.split('---') if n.strip()]
            return len(notes)
        except:
            return 0

if __name__ == '__main__':
    NotesApp().run()