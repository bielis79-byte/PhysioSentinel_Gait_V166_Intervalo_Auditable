# PhysioSentinel Gait · Versión 164

V164 mantiene congelados el fitting, `q(t)`, los joints y la anatomía V163. El
cambio se limita a la exportación.

## Exportación integral

- Calidad de captura y sincronización en CSV y JSON.
- Informe completo en TXT, DOCX y PDF.
- Gráfica longitudinal activa y gráfica del perfil biomecánico en PNG.
- Piel SKEL V163 corregida de 75 frames en el NPZ maestro.
- Geometría y transformaciones compactas Denver en NPZ, sin incluir los ZIP
  fuente ni los PKL privados.
- Tablas y gráficos disponibles de las pestañas 4, 5, 9, 10, 11, 12 y 13.
- Diccionario de variables completo.
- Manifiesto de cobertura de las 14 pestañas con estados `exportado`,
  `operativa`, `no disponible` o `pendiente de calcular`.

La aplicación nunca fabrica una salida ausente: si una modalidad no se calculó,
el manifiesto la identifica explícitamente.
