from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def crear_carta_cafe(nombre_archivo, productos):
    # Crear el objeto PDF
    pdf = canvas.Canvas(nombre_archivo, pagesize=letter)

    # Títulos
    pdf.setFont("Helvetica", 16)
    pdf.drawString(100, 750, "Carta de Café")

    # Línea separadora
    pdf.line(50, 730, 550, 730)

    # Lista de productos
    pdf.setFont("Helvetica", 12)
    y = 700  # Posición inicial en el eje y

    for producto, precio in productos.items():
        pdf.drawString(100, y, f"{producto}: ${precio}")
        y -= 20  # Mover hacia arriba para el próximo producto

    # Guardar el PDF
    pdf.save()

# Lista de productos y precios
productos = {
    "Pastel de Queso": 4900,
    "Croissant de Queso": 4800,
    "Pastel de Arequipe": 4900,
    "Empanada Argentina": 7600,
}

# Nombre del archivo PDF de salida
nombre_archivo = "carta_cafe.pdf"

# Crear la carta de café
crear_carta_cafe(nombre_archivo, productos)

print(f"La carta de café ha sido creada en: {nombre_archivo}")
