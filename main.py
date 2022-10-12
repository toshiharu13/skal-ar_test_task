DIRS_WAYS = []
ALLOWED_CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/.1234567890'


def get_validation(dir_way):
    """
    Функция валидатор
    """
    global ALLOWED_CHARACTERS
    if len(dir_way) > 255:
        raise Exception('Количество занков не должно превышать 255')
    for character in dir_way:
        if character not in ALLOWED_CHARACTERS:
            raise Exception('Использованы запрещенные символы')
    if dir_way.count('/') <= 1:
        return '/'
    return dir_way


def check_files(files):
    """
    Функция проверки корректности файлов
    """
    dublicates = [number for number in files if files.count(number) > 1]
    if dublicates:
        print('Найдены дубликаты имён файлов в одной папке!')

        for dublicate in dublicates:
            files.remove(dublicate)
        return files

    return None


def get_file(folder_way, file_system):
    """
    Функция получает путь до последней папки, и проверяет, есть ли в ней файл
    """
    way_to_file = file_system

    mod_folder_way = folder_way.split('/')
    for folder in mod_folder_way:
        way_to_file = way_to_file[folder]
    if way_to_file:
        if type(way_to_file) is list:
            if check_files(way_to_file):
                return way_to_file[0]
    return None


def unpack_dirs(dirs, way=''):
    """
    Функция распаковывает значения словаря и возвращает путь до последней папки
    """
    global DIRS_WAYS

    if not dirs or type(dirs) is list:
        DIRS_WAYS.append(f'{way}')
        return None

    for key in dirs:
        if type(dirs[key]) is dict or list:
            way_foward = f'{way}/{key}'
            unpack_dirs(dirs[key], way_foward)
    return None


def get_long_way(file_system):
    """
    Основная функция, выбирающая максимальный путь до папки/файла
    """
    global DIRS_WAYS
    ways_counter = [-1, '']
    for system_branch in file_system:
        unpack_dirs(file_system[system_branch], system_branch)

        for decode_branch in DIRS_WAYS:
            dir_counter = decode_branch.count('/')
            if ways_counter[0] < dir_counter:
                ways_counter = [dir_counter, decode_branch]
    _, biggest_way = ways_counter
    trailing_file = get_file(biggest_way, file_system)
    if trailing_file:
        biggest_way = f'{biggest_way}/{trailing_file}'

    validated_b_way = get_validation(f'/{biggest_way}')
    return validated_b_way


if __name__ == '__main__':
    d1 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}
    d2 = {'dir1': ['file1', 'file1']}
    d3 = {'dir1': ['file1', 'file2', 'file2']}

    biggest_path = get_long_way(d1)

    print(biggest_path)
