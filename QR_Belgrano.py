from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import qrcode

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

def generar_codigo_qr(pdf_url, qr_filename):
    # Crear el objeto QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Agregar la URL del archivo PDF al código QR
    qr.add_data(pdf_url)
    qr.make(fit=True)

    # Crear la imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen del código QR
    img.save(qr_filename)

# Lista de productos y precios
productos = {
    "Pastel de Queso": 4900,
    "Croissant de Queso": 4800,
    "Pastel de Arequipe": 4900,
    "Empanada Argentina": 7600,
}

# Nombre del archivo PDF de salida
nombre_archivo_pdf = "carta_cafe.pdf"

# URL del archivo PDF en GitHub (reemplázala con tu propia URL)
url_pdf_github = "https://github.com/jucampuca/QR_Belgrano_02/blob/master/carta_cafe.pdf"

# Nombre del archivo QR de salida
nombre_archivo_qr = "codigo_qr.png"

# Crear la carta de café
crear_carta_cafe(nombre_archivo_pdf, productos)

# Generar el código QR con la URL de GitHub
generar_codigo_qr(url_pdf_github, nombre_archivo_qr)

print(f"La carta de café ha sido creada en: {nombre_archivo_pdf}")
print(f"El código QR ha sido creado en: {nombre_archivo_qr}")
