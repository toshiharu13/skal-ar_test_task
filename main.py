DIRS_WAY = ''

def get_file(files):
    """
    Функция получает путь до последней папки, и проверяет, есть ли в ней файл
    """
    ...

def unpack_dirs(dirs):
    """
    Функция распаковывает значения словаря и возвращает путь до последней папки
    """
    #TODO разработать вариант, когда в папке может быть несколько веток папок
    global DIRS_WAY
    if not dirs or type(dirs) is list:
        return None
    for key in dirs:
        if type(dirs[key]) is dict:
            DIRS_WAY = f'{DIRS_WAY}/{key}'
            unpack_dirs(dirs[key])
        elif type(dirs[key]) is list:
            continue
        else:
            DIRS_WAY = f'{DIRS_WAY}/{key}'
    return None


def get_long_way(file_system):
    """
    Основная функция, выбирающая максимальный путь до папки/файла
    """
    global DIRS_WAY
    way_counter = [0, '/']
    for system_branch in file_system:
        unpack_dirs(file_system[system_branch],)

        dirs_way = f'{system_branch}/{DIRS_WAY}'
        dir_counter = dirs_way.count('/')
        #print(dir_counter)
        if way_counter[0] < dir_counter:
            way_counter = [dir_counter, dirs_way]
        DIRS_WAY = ''
    return way_counter


if __name__ == '__main__':
    d1 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}
    d2 = {'dir1': ['file1', 'file1']}
    d3 = {'dir1': ['file1', 'file2', 'file2']}
    counter, way = get_long_way(d3)
    print(way)
