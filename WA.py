import urllib.parse
import qrcode

# Número de WhatsApp con código de país (México: +52)
phone_number = "525562164709"

# Mensaje predefinido que quieres que aparezca al abrir WhatsApp
message = "Hola, estoy interesado en la elaboración de una página web desarrollada por NovaWeb. ¿Podrían darme más información?"

# Codificar mensaje para URL
encoded_message = urllib.parse.quote(message)

# Construir URL con mensaje
whatsapp_url_msg = f"https://wa.me/{phone_number}?text={encoded_message}"

# Crear código QR
qr = qrcode.make(whatsapp_url_msg)

# Guardar imagen
qr.save("QR_WhatsApp_NovaWeb_Mensaje.png")

print("Código QR generado y guardado como QR_WhatsApp_NovaWeb_Mensaje.png")
