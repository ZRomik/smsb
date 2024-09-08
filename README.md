# Система анкетирования в социальной сети Телеграм (САССТ)

## Краткое описание

САССТ предназначена для проведения анкетирования респондентов в социальной сети Telegram.
Анкеты формируются через меню `системы`и хранятся в одной из поддерживаемых БД.  
Доступные пользователю виды взаимодействия с`системой` определяет назначенная пользователю`роль`.

## `Роли`пользователя

В системе выделяется 3 доступных`роли` (по возрастанию от низшей к высшей):

- Респондент;
- Администратор;
- Супервайзер.

## Права пользователя

Каждой `роли` в `системе` доступен ограниченный набор действий.  
Роль с высшим статусом наследуют все доступные действия роли с низшим статусом.

1. `Респондент`:
    - Выдается автоматически при регистрации пользователя в системе. Роль нельзя отобрать.
    - Доступны действия:
        - Выбор анкеты для заполнения;
        - Заполнение анкеты;
        - Просмотр своей заполненной анкеты.
2. `Администратор`:
    - Выдается и отбирается супервайзером.
    - Доступны действия:
        - Создание новой анкеты;
        - Удаление существующей анкеты;
        - Добавление вопроса в анкету;
        - Удаление вопроса из анкеты;
        - Изменение позиции вопроса в анкете;
        - Блокировка (бан) аккаунта, после чего пользователь с заблокированным аккаунтом теряет возможность
          взаимодействовия с системой.
3. `Супервайзер`:
    - Выдается автоматически при вводе команды и пароля после первого старта системы;
    - В системе может быть только **один** супервайзер;
    - Доступны действия:
        - Назначение пользователю роли администратора;
        - Удаление у пользователя роли администратора;
        - Разблокировка (разбан) аккаунта;
        - Назначение пользователю роли супервайзера. После этого назначивший роль супервайзер автоматически теряет свою
          роль и получает роль респондента.

## Структура БД

![](\docs\db_structure.png)

## Подготовка к запуску

**Для пользователей Ubuntu**

Необходимо установить дополнительные пакеты для сборки библиотек _python_ с помощью команды `sudo apt install libpq-dev`

1. В каталоге с главным скриптом `bot.py` создать файл конфигурации бота `.env` (без имени).
2. В файл конфигурации добавить параметры:
    - `SMSB_TOKEN` - токен бота полученный от [BotFather](https://t.me/BotFather);
    - `SMSB_DB_TYPE` - тип БД:
        - 1 - PostgreSQL;
        - 2 - MySQL;
        - 3- SQLite.
3. `SMSB_DB_NAME` - имя БД (для SQLite к имени нужно добавить полный путь к файлу БД);
4. `SMSB_DB_USER`- имя пользователя для подключения к БД (только для Postgres и MySQL);
4. `SMSB_DB_PASS` - пароль для подключения к БД (только для Postges и MySQL);
5. `SMSB_ADM` - команда для получения роли администратора;
6. `SMSB_ADM_PASS` - пароль для получения роли администратора;
7. `SMSB_DB_HOST` - адрес сервера БД (только для Postgres и MySQL);
8. `SMSB_SYS` - команда для получения роли супервайзера;
9. `SMSB_SYS_PASS` - пароль для получения роли супервайзера;
10. `SMSB_PORT` - порт для подключения к БД (только если изменялся порт для подключения);
11. `SMSB_LOG` - путь для хранения файлов журнала (необязательный параметр).
12. Установить виртуальное окружение командой `python -m venv bot-env`
13. Активировать виртуальное окружение командой `bot-env\scripts\activate`.
14. Установить необходимые библиотеки спомощью команды `python -m pip install -r requirements.txt`.

## Запуск бота

В активированном виртуальном окружении запустить бот командой `python bot.py`.