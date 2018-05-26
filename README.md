# Smashing Wallpaper Downloader

Тестовое задание №2 [https://github.com/ostrovok-team/code-challenge/tree/master/python](https://github.com/ostrovok-team/code-challenge/tree/master/python).
Есть прекрасный сайт Smashing Magazine, который каждый месяц выкладывает отличные обои для десктопа. Заходить каждый месяц и проверять, что там нового дело не благородное, поэтому давайте попробуем автоматизировать эту задачу. Требуется написать cli утилиту, которая будет качать все обои в требуемом разрешение за указанный месяц-год в текущую директорию пользователя. Вот [тут](https://www.smashingmagazine.com/tag/wallpapers/) находятся все обои, а [здесь](https://www.smashingmagazine.com/2017/04/desktop-wallpaper-calendars-may-2017/) находятся обои за май 2017.

# Установка

Для запуска программы требуется установленный Python 3.5.  
В программе используются следующие сторонние библиотеки:  
- [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [lxml](http://lxml.de/)

Используйте команду pip для установки сторонних библиотек из файла зависимостей (или pip3 если есть конфликт с предустановленным Python 2):
```
pip install -r requirements.txt # В качестве альтернативы используйте pip3
```
Рекомендуется устанавливать зависимости в виртуальном окружении, используя [virtualenv](https://github.com/pypa/virtualenv), [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) или [venv](https://docs.python.org/3/library/venv.html).

# Использование

Для просмотра вспомогаельной информации по использованию программы используйте ключ ```-h``` или ```--help```:
```
$ python3 wallpapers.py -h
```
### Аргументы командной строки:
```
wallpapers.py [-h] -s SIZE [-m MONTH] [-y YEAR] [-c]
```
- ```-h, --help``` - Вызов справки.
- ```-s , --size``` - Требуемое разрешение в формате {ширина}x{высота} (например 1920x1080).
- ```-m, --month``` - Требуемый месяц (по умолчанию текущий месяц).
- ```-y, --year``` -  Требуемый год (по умолчанию текущий год).
- ```-c, --calendar``` - Обои с календарем (по умолчанию без календаря).


Пример запуска в Linux(Debian), Python 3.5.2. Скачивание изображений размером 320x480 за текущий месяц-год без календаря:

```
$ python wallpapers.py -s 320x480
may-18-may-the-fourth-be-with-yall-nocal-320x480.png
may-14-monkgolfier-nocal-320x480.png
may-18-geo-nocal-320x480.png
may-18-growth-at-the-cost-of-green-nocal-320x480.jpg
may-17-rainy-days-nocal-320x480.png
may-18-magical-sunset-nocal-320x480.png
may-18-leaves-of-grass-nocal-320x480.jpg
may-18-whats-the-buzz-nocal-320x480.png
may-16-poppies-paradise-nocal-320x480.jpg
may-18-its-finally-may-my-deer-nocal-320x480.png
may-16-lets-have-some-fun-in-the-sun-nocal-320x480.jpg
may-15-field-wild-flowers-nocal-320x480.jpg
may-18-skiing-nocal-320x480.png
may-17-who-is-your-mother-nocal-320x480.png
may-15-welcome-may-with-an-ice-cream-nocal-320x480.jpg
```
# Цели проекта

Код написан для образовательных целей. 