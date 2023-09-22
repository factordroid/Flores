from bokeh.plotting import figure, show, output_file
from bokeh.models import Label, BoxAnnotation
from bokeh.layouts import column
import numpy as np

# Parámetros para ajustar la forma de la flor
A = 1
B = 5
C = 1

# Rango de t
t = np.linspace(0, 2 * np.pi, 1000)

# Ecuaciones paramétricas para los pétalos de la flor central
x = A * np.sin(B * t) * np.cos(C * t)
y = A * np.sin(B * t) * np.sin(C * t)

# Coordenadas para el tallo de la flor central (doble de largo)
x_stem = np.array([0, 0])
y_stem = np.array([0, -2*A])  # El tallo es ahora el doble de largo

# Coordenadas para el núcleo de la flor central (color naranja)
x_core = np.array([0])
y_core = np.array([0])

# Coordenadas para los pétalos de las flores laterales (tamaño reducido)
x_left = x / 2 - 2
x_right = x / 2 + 2
y_left = y / 2 - 1
y_right = y / 2 - 1

# Coordenadas para el tallo de las flores laterales (tamaño reducido)
x_stem_left = np.array([-2, -2])
x_stem_right = np.array([2, 2])
y_stem_left = np.array([-1, -3])  # El tallo es ahora el doble de largo
y_stem_right = np.array([-1, -3])  # El tallo es ahora el doble de largo

# Coordenadas para el núcleo de las flores laterales (color naranja)
x_core_left = np.array([-2])
x_core_right = np.array([2])
y_core_left = np.array([-1])
y_core_right = np.array([-1])

# Crear una figura de Bokeh
p = figure(title="Flores Interactivas", width=800, height=400)

# Dibujar los pétalos de la flor central con relleno amarillo
p.patch(x, y, line_color="yellow", fill_color="yellow", line_width=2)

# Dibujar el tallo de la flor central en color verde
p.line(x_stem, y_stem, line_color="green", line_width=5)

# Dibujar el núcleo de la flor central en color naranja
p.circle(x_core, y_core, size=20, line_color="orange", fill_color="orange")

# Dibujar los pétalos de las flores laterales con relleno amarillo y tamaño reducido
p.patch(x_left, y_left, line_color="yellow", fill_color="yellow", line_width=2)
p.patch(x_right, y_right, line_color="yellow", fill_color="yellow", line_width=2)

# Dibujar el tallo de las flores laterales en color verde
p.line(x_stem_left, y_stem_left, line_color="green", line_width=5)
p.line(x_stem_right, y_stem_right, line_color="green", line_width=5)

# Dibujar el núcleo de las flores laterales en color naranja
p.circle(x_core_left, y_core_left, size=20, line_color="orange", fill_color="orange")
p.circle(x_core_right, y_core_right, size=20, line_color="orange", fill_color="orange")

# Agregar un rectángulo rojo alrededor del texto
texto = "AQUI ESTAN TUS FLORES AMARILLAS POR BONITA, TE AMO"
label = Label(x=0, y=-4.5, text=texto, text_color="yellow", text_font_size="12pt", text_align="center")
rect = BoxAnnotation(left=-8, right=8, top=-4, bottom=-6, fill_color="red", line_color="red")
p.add_layout(rect)
p.add_layout(label)

# Configurar aspecto de la figura
p.axis.visible = False
p.toolbar.logo = None

# Guardar la figura en un archivo HTML
output_file("flores_interactivas_corregido.html")

# Mostrar la figura en el navegador
show(p)
