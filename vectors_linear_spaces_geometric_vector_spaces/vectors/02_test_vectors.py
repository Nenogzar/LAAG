import math


def calculate_vector_length(start_coords, end_coords):
    permissible_length = [2, 3]
    if len(start_coords) != len(end_coords):
        raise ValueError("Началната и крайната точка трябва да имат еднакъв брой координати.")
    if len(start_coords) not in permissible_length:
        raise ValueError("Поддържат се само 2D и 3D вектори.")
    if len(start_coords) == 2:
        return math.sqrt((end_coords[0] - start_coords[0]) ** 2 + (end_coords[1] - start_coords[1]) ** 2)
    elif len(start_coords) == 3:
        return math.sqrt((end_coords[0] - start_coords[0]) ** 2 + (end_coords[1] - start_coords[1]) ** 2 + (
                    end_coords[2] - start_coords[2]) ** 2)


def vector_subtract(vec1, vec2):
    return [vec1[i] - vec2[i] for i in range(len(vec1))]


def is_zero_vector(vector):
    return all(coordinate == 0 for coordinate in vector)


def are_equal_vectors(vec1, vec2):
    return vec1 == vec2


def are_parallel_vectors(vec1, vec2):
    if len(vec1) == 2 and len(vec2) == 2:
        # Проверка за 2D вектори чрез пропорционалност
        return vec1[0] * vec2[1] == vec1[1] * vec2[0]
    elif len(vec1) == 3 and len(vec2) == 3:
        # Проверка за 3D вектори чрез векторно произведение
        cross_product = [vec1[1] * vec2[2] - vec1[2] * vec2[1], vec1[2] * vec2[0] - vec1[0] * vec2[2],
                         vec1[0] * vec2[1] - vec1[1] * vec2[0]]
        return is_zero_vector(cross_product)
    else:
        raise ValueError("Поддържат се само 2D и 3D вектори.")


def are_same_direction(vec1, vec2):
    if len(vec1) != len(vec2):
        return False
    return all(vec1[i] * vec2[i] > 0 for i in range(len(vec1)))


def are_in_same_plane(vec1, vec2, vec3):
    if len(vec1) == 3 and len(vec2) == 3 and len(vec3) == 3:
        cross_product = [vec1[1] * vec2[2] - vec1[2] * vec2[1], vec1[2] * vec2[0] - vec1[0] * vec2[2],
                         vec1[0] * vec2[1] - vec1[1] * vec2[0]]
        dot_product = sum(cross_product[i] * vec3[i] for i in range(len(cross_product)))
        return dot_product == 0
    else:
        raise ValueError("Проверката за равнина е възможна само за 3D вектори.")


def are_parallel_to_plane(vec, plane_normal):
    if len(vec) == 3 and len(plane_normal) == 3:
        dot_product = sum(vec[i] * plane_normal[i] for i in range(len(vec)))
        return dot_product == 0
    else:
        raise ValueError("Проверката за успоредност на равнина е възможна само за 3D вектори.")


def analyze_vectors(start1, end1, start2, end2):
    vec1 = vector_subtract(end1, start1)
    vec2 = vector_subtract(end2, start2)
    print(f"{vec1= }, {vec2= }")

    results = {
        "is_zero_vector_1 - първият вектор е нулев": is_zero_vector(vec1),
        "is_zero_vector_2 - вторият вектор е нулев": is_zero_vector(vec2),
        "are_equal - двата вектора са равни": are_equal_vectors(vec1, vec2),
        "are_parallel - двата вектора са успоредни": are_parallel_vectors(vec1, vec2),
        "are_same_direction -  двата вектора са еднопосочни": are_same_direction(vec1, vec2),
        "are_opposite_direction - двата вектора са разнопосочни": are_parallel_vectors(vec1, vec2) and not are_same_direction(vec1, vec2),
        "are_in_same_plane - вектор лежат в една и съща равнина": None,  # Only applicable for 3D vectors
        "are_parallel_to_plane -  вектор е успореден на равнина": None  # Only applicable for 3D vectors
    }

    if len(vec1) == 3 and len(vec2) == 3:
        normal = vector_subtract(end2, start1)
        results["are_in_same_plane"] = are_in_same_plane(vec1, vec2, normal)
        results["are_parallel_to_plane"] = are_parallel_to_plane(vec1, vec2)

    return results


# Пример за използване на глобалната функция
if __name__ == "__main__":
    start1 = list(
        map(float, input("Въведете координатите на началната точка на първия вектор (разделени с интервал): ").split()))
    end1 = list(
        map(float, input("Въведете координатите на крайната точка на първия вектор (разделени с интервал): ").split()))
    start2 = list(
        map(float, input("Въведете координатите на началната точка на втория вектор (разделени с интервал): ").split()))
    end2 = list(
        map(float, input("Въведете координатите на крайната точка на втория вектор (разделени с интервал): ").split()))

    try:
        length_vec1 = calculate_vector_length(start1, end1)
        length_vec2 = calculate_vector_length(start2, end2)
        print(f"Дължината на първия вектор е: {length_vec1}")
        print(f"Дължината на втория вектор е: {length_vec2}")

        results = analyze_vectors(start1, end1, start2, end2)
        for key, value in results.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(e)
