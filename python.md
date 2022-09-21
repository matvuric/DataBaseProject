# Интеграция Python

[Реализация](/dbConfig.py) создает в БД таблицы на каждый месяц и заполняет их. Учитывается количество дней в каждом месяце, а также является ли год високосным.
Для работы программы необходимо наличие вспомогательного файла config, из которого в программу поступают данные о sql сервере. 

---

Для файла config рекомендуется следующий вид:

``` py
host = "localhost"
user = "<DB_user_name>"
password = "****"
db_name = "<DataBase_name>"
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
```
