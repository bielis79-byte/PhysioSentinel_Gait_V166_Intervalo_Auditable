# PhysioSentinel Gait · Version 162

## Corrección confirmada sobre Alejandro

- Sustituye los frames del pie calculados independientemente por frames
  anatómicos continuos mediante transporte del eje transversal.
- Elimina las soluciones equivalentes que provocaban inversiones próximas a
  180 grados entre frames consecutivos.
- Conserva la neutralización rígida del atlas Denver sin alterar `poses`,
  `q(t)`, joints ni fitting.
- Retira del flujo activo la deformación aproximada de la piel de V161.
- El visor utiliza exactamente los vértices originales de la piel SKEL del NPZ.
- Añade control bilateral de rótula anterior. La corrección, cuando se necesita,
  afecta sólo a la malla patelar y no a fémur, tibia, pelvis o trocánteres.
- Mantiene el control adaptativo de pelvis mediante `axis_map`, sacro posterior
  y selección D/I de pies mediante hallux medial.
- El render se bloquea si el salto temporal del frame del pie supera 35
  grados por frame o falla alguna comprobación anatómica.

## Resultados de validación · `alejandro.npz`

- 75 frames evaluados.
- Salto máximo pie derecho: 18.65 grados/frame.
- Salto máximo pie izquierdo: 20.27 grados/frame.
- Rótulas: corrección bilateral a cara anterior; PASS.
- Pelvis: corrección AP aplicada; sacro posterior; PASS.
- Pies: asignación Denver intercambiada D/I; hallux medial bilateral; PASS.
- Piel SKEL: secuencia original preservada sin deformación de proximidad.

La previsualización fue confirmada visualmente por el usuario antes del
empaquetado definitivo.

