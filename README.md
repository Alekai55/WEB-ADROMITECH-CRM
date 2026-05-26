# Entorno de Desarrollo y Despliegue - Adromitech CRM

Este documento describe el entorno de desarrollo, las herramientas utilizadas y el stack tecnológico empleado para el proyecto **Adromitech CRM**, junto con la justificación de las decisiones tomadas.

## Acceso a la Aplicación
- **URL de Producción:** [https://app-470ea328-bec6-4c96-9116-f78bf79498d2.cleverapps.io/admin-leads](https://app-470ea328-bec6-4c96-9116-f78bf79498d2.cleverapps.io/admin-leads)

## 1. Entorno de Desarrollo

* **IDE (Entorno de Desarrollo Integrado): Visual Studio Code (VS Code)**
  * **Justificación:** VS Code es un editor de código fuente ligero pero muy potente. Ofrece una excelente integración con Python, un terminal integrado, control de versiones nativo con Git y un extenso ecosistema de extensiones que agiliza el desarrollo (autocompletado, debugging).
  * **Plugins/Extensiones utilizadas/recomendadas:** Python (oficial de Microsoft), Pylance, extensiones de HTML/CSS y Jinja (para las plantillas).

* **Versión de Python: Python 3.12**
  * **Justificación:** Python 3.12 es una de las versiones más recientes y estables. Ofrece mejoras significativas de rendimiento (como optimización en la ejecución), mensajes de error más claros y una excelente compatibilidad con las librerías modernas utilizadas en el proyecto.

* **SGBD (Sistema Gestor de Base de Datos): MySQL**
  * **Justificación:** MySQL es un motor de base de datos relacional robusto, seguro y de alto rendimiento. Es ideal para garantizar la consistencia e integridad de los datos en una aplicación estructurada como un CRM.

* **Gestión de Base de Datos: DBeaver**
  * **Justificación:** DBeaver es una herramienta cliente SQL universal multiplataforma. Su interfaz visual e intuitiva simplificó drásticamente la creación de tablas, administración de la base de datos remota (en Clever Cloud) y visualización/modificación de los datos durante el desarrollo sin necesidad de usar comandos por consola.

## 2. Servidor Web y Framework

* **Framework Web: Flask**
  * **Justificación:** Se eligió Flask por ser un micro-framework de Python ligero, modular y muy flexible. Permite construir la aplicación rápidamente con las herramientas exactas que se necesitan sin sobrecargar el proyecto.
* **Servidor Web en Producción: Gunicorn**
  * **Justificación:** Gunicorn es un servidor HTTP WSGI de nivel de producción. El servidor que trae Flask por defecto es solo para desarrollo. Gunicorn es capaz de procesar múltiples solicitudes concurrentes y asegura que la web funcione de manera estable y rápida para los usuarios finales.

## 3. Despliegue y Alojamiento (Hosting)

* **Plataforma Cloud: Clever Cloud**
  * **Justificación:** Clever Cloud es un proveedor de plataforma como servicio (PaaS) que facilita mucho el paso de desarrollo a producción.
  * **Alojamiento integral:** Permite tener tanto el entorno de ejecución de Python como el add-on de base de datos MySQL centralizados.
  * Su despliegue directo desde Git significa que cada vez que subimos código, la plataforma se encarga de compilarlo, instalar las dependencias (`requirements.txt`) y reiniciar la aplicación automáticamente.

## 4. Librerías de Python utilizadas
Las dependencias principales (listadas en el archivo `requirements.txt`) son:
- `Flask>=3.0.0`: Para la infraestructura y rutas de la web.
- `mysql-connector-python>=8.0.0`: El conector/driver oficial para comunicar nuestro código en Python con la base de datos MySQL alojada en Clever Cloud.
- `gunicorn>=21.0.0`: El servidor WSGI que Clever Cloud ejecuta para mantener la página en línea.
