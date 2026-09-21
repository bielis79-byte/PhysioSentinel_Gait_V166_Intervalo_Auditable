# PhysioSentinel Gait · Versión 163

## Cambio validado

- La piel SKEL de ambos pies elimina el offset visual de flexión plantar mediante
  los pesos oficiales de skinning de `skel_male.pkl` o `skel_female.pkl`.
- La selección del modelo es automática y depende del sexo guardado en Datos del
  paciente/registro.
- Se conserva la forma del pie: el interior se desplaza casi rígidamente y la
  transición del tobillo utiliza el blending oficial de SKEL.
- La corrección es sólo de registro visual. No modifica `q(t)`, joints, fitting,
  amplitud articular ni el patrón individual de marcha.

## Elementos congelados de V162

- Pelvis y sacro con orientación anteroposterior validada.
- Trocánteres, fémures, tibias y peronés.
- Rótulas en la cara anterior.
- Lateralidad de los pies y hallux medial.
- Continuidad temporal antigiros de 180 grados del atlas Denver.

## Seguridad

- La corrección se bloquea si las caras del NPZ no coinciden exactamente con la
  topología oficial SKEL de 6.890 vértices y 13.776 triángulos.
- Los PKL oficiales y los atlas Denver continúan fuera del paquete y de Supabase.
