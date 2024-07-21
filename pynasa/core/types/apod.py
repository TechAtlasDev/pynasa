from typing import Optional

class Apod():
    """Representa la Imagen del Día de la NASA (APOD)."""
    
    def __init__(self, data):
        """
        Inicializa la instancia de Apod con los datos de la API.
        
        :param data: Datos de respuesta de la API.
        """
        self.date:str = data.get('date')
        self.hdurl:str = data.get('hdurl')
        self.media_type:str = data.get('media_type')
        self.copyright:Optional[str] = data.get("copyright", None)
        self.service_version:str = data.get('service_version')
        self.title:str = data.get('title')
        self.explanation:str = data.get('explanation')
        self.url:str = data.get('url')
