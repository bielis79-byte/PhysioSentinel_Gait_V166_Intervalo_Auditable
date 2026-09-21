# PhysioSentinel Gait V166

## Corrección de trazabilidad del intervalo

- Las métricas, curvas y el vídeo anotado utilizan ahora exactamente el mismo recorte temporal seleccionado en la pestaña 4.
- El vídeo anotado se genera desde el primer frame seleccionado hasta el último, ambos inclusive; deja de exportarse el vídeo completo cuando se ha elegido un subintervalo.
- Se incorporan al histórico y a la exportación el inicio y final solicitados, primer y último frame reales, número de frames y duración efectiva analizada.
- Tras calcular se muestra una confirmación visible del intervalo realmente aplicado.
- Los controles globales de identidad de Pose2Sim quedan etiquetados como controles del vídeo bruto completo y no se presentan como calidad propia del segmento.
- En análisis biplanar se auditan por separado los frames frontal y lateral después de aplicar la sincronización.

## Elementos preservados

- Puntuación locomotora y biomecánica V165 sin cambios.
- Anatomía y cinemática V163 congeladas.
- Persistencia en Supabase limitada a resultados y metadatos; los vídeos continúan eliminándose del servidor temporal.

