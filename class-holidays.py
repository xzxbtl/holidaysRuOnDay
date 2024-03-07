from datetime import datetime
import holidays
from config.secret import Settings


class InformationToDay:
    """Показывает текущее время и дату"""

    def __init__(self, day: int, month: int, year: int, date):
        self.day = day
        self.month = month
        self.year = year
        self.date = date
        self.secret_key = Settings.SECRET_KEY
        self.date_str = Settings.formatted_date
        self.current_date = datetime.strptime(self.date_str, "%d-%m-%Y").date()
        self.ru_holidays = holidays.RU()
        self.holidays_for_date = self.ru_holidays.get(self.current_date)

    def show_date_info(self) -> str:
        """Вывод информации о времени"""
        print(f"Текущее время и дата на сегодня\nДень: {str(self.day).zfill(2)}\n"
              f"Месяц: {str(self.month).zfill(2)}\nГод: {str(self.year).zfill(2)}\nДата и Время: {self.date}\n")

    def show_secret_key(self) -> None:
        """Секретный ключ его вывод через метод"""
        print(self.secret_key)

    def __str__(self) -> str:
        return f"InformationToDay(day={self.day}, month={self.month}, year={self.year}, date={self.date})"

    def show_holidays(self):
        """Отображение праздников на сегодня"""
        if self.holidays_for_date:
            print(f"Праздники на {self.current_date}: {self.holidays_for_date}")
        else:
            print(f"На {self.current_date} Крупных Праздников нет")


current_date = datetime.now()
current_date_string = current_date.strftime('%d/%m/%y %H:%M')
obj = InformationToDay(1, 3, 2024, current_date_string)
print(obj)
obj.show_date_info()
obj.show_holidays()
obj.show_secret_key()
