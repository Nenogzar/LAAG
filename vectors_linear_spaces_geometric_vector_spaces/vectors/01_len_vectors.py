import math


def calculate_vector_length(start_coords, end_coords):
    """
    Изчислява дължината на вектор, определен от начална и крайна точка.

    :param start_coords: Списък от координати на началната точка (x1, y1) или (x1, y1, z1)
    :param end_coords: Списък от координати на крайната точка (x2, y2) или (x2, y2, z2)
    :return: Дължината на вектора
    """
    permissible_length = [2, 3]

    if len(start_coords) != len(end_coords):
        raise ValueError("Началната и крайната точка трябва да имат еднакъв брой координати.")

    if len(start_coords) not in permissible_length:
        raise ValueError("Поддържат се само 2D и 3D вектори.")

    if len(start_coords) == permissible_length[0]:  # 2D вектор
        x1, y1 = start_coords
        x2, y2 = end_coords
        length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return length

    elif len(start_coords) == permissible_length[1]:  # 3D вектор
        x1, y1, z1 = start_coords
        x2, y2, z2 = end_coords
        length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        return length


# Пример за използване на глобалната функция
if __name__ == "__main__":
    start_coords = list(map(float, input("Въведете координатите на началната точка (разделени с интервал): ").split()))
    end_coords = list(map(float, input("Въведете координатите на крайната точка (разделени с интервал): ").split()))

    try:
        length = calculate_vector_length(start_coords, end_coords)
        if len(start_coords) == 2:
            print(f"Дължината на двумерния вектор е: {length}")
        elif len(start_coords) == 3:
            print(f"Дължината на тримерния вектор е: {length}")
    except ValueError as e:
        print(e)
