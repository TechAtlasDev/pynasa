import requests
from ..utils.url import joinURL
from ..utils.alerts import handler
from typing import Optional

class NasaAPI:
    """Clase principal para interactuar con la API de NASA."""
    
    def __init__(self, api_key:str):
        """
        Inicializa la clase con la clave de API y la URL base.
        
        :param api_key: Clave de API para autenticar las solicitudes.
        """
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/"

    def _get_url(self, endpoint, params=None):
        """
        Construye la URL completa para una solicitud.
        
        :param endpoint: El endpoint de la API.
        :param params: Parámetros adicionales para la solicitud.
        :return: La URL completa.
        """
        url = joinURL(self.base_url, endpoint)
        if params:
            url += f"?{params}"
        return url

    def get_apod(self, date: Optional[str] = None, 
                 start_date: Optional[str] = None, 
                 end_date: Optional[str] = None,
                 count: Optional[int] = None, 
                 thumbs: bool = False) -> Optional[dict]:
        """
        Obtiene la Imagen del Día de la NASA (APOD) para una fecha específica, un rango de fechas o imágenes aleatorias.

        Args:
            date (Optional[str]): Fecha específica para la APOD en formato 'YYYY-MM-DD'. Si no se proporciona, se obtiene la imagen del día actual.
            start_date (Optional[str]): Fecha de inicio en formato 'YYYY-MM-DD' para un rango de fechas.
            end_date (Optional[str]): Fecha de fin en formato 'YYYY-MM-DD' para un rango de fechas. Si no se proporciona, se usa la fecha actual.
            count (Optional[int]): Número de imágenes aleatorias a devolver. No se puede usar con `date` o `start_date` y `end_date`.
            thumbs (bool): Si es True, devuelve la URL de la miniatura del video. Si no es un video, este parámetro se ignora.

        Returns:
            Optional[dict]: La respuesta JSON de la API, o None si la solicitud falla o no hay datos disponibles.
        """
        endpoint = "planetary/apod"
        params = f"api_key={self.api_key}"
        
        if date:
            params += f"&date={date}"
        if start_date:
            params += f"&start_date={start_date}"
        if end_date:
            params += f"&end_date={end_date}"
        if count:
            params += f"&count={count}"
        if thumbs:
            params += f"&thumbs=True"
        
        url = self._get_url(endpoint, params)
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP no exitosos
        except requests.RequestException as e:
            handler(f"Error al obtener APOD: {e}")  # Usa el manejador de alertas si ocurre un error
            return None
        
        return response.json()

# Ejemplo de uso
if __name__ == "__main__":
    api = NasaAPI(api_key="DEMO_KEY")
    apod_data = api.get_apod()
    if apod_data:
        print(f"Title: {apod_data.get('title')}")
        print(f"Explanation: {apod_data.get('explanation')}")
        print(f"URL: {apod_data.get('url')}")
