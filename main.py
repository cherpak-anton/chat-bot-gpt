import openai
import json

# Установите ключ API OpenAI
openai.api_key = "YOUR_API_KEY"

# Создайте экземпляр класса OpenAI
openai_instance = openai.api.OpenAI()

# Пример запроса к OpenAI API
def ask_question(prompt):
    response = openai_instance.completions.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    if response and response.choices:
        return response.choices[0].text.strip()

# Пример использования
while True:
    # Получаем ввод пользователя
    input_text = input("> ")

    # Задаем вопрос API OpenAI
    response_text = ask_question(input_text)

    # Печатаем ответ API OpenAI
    print(response_text)
