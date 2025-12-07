import urllib.request
import re

class MyFile:
    def __init__(self, path, mode="read"):
        self.path = path
        self.mode = mode
        self.file = None
        
    def read(self):
        if self.mode != "read":
            raise ValueError("Файл открыт не в режиме чтения")
        
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Ошибка при чтении файла: {e}"
        else:
            raise ValueError("Файл открыт не в режиме чтения")
    def write(self, content):
        if self.mode == "write":
            try:
                with open(self.path, 'w', encoding='utf-8') as file:
                    file.write(content)
                return f"Запись в файл {self.path} выполнена успешно"
            except Exception as e:
                return f"Ошибка при записи в файл: {e}"
        
        elif self.mode == "append":
            try:
                with open(self.path, 'a', encoding='utf-8') as file:
                    file.write(content)
                return f"Добавление в файл {self.path} выполнено успешно"
            except Exception as e:
                return f"Ошибка при добавлении в файл: {e}"
        else:
            raise ValueError("Файл открыт не в режиме записи/добавления")
    
    def read_url(self):
        if self.mode != "url":
            raise ValueError("Объект не инициализирован в режиме URL")
        
        try:
            with urllib.request.urlopen(self.path) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            return f"Ошибка при чтении URL: {e}"
    
    def count_urls(self):
        if self.mode != "url":
            raise ValueError("Объект не инициализирован в режиме URL")
        
        content = self.read_url()
        # Регулярное выражение для поиска URL
        url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        urls = re.findall(url_pattern, content)
        return len(urls)
    
    def write_url(self, filename):
        if self.mode != "url":
            raise ValueError("Объект не инициализирован в режиме URL")
        
        content = self.read_url()
        if not content.startswith("Ошибка"):
            try:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(content)
                return f"Содержимое URL записано в файл {filename}"
            except Exception as e:
                return f"Ошибка при записи в файл: {e}"
        return content
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
    
    def close(self):
        if self.file:
            self.file.close()
            self.file = None


file = MyFile("text.txt", "read")
text = file.read()  # происходит чтение в виде str
print(text)

# Запись в файл
file = MyFile("text.txt", "write")
result = file.write("привет!")  # происходит запись строки в файл
print(result)

# Добавление в файл
file = MyFile("text.txt", "append")
result = file.write(" привет!")  # происходит добавление строки в конец файла
print(result)

# Работа с URL
file = MyFile("https://pycode.ru/python_tasks_5.html", "url")
# чтение содержимого страницы
text = file.read_url()  # происходит чтение в виде str
print(text[:500] + "...")  # выводим первые 500 символов

# подсчет URL на странице
count = file.count_urls()
print(f"Количество URL на странице: {count}")

# запись содержимого страницы в файл
result = file.write_url("textURL.txt")
print(result)

# закрытие файла
file.close()
