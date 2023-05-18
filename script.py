pip install selenium

apt-get install chromium
from selenium from webdriver

import time

url = 'https://youtu.be/ROynRDePgT4'  # URL del sitio web a visitar

num_visitas = 10  # Número de visitas a generar

tiempo_visita = 10  # Tiempo en segundos para permanecer en la página

# Configuración del navegador

options = webdriver.ChromeOptions()

options.add_argument('--headless')  # Ejecución en segundo plano, sin ventana del navegador

driver = webdriver.Chrome(options=options)

for _ in range(num_visitas):

    driver.get(url)

    print(f'Visita iniciada: {driver.current_url}')

    time.sleep(tiempo_visita)

    print(f'Visita completada: {driver.current_url}')

driver.quit()  # Cerrar el navegador al finalizar
