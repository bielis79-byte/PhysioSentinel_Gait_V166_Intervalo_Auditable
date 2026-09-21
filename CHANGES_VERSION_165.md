# PhysioSentinel Gait V165

## Pestaña 10 actualizada

### ICLM 0.2 capacidad locomotora

- La ayuda técnica ya no queda desconectada de la independencia funcional.
- La puntuación efectiva utiliza la condición más limitante entre la selección clínica y la ayuda registrada.
- Dos muletas, caminador o rollator limitan el ICLM a 49/100.
- Bastón o una muleta limitan el ICLM a 69/100.
- Si no existe velocidad calibrada, la cadencia entra como respaldo de ritmo, sin presentarse como velocidad.
- Cadencias inferiores a 50 pasos/min limitan el ICLM a 49/100 y las inferiores a 70 pasos/min a 69/100.
- La velocidad medida en m/s continúa teniendo prioridad cuando está disponible.

### ICBF e ICS 0.5 perfil biomecánico

- El perfil frontal incorpora un dominio distal proyectado de rodilla y pie con un peso del 20 por ciento.
- El dominio integra magnitud y diferencia bilateral de rodilla, valgo dinámico proyectado, progresión del pie y diferencia bilateral de retropié.
- Los pesos frontales son pelvis 23 por ciento, tronco 20 por ciento, COM y BOS 22 por ciento, hombros y pelvis 15 por ciento y control distal 20 por ciento.
- Se mantiene la agregación no compensatoria de 65 por ciento de media ponderada y 35 por ciento del peor dominio.
- La interfaz declara expresamente que el dominio distal es una proyección 2D y no diagnostica valgo, rotación ni pronación 3D.
- La rotación axial real de tronco y pelvis continúa fuera de la puntuación cuando solo existe una cámara frontal.

## Caso de regresión Pau

El caso que motivó la revisión mostraba dos muletas, marcha visualmente muy lenta y alteraciones distales claras. En V164 la ayuda técnica podía coexistir con independencia predeterminada y la lentitud no entraba sin velocidad métrica. En V165 dos muletas activan automáticamente un techo de 49/100 y la cadencia actúa como respaldo cuando falta velocidad. Las alteraciones de rodilla y pie dejan de ser invisibles para el ICBF.

## Elementos congelados

No se modifica el tracking, la segmentación temporal, SKEL, Denver, el atlas anatómico, la cinemática 3D ni los exportadores de vídeo. Los cambios se limitan a la puntuación, presentación y exportación de la pestaña 10.
