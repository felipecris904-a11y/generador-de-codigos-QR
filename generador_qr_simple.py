"""
Generador de Códigos QR - Versión Simple
"""

import qrcode
import os

def main():
    print("=" * 50)
    print("    GENERADOR DE CÓDIGOS QR")
    print("=" * 50)
    
    while True:
        # Solicitar el enlace o texto
        print("\n")
        enlace = input("Ingrese el enlace o texto para el código QR: ").strip()
        
        if not enlace:
            print("⚠️  Error: No puedes dejar el campo vacío.")
            continue
        
        # Solicitar el nombre del archivo
        nombre = input("¿Qué nombre desea colocarle al archivo?: ").strip()
        
        if not nombre:
            print("  Error: No puedes dejar el campo vacío.")
            continue
        
        # Agregar extensión .png si no la tiene
        if not nombre.lower().endswith('.png'):
            nombre += '.png'
        
        try:
            # Generar el código QR
            print("\n⏳ Generando código QR...")
            img = qrcode.make(enlace)
            img.save(nombre)
            
            print(f"\n✅ ¡Código QR guardado exitosamente como '{nombre}'!")
            print(f"📁 Ubicación: {os.path.abspath(nombre)}")
            print("📱 Ya puedes escanearlo con tu dispositivo móvil.")
            
        except Exception as e:
            print(f"\n❌ Error al generar el código QR: {e}")
        
        # Preguntar si desea continuar
        print("\n" + "-" * 50)
        respuesta = input("¿Deseas generar otro código QR? (s/n): ").lower().strip()
        
        if respuesta not in ['s', 'si', 'sí']:
            print("\n¡Gracias por usar el Generador de Códigos QR! 👋\n")
            break

if __name__ == "__main__":
    main()
