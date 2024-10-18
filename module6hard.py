import math


class Figure:
    sides_count = 0  # Счётчик количества сторон фигуры.
    side_lengths_count = 0  # Счётчик длин сторон, передаваемых при создании фигуры.
    control_sides_vector = []  # Массив с единичными сторонами в количестве sides_count, которое требует фигура.
    planar_polygon_index = False # Индекс свойства, принимает значение "True" для плоских многоугольников.
    regular_polygon_index = False # Индекс свойства, принимает значение "True" для правильных многоугольников.

    def __init__(self, color: list[int], *sides, filled=True): # Массив color определён как список.
        self.filled = filled

        """
        Проверка на количество и правильность переданных значений параметров, 
        задающих цвет в RGB-формате при создании объектов: 
        если количество и значения параметров не принадлежат требуемому диапазону, 
        то создаётся фигура предустановленного цвета, а на консоль выводится соответствующее сообщение.
        """
        if len(color) != 3:
            self.red = 100
            self.green = 0
            self.blue = 0
            self.__color = [self.red, self.green, self.blue]
            print(f'Ошибка при введении параметров, задающих цвет фигуры в RGB-формате. '
                  f' Должно быть передано ровно 3 целых числа от 0 до 255 включительно. Введено: {color}. '
                  f'\nЦвет фигуры задан предустановленными значениями параметров: {self.__color}.')
        else:
            if (color[0] not in range(0, 256) or color[1] not in range(0, 256) or color[2] not in range(0, 256) or
                    not isinstance(color[0], int) or not isinstance(color[1], int) or not isinstance(color[2], int)):
                print('Числа, задающие RGB - формат, введены некорректно '
                      '(корректные значения должны принадлежать диапазону целых чисел от 0 до 255 включительно).')
            else:
                self.red = color[0]
                self.green = color[1]
                self.blue = color[2]
                self.__color = [self.red, self.green, self.blue]

        """
        Проверка на количество и правильность значений переданных длин сторон при создании объектов: 
        1) если количество переданных длин сторон не равно side_lengths_count, то создаётся массив с единичными 
        сторонами в кол-ве, которое требует фигура, а на консоль выводится соответствующее сообщение;
        2) если значения длин переданных сторон не принадлежат тербуемому диапазону значений, 
        то создаётся пустая строка, а на консоль выводится соответствующее сообщение.
        """
        self.__sides = self.control_sides_vector
        if len(sides) != self.side_lengths_count:
            print(f'Ошибка при вводе длин сторон фигуры. '
                  f'Количество введенных длин сторон {len(sides)} отличается от '
                  f'требуемого количества {self.side_lengths_count}. '
                  f'\nВведенный список сторон {list(sides)} преобразован в массив {self.control_sides_vector} '
                  f'с единичными сторонами в том количестве, которое требует фигура.')
        elif len(sides) == self.side_lengths_count:
            for side in sides:
                if side <= 0 or not isinstance(side, int):
                    print(f'Ошибка при вводе длин стороны фигуры. '
                          f'Длина стороны должны принимать целые положительные значения. '
                          f'\nВведенный список сторон {list(sides)} преобразован в массив {self.control_sides_vector} '
                          f'с единичными сторонами в том количестве, которое требует фигура.')
                    break
            else:
                if self.regular_polygon_index:
                    self.__sides = []
                    for i in range(0, self.sides_count):
                        self.__sides.append(sides[0])
                else:
                    for side in sides:
                        if 2 * side >= sum(sides) and self.planar_polygon_index:
                            print(f'Ошибка при вводе длин сторон фигуры. '
                                  f'Длина стороны "{side}" больше суммы длин остальных сторон. '
                                  f'\nВведенный список сторон {list(sides)} преобразован в массив {self.control_sides_vector} '
                                  f'с единичными сторонами в том количестве, которое требует фигура.')
                            break
                    else:
                        self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        color_params = False
        if r not in range(0, 256) or g not in range(0, 256) or b not in range(0, 256):
            pass
        elif not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
            pass
        else:
            color_params = True
        return color_params

    def set_color(self, new_color: list[int]):
        if len(new_color) != 3:
            print(f'Ошибка при попытке изменения цвета фигуры в RGB-формате. '
                  f' Должно быть передано ровно 3 целых числа от 0 до 255 включительно. Введено: {new_color}. '
                  f'\nЦвет фигуры не изменен.')
        else:
            new_r = new_color[0]
            new_g = new_color[1]
            new_b = new_color[2]
            res_exam_colors = self.__is_valid_color(new_r, new_g, new_b)
            if res_exam_colors == False:
                print(f'Числа, задающие цвет фигуры в RGB - формате, переопределены некорректно: {new_color} '
                      '(корректные значения принадлежат диапазону целых чисел от 0 до 255 включительно). '
                      '\nЦвет фигуры не изменен.')
            else:
                self.__color = new_color

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, sides):
        sides_param = True
        if len(sides) != self.side_lengths_count:
            sides_param = False
            print('Ошибка при попытке изменения длин сторон фигуры. '
                  f'Количество новых длин сторон {len(sides)} отличается от требуемого '
                  f'для данной фигуры количества {self.side_lengths_count}.')
        else:
            for side in sides:
                if side <= 0 or not isinstance(side, int):
                    sides_param = False
                    print(f'Ошибка при попытке изменения длин сторон фигуры. '
                          f'Новые длины сторон {list(sides)} введены некорректно. '
                          '\nДлины сторон должны принимать целые положительные значения.')
                    break
            else:
                if self.planar_polygon_index:
                    for side in sides:
                        if 2 * side >= sum(sides):
                            sides_param = False
                            print(
                                f'Ошибка при попытке изменения длин сторон фигуры. Введены длины сторон: {list(sides)}. '
                                f'Длина стороны "{side}" больше суммы длин остальных сторон.')
                            break
        return sides_param

    def set_sides(self, *new_sides):
        res_exam_sides = self.__is_valid_sides(new_sides)
        if res_exam_sides:
            self.__sides = list(new_sides)
        else:
            print('Длины сторон фигуры остались прежними.')

    def __len__(self):
        perimetr = sum(self.__sides)
        return perimetr


