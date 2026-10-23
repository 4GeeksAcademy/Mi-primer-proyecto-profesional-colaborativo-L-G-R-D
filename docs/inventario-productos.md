# Maison RDL — Inventario de productos

Tarea: [T03](../tasks/T03-inventario.md). Responsable: Daniel. Actualizado: 23/10/2026.
Estado: inventario base integrado; nuevas imágenes de esta actualización pendientes de revisión de Gaby e integración.

> **Datos ficticios.** Maison RDL es una marca inventada para un prototipo académico. Productos, referencias, precios, tallas, materiales y descripciones son de demostración: no existen, no se venden y no describen artículos reales. No hay existencias, envíos ni condiciones comerciales.

Fuente común para las cinco páginas: inicio (T04), catálogo (T05), producto (T06), carrito (T07) y checkout (T08). Copiar los datos tal como aparecen aquí; no crear nombres, precios ni referencias distintos por página. Imágenes y procedencia: [fuentes de imágenes](fuentes-imagenes.md).

## Acuerdos y pendientes que afectan a los datos

| Tema | Estado | Qué se usa en este documento |
| --- | --- | --- |
| Idioma | Confirmado por Lydia el 23/10/2026 para completar la demostración. | Español (`lang="es"`). |
| Moneda | Confirmada por Lydia el 23/10/2026 para completar la demostración. | Euro (EUR). El carrito muestra dos decimales; los precios enteros de las fichas conservan el mismo valor. |
| Impuestos | Supuesto de demostración confirmado por Lydia; no es fiscalidad real ni requisito del enunciado. | Impuesto de simulación del 20 % incluido en los precios; se desglosa, no se suma de nuevo. |
| Cantidades del carrito | Confirmadas por Lydia. | Una unidad de cada una de las tres referencias de T07. |
| Talla de cada línea del carrito | Selección autorizada por Lydia entre las tallas disponibles. | Camisa M, pantalón 38 y mocasín 42; ver supuesto de importes. |
| Imágenes de 16 productos | Completadas por petición de Roger el 23/10/2026. | Imágenes de muestra generadas para cada referencia; ver [fuentes](fuentes-imagenes.md). |

Si cambia la moneda, cambian todos los precios de este documento en el mismo cambio.

## Productos propuestos para el carrito (T07)

Los tres tienen imagen propia de muestra y todos sus datos completos. Las fichas completas están más abajo.

| Línea | Referencia | Nombre | Categoría | Tallas disponibles | Precio unitario | Imagen |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | MRDL-CAM-001 | Camisa de seda marfil | Camisas | XS, S, M, L, XL | 240 € | assets/images/shirt.webp |
| 2 | MRDL-PAN-001 | Pantalón ancho de pinzas taupe | Pantalones | 34, 36, 38, 40, 42, 44 | 295 € | assets/images/trousers.webp |
| 3 | MRDL-CAL-001 | Mocasín de piel espresso | Calzado | 39, 40, 41, 42, 43, 44, 45 | 390 € | assets/images/shoes.webp |

### Supuesto de importes

Confirmado por Lydia el 23/10/2026 para completar T07. Registro en la fuente común para coordinación y revisión de Daniel, responsable del inventario; no se atribuye aprobación a Daniel ni se han enviado mensajes en su nombre. Roger mantiene la dirección del diseño.

**Supuesto del ejercicio, no implementación fiscal real:** precios en EUR con un impuesto de simulación del 20 % incluido. Español e importes con dos decimales. Datos estáticos, sin persistencia ni recálculo automático.

| Referencia | Talla elegida | Precio unitario con impuesto incluido | Cantidad | Total de línea con impuesto incluido |
| --- | --- | --- | --- | --- |
| MRDL-CAM-001 | M | 240,00 € | 1 | 240,00 € |
| MRDL-PAN-001 | 38 | 295,00 € | 1 | 295,00 € |
| MRDL-CAL-001 | 42 | 390,00 € | 1 | 390,00 € |

