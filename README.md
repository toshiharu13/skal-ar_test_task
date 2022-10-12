# Программа для расчета самой длинной дериктории
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
## Программа принимает схему директорий и файлов в формате словаря. На выходе программа передаёт самый длинный файловый путь
## Установка
- Clone project from [github.com](https://github.com)
```shell
git clone https://github.com/toshiharu13/skal-ar_test_task.git
```
Проект готов к использованию, тестовые переменные d1, d2, d3 можно передавать в качестве аргументов в функцию get_long_way

Пример входящих данных
```python
    d1 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}
    d2 = {'dir1': ['file1', 'file1']}
    d3 = {'dir1': ['file1', 'file2', 'file2']}
```

Пример запуска программы
```python
biggest_path = get_long_way(d1)
```

Проект написан для проверки знаний и поднятия скила в общем.