class Circle(Figure):
    sides_count = 1
    side_lengths_count = 1
    control_sides_vector = [1]

    def __init__(self, color: list[int], *sides, filled=True):
        super().__init__(color, *sides, filled=filled)
        self.__radius = None

    def calc_radius(self):
        radius = Figure.__len__(self) / (2 * math.pi)
        return radius

    def printer_rad(self):
        self.__radius = self.calc_radius()
        print(self.__radius)

    def get_square(self):
        self.__radius = self.calc_radius()
        circle_square = math.pi * self.__radius ** 2
        return circle_square


class Triangle(Figure):
    sides_count = 3
    side_lengths_count = 3
    control_sides_vector = [1, 1, 1]
    planar_polygon_index = True

    def get_square(self):
        p = 0.5 * Figure.__len__(self)
        triangle_square = (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5
        return triangle_square


class Cube(Figure):
    sides_count = 12
    side_lengths_count = 1
    regular_polygon_index = True
    control_sides_vector = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def get_volume(self):
        cub_volume = self.get_sides()[0] ** 3
        return cub_volume


print()
print(f'ПРОВЕРКА КЛАССА {Circle}, ЕСЛИ ДАННЫЕ ВВЕДЕНЫ КОРРЕКТНО.')
cr = Circle([35, 44, 16], 11)
print(cr.get_sides())
print(cr.get_color())
cr.set_sides(4)
print(cr.get_sides())
print(len(cr))
print(cr.sides_count)
cr.printer_rad()
print(cr.get_square())
cr.set_color([55, 34, 40])
print(cr.get_color())

print()
print(f'ПРОВЕРКА КЛАССА {Circle}, ЕСЛИ ДАННЫЕ ВВЕДЕНЫ НЕКОРРЕКТНО.')
cr2 = Circle([235, 32, 154], 89, 2)
print(cr2.get_sides())
cr2.set_sides(6.2)
print(cr2.get_sides())
cr2.set_sides(7)
print(cr2.get_sides())
cr2.set_sides(44, 11)
print(cr2.get_sides())
print()
cr3 = Circle([235, 34, 68], 24)
print(cr3.get_color())
cr3.set_color([387, 23, 67])
print(cr3.get_color())
cr3.set_color([38, 8.7, 23])
print(cr3.get_color())
cr3.set_color([87, 23, 67])
print(cr3.get_color())
cr3.set_color([64, 91])
print(cr3.get_color())
cr4 = Circle([235, 34], 24)
print(cr4.get_color())

print()
print(f'ПРОВЕРКА КЛАССА {Triangle}, ЕСЛИ ДАННЫЕ ВВЕДЕНЫ КОРРЕКТНО.')
tr1 = Triangle([28, 43, 15], 3, 6, 8)
print(tr1.get_sides())
print(tr1.get_color())
print(tr1.get_square())
tr1.set_sides(3, 4, 5)
print(tr1.get_sides())
print(tr1.get_square())

print()
print(f'ПРОВЕРКА КЛАССА {Triangle}, ЕСЛИ ДАННЫЕ ВВЕДЕНЫ НЕКОРРЕКТНО.')
tr1.set_color([32, 18])
print(tr1.get_color())
tr2 = Triangle([28, 43], 3, 6, 8)
print(tr2.get_color())
tr3 = Triangle([28, 43, 15], 3, 8)
tr4 = Triangle([28, 43, 34, 56], 3, 6, 8)
tr5 = Triangle([28, 43, 34], 3, 6, 10)
tr5.set_sides(3, 6, 8)
print(tr5.get_sides())
tr5.set_sides(1, 2, 15)
print(tr5.get_sides())
tr1.set_sides(3, 4, 10)
print(tr1.get_sides())
print(tr1.get_square())
tr7 = Triangle([28, 43, 15], 17, 6, 35)
print(tr7.get_sides())

print()
print(f'ПРОВЕРКА КЛАССА {Cube}, ЕСЛИ ДАННЫЕ ВВЕДЕНЫ КОРРЕКТНО.')
cu1 = Cube([235, 64, 180], 4)
print(cu1.get_sides())
print(cu1.get_volume())
cu1.set_color([32, 18, 201])
print(cu1.get_color())
cu1.set_sides(37)
print(cu1.get_sides())

print()
print(f'ПРОВЕРКА КЛАССА {Cube}, ЕСЛИ ДАННЫЕ ВВЕДЕНЫ НЕКОРРЕКТНО.')
cu2 = Cube([235, 64, 180], 64, 44)
print(cu2.get_sides())
cu1.set_sides(37, 18)
print(cu1.get_sides())
cu1.set_sides(-4)
print(cu1.get_sides())

# КОД ДЛЯ ПРОВЕРКИ, ДАННЫЙ В ЗАДАНИИ
print()
print()
print('КОД ДЛЯ ПРОВЕРКИ:')
circle1 = Circle([100, 200, 100], 10)  # (Цвет, стороны)
cube1 = Cube([222, 35, 130], 6)

# Проверка на изменение цветов:
circle1.set_color([55, 66, 77])  # Изменится
print(circle1.get_color())
cube1.set_color([300, 70, 15])  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
