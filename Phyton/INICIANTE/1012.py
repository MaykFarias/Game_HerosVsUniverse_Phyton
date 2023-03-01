a = float(input())
b = float(input())
c = float(input())

area_do_triandulo = (a * c) / 2
## Área = (base x altura) / 2

area_do_circulo = 3.14159 * c**2
## Área = pi x raio²

area_do_trapezio = ((a + b) * c) / 2
## ((base maior + base menor) x altura) / 2

area_do_quadrado = b ** 2
## Área = lado²

area_do_retangulo = a * b
## Área = lado1 x lado2

print(f'TRIANGULO: {area_do_triandulo:.3f}')
print(f'CIRCULO: {area_do_circulo:.3f}')
print(f'TRAPEZIO: {area_do_trapezio:.3f}')
print(f'QUADRADO: {area_do_quadrado:.3f}')
print(f'RETANGULO: {area_do_retangulo:.3f}')