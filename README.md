# sturdy-palm-tree
Приложение для прогнозирования алкогольной зависимости у школьников: ui

ИС содержит следующие элементы:
- Веб-приложение для сбора данных
- Базу данных для хранения результатов опроса и информации о студентах.
- Веб-приложения для прогнозирования результатов опроса<br />
![Диаграмма без названия drawio(10)](https://github.com/user-attachments/assets/0433c536-173c-4b56-a688-c3a05316da89)



Приложение polls_app представляет собой систему сбора данных с помощью форм "Опрос" и возможность отслеживания данных.<br />

login page -- единственная точка входа для администратора в веб-приложение. После прохождения авторизации админу выдаются права для дальшейних действий.<br />
Main -- разводящая страница, которая позволяет перейти на страницы Студенты и Опросы. (ее необходимость не решена)<br />
Опросы -- список опросов, которые есть на сайте.<br />
Студенты -- список студентов и возможность перехода на их детальную страницу.<br />
Детальная страница: опрос -- страница опроса, где отображены все данные по данному опросу: поля, результаты опросов.<br />
Детальная страница студент -- страница студента с его мета информацией и информацией о пройденных опросах.<br />
![Диаграмма без названия drawio(11)](https://github.com/user-attachments/assets/d5a7af8a-3251-416b-a4d1-404ce709211a)


**Login page**<br />
Страница содержит форму авторизации<br />
![Диаграмма без названия drawio(3)](https://github.com/user-attachments/assets/11a96f7b-6bad-4bb3-b96f-6010993bf9a6)

При нажатии на кнопку отправки данных на сервер происходит процесс аутентификация и авторизация.
Данные для администратора будут указаны в переменных среды сервера, т.к для одного пользователя не имеет смысла создавать отдельную сущность, ибо система расчитана для работы одного человека.<br />
![Диаграмма без названия drawio(4)](https://github.com/user-attachments/assets/0e66e05f-d63f-4500-b3f5-0c1557fbf7ea)


**Опросы**<br />
Страница содержит список опросов для сбора данных.
При переходе на страницу происходит обращение к серверу для получения списка опросов. Сами формы опроса не будут храниться в базе данных, а будут располагаться в отдельном файловом хранилище и будут представлять собой схемы-формы с описанием полей и их типом данных, т.к это сделает процесс поддержки в будущем более простым.<br />
![Диаграмма без названия drawio(5)](https://github.com/user-attachments/assets/8b501d6f-2278-4af0-b1f0-e9912060aa74)


**Студенты**<br />
Страница содержит список студентов.
При переходе на страницу срабатывает запрос к серверу для получения списка студентов. Список студентов хранится в базе данных и добавление их в эту базу будет происходит по мере заполнения ими форм опросов. Будет создаваться уникальный составной идентификатор студента, состоящий из его группы и фио. <br />

![Диаграмма без названия drawio(6)](https://github.com/user-attachments/assets/073235e3-4c7a-4832-99d7-432d6e364438)

_Описание алгоритма работы добавления студента в базу данных_ <br />
![Диаграмма без названия drawio(7)](https://github.com/user-attachments/assets/61356d9e-8195-4911-9699-a00526c508d7)

**Детальная страница: опрос**
Страница представляет собой информационную страницу со следующей информацией: поля формы опроса, кол-во раз, сколько этот опрос был пройден, метаинформация об опросе, статистика о прохождении опроса (в разработке).

_Описание алгоритма работы детальной страницы: опрос_<br />
![Диаграмма без названия drawio(8)](https://github.com/user-attachments/assets/4e257935-d371-44de-a7e6-bfd529777761)

**Детальная страница: студент**

Страница с детальной информацией студента: метаинформация, пройденные опросы, прогноз склонности к алкоголизму(в разработке).<br />

![Диаграмма без названия drawio(12)](https://github.com/user-attachments/assets/84ed616a-bea0-4a15-bd8d-81eb79058397)
