# 🚀 PYNASA: Tu Biblioteca Python para la API de NASA 🌌

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-brightgreen.svg)](https://www.python.org/downloads/release/python-360/)

¡Bienvenido a **PYNASA**! Una biblioteca en Python para interactuar con la API de NASA y explorar el cosmos desde tu consola. 🌠
Documentación: https://pynasa.vercel.app/

## 🌟 Características

- 📸 Obtener la Imagen del Día de la NASA (APOD)
- 🌍 Información de objetos cercanos a la Tierra (NEO)
- 🛰️ Datos de misiones espaciales y mucho más...

## 🚀 Instalación

Instalar **PYNASA** es muy sencillo:

```bash
pip install pynasa
```

## 🛠️ Uso Básico

Aquí tienes un ejemplo sencillo para obtener la Imagen del Día de la NASA (APOD):

```python
import pynasa
from pynasa.core.types.apod import Apod

API = pynasa.NASA(api_key="DEMO_KEY")
apod: Apod = API.apod()

print(f"🌌 Título: {apod.title}")
```

## 📚 Documentación

Para más ejemplos y detalles de uso, visita nuestra [documentación](https://github.com/techatlasdev/pynasa).

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama (`git checkout -b feature/nueva-feature`).
3. Realiza tus cambios y haz un commit (`git commit -am 'Añadir nueva-feature'`).
4. Haz un push a la rama (`git push origin feature/nueva-feature`).
5. Abre un Pull Request.

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 📬 Contacto

Para cualquier pregunta o sugerencia, por favor abre un issue en el repositorio o contacta a [gjimenezdeza@gmail.com](mailto:gjimenezdeza@gmail.com).

¡Gracias por usar `pynasa`! 🚀
