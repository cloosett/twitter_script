# twitter_script
    Скрипт Автоматизації Twitter
Цей скрипт автоматизує публікації в Twitter за допомогою Selenium та Chrome WebDriver. Він зчитує дані облікового запису та повідомлень зі вхідних файлів та використовує пул потоків для паралельного виконання.

    Передумови
Python: Переконайтеся, що на вашому комп'ютері встановлено Python. Ви можете завантажити його з python.org.
Chrome WebDriver: Завантажте Chrome WebDriver, який відповідає версії вашого браузера Chrome. Ви можете знайти його тут.
Необхідні Пакети: Встановіть необхідні пакети Python за допомогою наступної команди:
pip install selenium fake_useragent

    Використання
Клонування репозиторію:
git clone https://github.com/your-username/your-repository.git
Перейдіть в директорію:
cd your-repository
Встановлення додаткових пакетів:
pip install -r requirements.txt
Завантаження Chrome WebDriver:
Завантажте Chrome WebDriver та розмістіть його в тій же директорії, що й скрипт.
    
    Створення Вхідних Файлів:

ТІЛЬКИ В ТОМУ ВИПАДКУ, ЯКЩО ФАЙЛІВ ЩЕ НЕМА!
Створіть файл з назвою accounts.txt із обліковими записами Twitter у форматі username:password на кожному рядку.
Створіть файл із назвою post.txt із текстом твітів, які ви хочете опублікувати, на кожному рядку.


    Запустіть Скрипт:

python main.py

    Моніторинг Виконання:

Скрипт буде виконуватися паралельно для кожної комбінації облікового запису та повідомлення. Перевіряйте консоль на предмет помилок або успішного виконання.

    Зауваження
Переконайтеся, що ви використовуєте правильну версію Chrome WebDriver.
Розкоментуйте опцію --headless у скрипті для безголового виконання, якщо це потрібно.
Відредагуйте параметр max_workers у скрипті відповідно до можливостей вашої системи.
Зв'язок зі мною телеграм : @kiiirookie.
