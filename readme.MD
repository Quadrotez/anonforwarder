<h1>Anon Forwarder</h1>
<p>Предназначен для анонимной пересылки сообщений
в конкретный чат в Telegram<br>
Для начала работы потребуется:</p>

<ol>
<li>
Установить <a href="https://www.python.org/">Python</a>
</li>

<li>
Скачать zip-архив с репозитория, распаковав его в свободную папку
</li>

<li>
Открыть терминал (На Windows win+r и в табло вписать cmd), перейдя в вашу директорию (С помощью команды cd "директория")
и установив необходимые библиотеки (pip install -r requirements.txt)
</li>

<li>
Создать файл config.ini
</li>

<li>Вписать туда следующие данные:

    [SECURITY]
    TOKEN=токен бота
    FORWARD_CHAT=айди чата для пересылки
</li>

<li>
Запустить файл main.py
</li>

<li>Готово!</li>
</ol>

<br><br><br>
<p>Использует фреймворк <a href="https://github.com/aiogram/aiogram">Aiogram</a></p>