#codigo de prueba aqui#

from restaurante3 import ManejoPedidos, Pago

"""
aca va la prueba de lo que esta en el archivo restaurante3.py y se 
comprueba con modificaciones con respecto al archivo original
"""

def demo_pedido_completo():
    manager = ManejoPedidos()

def mostrar_menu(manager):
    """Muestra el menú actual"""
    print("\n--- MENÚ DISPONIBLE ---")
    for nombre, item in manager.menu.menu_items.items():
        print(f"{nombre}: ${item.price:.2f} ({item.type}/{item.subtype})")

items_iniciales = [
        ("Refresco", 2.5, "bebida", "mediano"),
        ("Ensalada Felipe", 6.50, "plato", "entrada"),
        ("Pizza Hawaiana", 12.5, "plato", "principal"),
        ("Banana split", 5.0, "postre", "postre")
    ]
for nombre, precio, tipo, subtipo in items_iniciales:
        if not manager.menu.get_item(nombre):
            manager.menu.add_item(nombre, precio, tipo, subtipo)
    
mostrar_menu(manager)
    
pedido = manager.create_order()
print("\n--- AÑADIENDO ÍTEMS AL PEDIDO ---")
    
manager.add_to_order(pedido, "Pizza Hawaiana", 2)
manager.add_to_order(pedido, "Banana split", 1)
    
pedido.mostrar_factura()
    
print("\n--- PROCESANDO PAGO ---")
pago = Pago(pedido, "tarjeta")
if pago.procesar_pago():
    print("Pago completado con éxito :)")
else:
    print("Fallo en el pago >:(")

pago.generar_recibo()

if __name__ == "__main__":
    print("DEMO SISTEMA DE RESTAURANTE 3.0 ")
    
    try:
        demo_pedido_completo()
        
        print("\n✨ Prueba completada con éxito ✨")
    
    except Exception as e:
        print(f"\n Error durante la prueba: {str(e)}")