# PhysioSentinel Gait Version 163

V163 consolida la anatomía Denver validada en V162 y alinea también la piel SKEL
de los pies con el esqueleto. Para ello utiliza los pesos oficiales del modelo
SKEL correspondiente al sexo registrado.

La aplicación requiere, como antes, el ZIP privado `skel_models_v1.1.zip` por el
cargador automático o mediante carga manual. El ZIP debe incluir
`skel_male.pkl` y/o `skel_female.pkl`. El atlas Denver masculino o femenino se
carga aparte y no se incluye en este paquete.

La neutralización no impone una marcha estándar: conserva la variación temporal
de cada paciente y sólo corrige el offset fijo de montaje de la piel del pie.
