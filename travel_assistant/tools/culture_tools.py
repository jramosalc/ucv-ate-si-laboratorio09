def get_local_culture_info(destination: str) -> dict:
    """Return basic local culture information for a travel destination.

    Args:
        destination: Travel destination name.

    Returns:
        Dictionary with gastronomy, customs and useful phrases.
    """
    destination_normalized = destination.lower().strip()

    gastronomy = []
    customs = []
    phrases = []

    if "cusco" in destination_normalized or "peru" in destination_normalized:
        gastronomy = ["Cuy al horno", "Chupe de camarones", "Rocoto relleno", "Chicha morada"]
        customs = [
            "Saludar con respeto a los pobladores locales.",
            "Pedir permiso antes de fotografiar personas.",
            "Respetar los sitios arqueológicos y no tocar las ruinas.",
        ]
        phrases = [
            "Allinllachu (¿Cómo estás? en quechua)",
            "Sulpayki (Gracias en quechua)",
            "Maypin? (¿Dónde? en quechua)",
        ]
    elif "arequipa" in destination_normalized:
        gastronomy = ["Rocoto relleno", "Adobo arequipeño", "Chupe de camarones", "Queso helado"]
        customs = [
            "Visitar el centro histórico patrimonio de la UNESCO.",
            "Respetar los horarios de misa en las iglesias coloniales.",
        ]
        phrases = [
            "¡Bienvenido al valle del volcán!",
            "¿Dónde queda el convento de Santa Catalina?",
        ]
    elif "buenos aires" in destination_normalized or "argentina" in destination_normalized:
        gastronomy = ["Asado", "Empanadas", "Medialunas", "Dulce de leche"]
        customs = [
            "El saludo es con un beso en la mejilla.",
            "Las cenas se realizan tarde, generalmente después de las 21:00.",
            "Se valora mucho la conversación y el debate.",
        ]
        phrases = [
            "Che, ¿cómo andás?",
            "¡Bárbaro! (Excelente)",
            "¿Me traés la cuenta? (en restaurantes)",
        ]
    elif "paris" in destination_normalized or "francia" in destination_normalized:
        gastronomy = ["Croissant", "Crêpes", "Boeuf bourguignon", "Macarons"]
        customs = [
            "Siempre saludar con 'Bonjour' al entrar a un comercio.",
            "Las propinas no son obligatorias pero se agradecen.",
            "Hablar en voz baja en espacios públicos.",
        ]
        phrases = [
            "Bonjour (Buenos días)",
            "Merci beaucoup (Muchas gracias)",
            "Où est le métro? (¿Dónde está el metro?)",
            "L'addition, s'il vous plaît (La cuenta, por favor)",
        ]
    else:
        gastronomy = ["Consulta la gastronomía local en guías de viaje actualizadas."]
        customs = ["Investiga las costumbres locales antes de viajar."]
        phrases = ["Aprende al menos: hola, gracias, por favor y ¿dónde está...?"]

    return {
        "status": "success",
        "destination": destination,
        "gastronomy": gastronomy,
        "customs": customs,
        "useful_phrases": phrases,
    }
