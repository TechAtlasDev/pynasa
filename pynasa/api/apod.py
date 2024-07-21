from typing import Union
from ..core.api import NasaAPI
from ..core.types.apod import Apod

def get_apod(API: NasaAPI, **kwargs) -> Union[Apod, list[Apod], None]:
    """
    Obtiene la Imagen del Día de la NASA (APOD) utilizando una instancia de NasaAPI.

    Args:
        api (NasaAPI): Instancia de la clase NasaAPI.
        kwargs: Parámetros opcionales para la solicitud, como date, start_date, end_date, count, y thumbs.

    Returns:
        Union[Apod, None]: Instancia de Apod con los datos obtenidos de la API, o None si la solicitud falla o no hay datos disponibles.
    """
    # Llamar al método get_apod de NasaAPI con los parámetros
    response_api = API.get_apod(**kwargs)
    
    if response_api is None:
        # Manejo en caso de no obtener datos
        return None

    return Apod(response_api) if type(response_api) is not list else [Apod(item) for item in response_api]
