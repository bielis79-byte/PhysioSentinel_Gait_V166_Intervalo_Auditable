# PhysioSentinel Gait V165

Versión derivada de V164 con actualización específica de la pestaña 10.

## Instalación

1. Descomprimir el ZIP.
2. Instalar las dependencias de `requirements.txt`.
3. Ejecutar `streamlit run streamlit_app.py`.

## Cambios principales

- ICLM 0.2 con reconciliación automática de ayuda técnica e independencia funcional.
- Respaldo de cadencia cuando no existe velocidad métrica.
- ICBF e ICS 0.5 con dominio distal proyectado de rodilla y pie.
- Nuevas advertencias metodológicas y trazabilidad en la exportación integral.

Consulte `CHANGES_VERSION_165.md` para el detalle de fórmulas, pesos, límites y restricciones.
