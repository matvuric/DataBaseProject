# Ход выполнения нормализации
После выделения конкретных сущностей, был сформирован список атрибутов каждой сущности:
### CALENDAR:
> Календарь мероприятий содержит в себе ключевой атрибут - id и колонку date, в которой располагается информация о дате мероприятия в формате DATETIME. При помощи ключа id таблица связана с сущностью EVENT. Все атрибуты данной сущности обязательны к заполнению.
### EVENT:
> Мероприятия содержат информацию об описании мероприятия - event, изображение(превью) - picture, а также ключевой атрибут date_id, указывающий на значение в сущности CALENDAR, содержащем информацию о дате мероприятия. Все атрибуты данной сущности обязательны к заполнению.
### CATEGORY:
> Категории содержат список типовых мест в городе (спортивные, музеи, исторические места и т.д.) - category_name и ключевой атрибут - id, связывающий с сущностью PLACES. Все атрибуты данной сущности обязательны к заполнению.
### PLACES:
> Места содержат информацию с описанием места - place и адресом - address, а также ключевой атрибут - cat_id, указывающий на категорию, к которой относится место. Все атрибуты данной сущности обязательны к заполнению.
### PEOPLE:
> Таблица люди содержит информацию об исторический личностях: имя - name, фотография - picture, описание - description, дата рождения - birth_date и дату смерти - death_date. Все атрибуты данной сущности обязательны к заполнению.
