# Пример Python-кода, демонстрирующего принципы KISS, YAGNI, DRY и SOLID

# Принцип единственной ответственности (SRP): Каждый класс отвечает за одну задачу.
class VideoProcessor:
    def extract_objects(self, video_path):
        """
        Извлекает объекты из видео.
        :param video_path: Путь к видеофайлу.
        :return: Список распознанных объектов.
        """
        print(f"Обработка видео: {video_path}")
        return ["машина", "дерево", "человек"]  # Симуляция результата распознавания

class ResultsFormatter:
    def format_results(self, objects):
        """
        Форматирует результаты распознавания для отображения.
        :param objects: Список распознанных объектов.
        :return: Отформатированная строка с результатами.
        """
        return f"Распознанные объекты: {', '.join(objects)}"

# Принцип открытости/закрытости (OCP): Классы открыты для расширения, но закрыты для изменения.
class VideoFilter:
    def filter_objects(self, objects, criteria):
        """
        Фильтрует распознанные объекты на основе заданных критериев.
        :param objects: Список распознанных объектов.
        :param criteria: Критерии фильтрации (список допустимых объектов).
        :return: Отфильтрованный список объектов.
        """
        return [obj for obj in objects if obj in criteria]

# Принцип подстановки Барбары Лисков (LSP): Подклассы должны заменять базовые классы.
class AdvancedVideoProcessor(VideoProcessor):
    def extract_objects(self, video_path):
        """
        Расширенная обработка видео с добавлением новых типов объектов.
        :param video_path: Путь к видеофайлу.
        :return: Расширенный список распознанных объектов.
        """
        print(f"Расширенная обработка видео: {video_path}")
        return super().extract_objects(video_path) + ["велосипед"]

# Принцип разделения интерфейса (ISP): Клиенты не должны зависеть от методов, которые они не используют.
class ReportGenerator:
    def generate_report(self, formatted_results):
        """
        Генерирует отчет для результатов распознавания.
        :param formatted_results: Отформатированные результаты.
        """
        print(f"Отчет: {formatted_results}")

# Принцип инверсии зависимостей (DIP): Модули высокого уровня не зависят от модулей низкого уровня.
def process_video(video_path, processor, formatter, reporter):
    """
    Выполняет полный цикл обработки видео: распознавание, форматирование и генерация отчета.
    :param video_path: Путь к видеофайлу.
    :param processor: Экземпляр класса, отвечающего за обработку видео.
    :param formatter: Экземпляр класса, отвечающего за форматирование результатов.
    :param reporter: Экземпляр класса, отвечающего за генерацию отчетов.
    """
    objects = processor.extract_objects(video_path)
    formatted_results = formatter.format_results(objects)
    reporter.generate_report(formatted_results)

# Основная программа, демонстрирующая использование
if __name__ == "__main__":
    video_path = "sample_video.mp4"

    # Применение принципа инверсии зависимостей
    processor = VideoProcessor()
    formatter = ResultsFormatter()
    reporter = ReportGenerator()

    process_video(video_path, processor, formatter, reporter)

    # Демонстрация гибкости (OCP, LSP) с использованием AdvancedVideoProcessor
    advanced_processor = AdvancedVideoProcessor()
    process_video(video_path, advanced_processor, formatter, reporter)
