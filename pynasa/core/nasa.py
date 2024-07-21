
from typing import Optional, Union

from ..utils.alerts import handler
from ..core.api import NasaAPI

from ..api.apod import get_apod
from ..api.apod import Apod

class NASA:
    def __init__(self, api_key: str="DEMO_KEY"):
        """
        Inicializa la instancia de NASA con la clave API.

        Args:
            api_key (str): Clave API para acceder a los datos de la NASA.
        """
        self.api_key = api_key
        handler().info("Se está usando la DEMO_KEY, puedes conseguir la tuya en https://api.nasa.gov/") if api_key == "DEMO_KEY" else "" 
        self.API = NasaAPI(api_key)

    def apod(self, date: Optional[str] = None, 
             start_date: Optional[str] = None, 
             end_date: Optional[str] = None,
             count: Optional[int] = None, 
             thumbs: bool = False) -> Union[Apod, list[Apod]]:
        """
        Obtiene la Imagen del Día de la NASA (APOD) para una fecha específica, un rango de fechas o imágenes aleatorias.

        Args:
            date (Optional[str]): La fecha para la APOD en formato 'YYYY-MM-DD'. Si es None, se obtiene la APOD de hoy.
            start_date (Optional[str]): Fecha de inicio en formato 'YYYY-MM-DD' para un rango de fechas. No se puede usar con `date`.
            end_date (Optional[str]): Fecha de fin en formato 'YYYY-MM-DD' para un rango de fechas. Si es None, se usa la fecha actual.
            count (Optional[int]): Número de imágenes aleatorias a devolver. No se puede usar con `date` o `start_date` y `end_date`.
            thumbs (bool): Si es True, devuelve la URL de la miniatura del video. Si no es un video, este parámetro se ignora.

        Returns:
            Union[Apod, list[Apod], None]: Una instancia de la clase Apod con los detalles de la Imagen del Día de la NASA,
                                o una lista llena de Apods,
                                o None si la solicitud falla o no hay datos disponibles.
        """
        # Llamar a la función get_apod con todos los parámetros proporcionados
        apod_data = get_apod(
                            API=self.API,
                            date=date, 
                            start_date=start_date, 
                            end_date=end_date, 
                            count=count, 
                            thumbs=thumbs
                            )
        
        # Verificar si se obtuvo una respuesta válida
        if apod_data is None:
            return None

        return apod_data
