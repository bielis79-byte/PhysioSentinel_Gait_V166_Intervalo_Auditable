# PhysioSentinel Gait V166

Esta versión corrige la coherencia entre el intervalo temporal seleccionado y los productos derivados del análisis.

Al pulsar **Calcular, guardar histórico y eliminar vídeo**, la aplicación convierte los segundos seleccionados a frames. Ese mismo conjunto de frames alimenta las métricas, las curvas, los snapshots cinemáticos y el vídeo anotado descargable.

La interfaz informa después del cálculo del intervalo solicitado, los frames realmente empleados, el número de frames y la duración efectiva. La pequeña diferencia que pueda existir entre los segundos solicitados y la duración efectiva corresponde exclusivamente al redondeo temporal a frames según los FPS del vídeo.

Pose2Sim continúa obteniendo el tracking del vídeo bruto antes de seleccionar el intervalo. Sus controles de identidad globales se conservan como auditoría, claramente diferenciados de las métricas de calidad calculadas dentro del segmento.

