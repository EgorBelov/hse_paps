
## Цель
Создание инструмента для быстрого и точного распознавания объектов на видеоизображениях, опубликованных в социальных сетях, с возможностью поиска по заданным параметрам. Приложение должно помочь пользователям находить необходимый контент, автоматизировать обработку видеоданных, а также обеспечивать удобный интерфейс и интеграцию с популярными социальными платформами.

## Перечень заинтересованных лиц (стейкхолдеров)
1. Разработчик
    - Роль: основной создатель приложения, отвечающий за проектирование, разработку, тестирование и внедрение системы.
    - Интересы: успешное завершение проекта, соответствие поставленным требованиям, получение опыта и навыков в области разработки.

2. Пользователи приложения
    - Роль: люди, которые будут использовать приложение для поиска объектов на видео в социальных сетях.
    - Интересы: простота и удобство использования, высокая точность поиска, быстрое получение результатов.

3. Научный руководитель
    - Роль: наставник, предоставляющий рекомендации, проверяющий выполнение работы и оценивающий результаты.
    - Интересы: соответствие поставленным задачам, качественное выполнение лабораторной работы, соответствие научным и практическим стандартам.

4. Администраторы платформ социальных сетей (непрямые стейкхолдеры)
    - Роль: владельцы и разработчики API, через которые приложение будет интегрироваться с социальными сетями.
    - Интересы: соблюдение условий использования API, минимальная нагрузка на их системы, соблюдение конфиденциальности данных.

## Перечень функциональных требований
- Распознавание объектов на видео
    Возможность определять заданные пользователем объекты (люди, автомобили, животные и т.д.) на видео.

- Поиск видео с объектами
    Возможность находить видео в социальных сетях на основе заданного описания или изображений объектов.

- Фильтрация результатов
    Возможность сортировки и фильтрации результатов по временным меткам, местоположению и платформам.

- Выгрузка и анализ данных
    Возможность выгрузки результатов поиска и предоставления аналитической сводки.

- Интеграция с популярными социальными сетями
    Работа с платформами (например, Telegram, VK) через API.

## Диаграмма вариантов использования
![alt text](<Снимок экрана 2024-12-11 в 14.30.21.png>)

## Перечень сделанных предположений
- Доступ к API социальных сетей
    Считается, что API платформ социальных сетей предоставляют возможность поиска и анализа видеоконтента.

- Качество исходных данных
    Видеоизображения содержат достаточное качество для работы алгоритмов машинного обучения.

- Ограничения платформ
    Временные лимиты и ограничения API учтены, но не создадут значительных барьеров для поиска.

- Объекты поиска
    Пользователи заранее знают, какие объекты они хотят найти, и предоставляют соответствующие запросы или примеры.

- Права пользователей
    У пользователей есть необходимые права для работы с видео и данными из социальных сетей.

## Перечень нефункциональных требований
- Производительность
    Обработка запросов не превышает 3 секунд для видео до 10 минут длительности.

- Масштабируемость
    Система должна обрабатывать до 10000 запросов в день без снижения производительности.

- Безопасность
    Данные пользователей должны быть защищены согласно стандарту GDPR.

- Интерфейс
    Удобный и интуитивно понятный интерфейс с минимальным количеством действий для выполнения поиска.

- Совместимость
    Приложение должно быть доступно на основных браузерах (Chrome, Firefox, Safari).

- Точность
    Уровень точности распознавания объектов должен составлять не менее 80%.