- Total de cada línea = precio unitario × cantidad. Total con impuestos incluidos = 240,00 + 295,00 + 390,00 = **925,00 €**.
- Desglose sobre el total del pedido: subtotal sin impuestos = 925,00 / 1,20 = 770,8333...; redondeado a dos decimales = **770,83 €**.
- Regla de presentación: redondeo al céntimo más próximo, con mitades hacia arriba. El impuesto se obtiene por diferencia entre el total incluido y el subtotal redondeado: 925,00 - 770,83 = **154,17 €**.
- Conciliación: subtotal sin impuestos 770,83 + impuestos incluidos 154,17 = total **925,00 €**. No sumar otra vez los impuestos al total ni aplicar el 20 % sobre el precio ya incluido para extraerlos.

Se conserva el esquema de [T07](../tasks/T07-estructura-carrito.md#esquema-de-importes), concretado aquí con la modalidad de impuestos incluidos. Sin portes, descuentos ni otros cargos. La revisión de Daniel de este registro queda pendiente; los valores solicitados por Lydia ya están definidos para la demostración.

## Resumen de los veinte productos

Cinco productos por categoría. Tallas: camisas en letras (XS–XL); pantalones en tallas francesas 34–44; calzado en numeración europea; accesorios en «Única», centímetros (cinturón) o letras (guantes).

| Referencia | Nombre | Categoría | Tallas | Precio | Imagen |
| --- | --- | --- | --- | --- | --- |
| MRDL-CAM-001 | Camisa de seda marfil | Camisas | XS, S, M, L, XL | 240 € | Propia de muestra |
| MRDL-CAM-002 | Camisa de popelín blanca | Camisas | XS, S, M, L, XL | 165 € | Propia de muestra |
| MRDL-CAM-003 | Camisa de lino arena | Camisas | S, M, L, XL | 175 € | Propia de muestra |
| MRDL-CAM-004 | Camisa oxford azul niebla | Camisas | S, M, L, XL | 155 € | Propia de muestra |
| MRDL-CAM-005 | Sobrecamisa de lana oliva | Camisas | S, M, L, XL | 285 € | Propia de muestra |
| MRDL-PAN-001 | Pantalón ancho de pinzas taupe | Pantalones | 34, 36, 38, 40, 42, 44 | 295 € | Propia de muestra |
| MRDL-PAN-002 | Pantalón recto de lana carbón | Pantalones | 36, 38, 40, 42, 44 | 270 € | Propia de muestra |
| MRDL-PAN-003 | Pantalón de lino marfil | Pantalones | 34, 36, 38, 40, 42 | 210 € | Propia de muestra |
| MRDL-PAN-004 | Chino de algodón piedra | Pantalones | 36, 38, 40, 42, 44 | 180 € | Propia de muestra |
| MRDL-PAN-005 | Pantalón de pana chocolate | Pantalones | 36, 38, 40, 42, 44 | 230 € | Propia de muestra |
| MRDL-CAL-001 | Mocasín de piel espresso | Calzado | 39, 40, 41, 42, 43, 44, 45 | 390 € | Propia de muestra |
| MRDL-CAL-002 | Bailarina de piel marfil | Calzado | 36, 37, 38, 39, 40, 41 | 320 € | Propia de muestra |
| MRDL-CAL-003 | Botín de ante arena | Calzado | 37, 38, 39, 40, 41, 42, 43, 44 | 450 € | Propia de muestra |
| MRDL-CAL-004 | Zapato derby de piel negra | Calzado | 39, 40, 41, 42, 43, 44, 45 | 410 € | Propia de muestra |
| MRDL-CAL-005 | Sandalia de piel coñac | Calzado | 36, 37, 38, 39, 40, 41 | 280 € | Propia de muestra |
| MRDL-ACC-001 | Bolso de asa corta coñac | Accesorios | Única | 690 € | Propia de muestra |
| MRDL-ACC-002 | Cinturón de piel espresso | Accesorios | 80, 85, 90, 95, 100 (cm) | 140 € | Propia de muestra |
| MRDL-ACC-003 | Pañuelo de seda piedra | Accesorios | Única | 160 € | Propia de muestra |
| MRDL-ACC-004 | Bufanda de cachemira oliva | Accesorios | Única | 260 € | Propia de muestra |
| MRDL-ACC-005 | Guantes de piel chocolate | Accesorios | S, M, L | 170 € | Propia de muestra |

Rango de precios: 140 € a 690 €. Las referencias siguen el patrón `MRDL-<categoría>-<número>`: CAM camisas, PAN pantalones, CAL calzado, ACC accesorios.

## Fichas

Campos de cada ficha: referencia, nombre, categoría, descripción, materiales, uso recomendado, tallas, precio, imagen y texto alternativo. Todas son ficticias.

En «Imagen», **propia de muestra** significa que el archivo existe y muestra este artículo; **pendiente** significa que no hay imagen de este artículo. Para las pendientes se da la ruta prevista (el archivo aún no existe) y el texto alternativo previsto, que debe revisarse cuando exista la imagen. No mostrar la foto de otro artículo como si fuera esta sin decidirlo con Roger y sin ajustar el texto alternativo a lo que se ve.

### Camisas

#### MRDL-CAM-001 — Camisa de seda marfil

- Categoría: Camisas.
- Descripción: camisa de manga larga y corte holgado, con cuello clásico, botonadura delantera, puños con botón y bajo redondeado. La seda le da caída fluida y un brillo discreto.
- Materiales: 100 % seda.
- Uso recomendado: oficina y ocasiones formales; por fuera o metida en un pantalón de tiro alto. Lavado en seco.
- Tallas: XS, S, M, L, XL.
- Precio: 240 €.
- Imagen: propia de muestra, `assets/images/shirt.webp`.
- Texto alternativo: «Camisa de seda marfil de manga larga colgada en una percha de madera».

#### MRDL-CAM-002 — Camisa de popelín blanca

- Categoría: Camisas.
- Descripción: camisa de corte recto con cuello italiano, tapeta oculta y puños redondeados. Popelín de tacto liso y aspecto nítido.
- Materiales: 100 % algodón popelín.
- Uso recomendado: uso diario y trabajo; combina con traje o con vaquero. Lavado a 30 °C y planchado a temperatura media.
- Tallas: XS, S, M, L, XL.
- Precio: 165 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-cam-002.webp`.
- Texto alternativo: «Camisa de popelín blanca de manga larga».

#### MRDL-CAM-003 — Camisa de lino arena

- Categoría: Camisas.
- Descripción: camisa amplia de cuello abierto y manga larga que puede remangarse, con un bolsillo de pecho. Textura natural del lino.
- Materiales: 100 % lino.
- Uso recomendado: primavera y verano, viajes y planes de día. El lino se arruga con el uso; lavado a 30 °C.
- Tallas: S, M, L, XL.
- Precio: 175 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-cam-003.webp`.
- Texto alternativo: «Camisa de lino color arena con cuello abierto».

#### MRDL-CAM-004 — Camisa oxford azul niebla

- Categoría: Camisas.
- Descripción: camisa de cuello abotonado y corte regular en tejido oxford, de un azul grisáceo suave.
- Materiales: 100 % algodón oxford.
- Uso recomendado: uso diario, sola o bajo un jersey o una americana. Lavado a 30 °C.
- Tallas: S, M, L, XL.
- Precio: 155 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-cam-004.webp`.
- Texto alternativo: «Camisa oxford azul niebla con cuello abotonado».

#### MRDL-CAM-005 — Sobrecamisa de lana oliva

- Categoría: Camisas.
- Descripción: sobrecamisa de corte recto con dos bolsillos de parche en el pecho y botones en tono oscuro. Tejido grueso que funciona como capa ligera.
- Materiales: 80 % lana, 20 % poliamida.
- Uso recomendado: otoño e invierno, sobre una camiseta o una camisa fina. Lavado en seco.
- Tallas: S, M, L, XL.
- Precio: 285 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-cam-005.webp`.
- Texto alternativo: «Sobrecamisa de lana verde oliva con bolsillos de parche».

### Pantalones

#### MRDL-PAN-001 — Pantalón ancho de pinzas taupe

- Categoría: Pantalones.
- Descripción: pantalón de tiro alto y pierna ancha con dos pinzas delanteras, trabillas, bolsillos laterales y raya marcada.
- Materiales: crepé de lana; 100 % lana.
- Uso recomendado: oficina y eventos; con camisa metida y calzado plano o de tacón bajo. Lavado en seco.
- Tallas: 34, 36, 38, 40, 42, 44.
- Precio: 295 €.
- Imagen: propia de muestra, `assets/images/trousers.webp`.
- Texto alternativo: «Pantalón ancho de pinzas color taupe colgado de una percha de madera».

#### MRDL-PAN-002 — Pantalón recto de lana carbón

- Categoría: Pantalones.
- Descripción: pantalón de pierna recta y tiro medio, cierre con cremallera y botón, y bolsillos traseros con vivo.
- Materiales: 98 % lana, 2 % elastano.
- Uso recomendado: trabajo y ocasiones formales; admite americana a juego o jersey fino. Lavado en seco.
- Tallas: 36, 38, 40, 42, 44.
- Precio: 270 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-pan-002.webp`.
- Texto alternativo: «Pantalón recto de lana gris carbón».

#### MRDL-PAN-003 — Pantalón de lino marfil

- Categoría: Pantalones.
- Descripción: pantalón amplio de cintura elástica con cordón interior y bolsillos laterales. Ligero y transpirable.
- Materiales: 100 % lino.
- Uso recomendado: verano, viajes y planes de costa. Lavado a 30 °C.
- Tallas: 34, 36, 38, 40, 42.
- Precio: 210 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-pan-003.webp`.
- Texto alternativo: «Pantalón amplio de lino color marfil».

#### MRDL-PAN-004 — Chino de algodón piedra

- Categoría: Pantalones.
- Descripción: chino de corte recto ligeramente estrecho en el bajo, con bolsillos al bies y pinza discreta.
- Materiales: 97 % algodón, 3 % elastano.
- Uso recomendado: uso diario y fines de semana; con camisa oxford o punto. Lavado a 30 °C.
- Tallas: 36, 38, 40, 42, 44.
- Precio: 180 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-pan-004.webp`.
- Texto alternativo: «Pantalón chino de algodón color piedra».

#### MRDL-PAN-005 — Pantalón de pana chocolate

- Categoría: Pantalones.
- Descripción: pantalón de pana de canalé fino, corte recto y tiro medio, con cinco bolsillos.
- Materiales: 99 % algodón, 1 % elastano.
- Uso recomendado: otoño e invierno, con punto grueso o sobrecamisa. Lavado a 30 °C del revés.
- Tallas: 36, 38, 40, 42, 44.
- Precio: 230 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-pan-005.webp`.
- Texto alternativo: «Pantalón de pana marrón chocolate».

### Calzado

#### MRDL-CAL-001 — Mocasín de piel espresso

- Categoría: Calzado.
- Descripción: mocasín de puntera alargada y redondeada con antifaz cosido, forro en piel y suela fina de cuero con tacón bajo.
- Materiales: exterior y forro de piel de becerro; suela de cuero.
- Uso recomendado: oficina y ocasiones formales o de día; con pantalón de vestir o chino. Evitar la lluvia intensa; limpiar con crema para piel.
- Tallas: 39, 40, 41, 42, 43, 44, 45.
- Precio: 390 €.
- Imagen: propia de muestra, `assets/images/shoes.webp`.
- Texto alternativo: «Par de mocasines de piel marrón oscuro sobre un suelo de piedra clara».

#### MRDL-CAL-002 — Bailarina de piel marfil

- Categoría: Calzado.
- Descripción: bailarina de punta redondeada y escote cómodo, con plantilla acolchada.
- Materiales: exterior de piel de cordero; forro de piel; suela de goma fina.
- Uso recomendado: uso diario y ciudad; con pantalón tobillero o falda. Limpiar con un paño seco.
- Tallas: 36, 37, 38, 39, 40, 41.
- Precio: 320 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-cal-002.webp`.
- Texto alternativo: «Bailarinas de piel color marfil».

#### MRDL-CAL-003 — Botín de ante arena

- Categoría: Calzado.
- Descripción: botín Chelsea de caña baja con elásticos laterales y tirador trasero.
- Materiales: exterior de ante; forro de piel; suela de goma.
- Uso recomendado: otoño y primavera, uso diario. Aplicar protector para ante y evitar el agua.
- Tallas: 37, 38, 39, 40, 41, 42, 43, 44.
- Precio: 450 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-cal-003.webp`.
- Texto alternativo: «Botines Chelsea de ante color arena».

#### MRDL-CAL-004 — Zapato derby de piel negra

- Categoría: Calzado.
- Descripción: zapato derby de cordones con pala lisa y acabado pulido.
- Materiales: exterior y forro de piel de becerro; suela de cuero.
- Uso recomendado: ocasiones formales y trabajo; con traje o pantalón de lana. Limpiar con crema para piel.
- Tallas: 39, 40, 41, 42, 43, 44, 45.
- Precio: 410 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-cal-004.webp`.
- Texto alternativo: «Zapatos derby de piel negra con cordones».

#### MRDL-CAL-005 — Sandalia de piel coñac

- Categoría: Calzado.
- Descripción: sandalia plana de tiras cruzadas con hebilla en el tobillo.
- Materiales: tiras de piel; plantilla de piel; suela de cuero.
- Uso recomendado: verano, ciudad y vacaciones. Evitar el agua.
- Tallas: 36, 37, 38, 39, 40, 41.
- Precio: 280 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-cal-005.webp`.
- Texto alternativo: «Sandalias planas de piel color coñac».

### Accesorios

#### MRDL-ACC-001 — Bolso de asa corta coñac

- Categoría: Accesorios.
- Descripción: bolso estructurado de líneas rectas y esquinas suaves, con solapa, cierre metálico rectangular en tono latón y asa superior curva.
- Materiales: exterior de piel con pespunte visible; herrajes metálicos en tono latón.
- Uso recomendado: de día y de tarde, llevado a mano. Guardar en su funda y limpiar con un paño seco.
- Tallas: Única.
- Precio: 690 €.
- Imagen: propia de muestra, `assets/images/bag.webp`.
- Texto alternativo: «Bolso de piel color coñac con asa superior sobre un bloque de piedra».

#### MRDL-ACC-002 — Cinturón de piel espresso

- Categoría: Accesorios.
- Descripción: cinturón de 3 cm de ancho con hebilla metálica mate y cantos pintados.
- Materiales: piel de becerro; hebilla de latón.
- Uso recomendado: con pantalón de vestir o chino. Talla según el contorno de cintura en centímetros.
- Tallas: 80, 85, 90, 95, 100 (cm).
- Precio: 140 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-acc-002.webp`.
- Texto alternativo: «Cinturón de piel marrón oscuro con hebilla metálica».

#### MRDL-ACC-003 — Pañuelo de seda piedra

- Categoría: Accesorios.
- Descripción: pañuelo cuadrado de 90 × 90 cm con estampado geométrico en tonos piedra y marfil y bordes enrollados.
- Materiales: 100 % seda de sarga.
- Uso recomendado: al cuello, en el pelo o anudado al asa de un bolso. Lavado en seco.
- Tallas: Única.
- Precio: 160 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-acc-003.webp`.
- Texto alternativo: «Pañuelo de seda con estampado geométrico en tonos piedra».

#### MRDL-ACC-004 — Bufanda de cachemira oliva

- Categoría: Accesorios.
- Descripción: bufanda larga de punto fino con flecos cortos en los extremos.
- Materiales: 100 % cachemira.
- Uso recomendado: otoño e invierno. Lavado a mano en frío o en seco; secar en plano.
- Tallas: Única.
- Precio: 260 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-acc-004.webp`.
- Texto alternativo: «Bufanda de cachemira verde oliva con flecos».

#### MRDL-ACC-005 — Guantes de piel chocolate

- Categoría: Accesorios.
- Descripción: guantes de piel lisa con forro de punto y pespunte en el dorso.
- Materiales: exterior de piel de cordero; forro de 100 % cachemira.
- Uso recomendado: invierno y ciudad. Limpiar con un paño seco.
- Tallas: S, M, L.
- Precio: 170 €.
- Imagen: propia de muestra, `assets/images/productos/mrdl-acc-005.webp`.
- Texto alternativo: «Guantes de piel marrón chocolate».

## Uso en las páginas

- Copiar referencia, nombre, precio y tallas sin cambios. Si una página necesita un texto más corto, usar el nombre del producto, no una variante nueva.
- El nombre de la categoría debe coincidir con el filtro del catálogo y con los enlaces del footer: Camisas, Pantalones, Calzado y Accesorios.
- Qué productos aparecen en Nuevos lanzamientos y Más vendidos lo decide T04. Esos títulos son secciones de la demo, no datos de ventas reales.
- Los datos visibles de producto.html servirán para el marcado Product de T09; no añadir valoraciones, reseñas, existencias ni promociones.
