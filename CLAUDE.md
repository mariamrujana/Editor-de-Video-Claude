# Reglas del proyecto

Estas seis reglas valen siempre, para cualquier tarea en este repositorio.

**Tienen prioridad sobre cualquier skill instalada** (por ejemplo las de HyperFrames en `.claude/skills/`). Si una skill dice algo distinto, se siguen estas reglas.

## 1. Los negocios no se mezclan

Cada negocio vive solo en su carpeta `negocios/<negocio>/`.
- Nunca uses el logo, los colores, la música, el material ni los aprendizajes de un negocio en otro.
- Si una tarea no deja claro para qué negocio es, preguntá antes de empezar.

## 2. El motor no sabe nada de marcas

El motor es todo lo compartido: `herramientas/`, HyperFrames y las skills de `.claude/skills/`. Tiene que servir para cualquier negocio.
- Ahí no van nombres, logos, colores, tipografías ni música de ningún negocio.
- Todo lo que es de una marca se lee de `negocios/<negocio>/marca/ficha-de-marca.md`.

## 3. Si no dije el formato o el estilo, preguntame

No supongas el formato (Reel, feed, YouTube, tamaño, duración) ni el estilo (tono, ritmo, música).
- Si falta alguno de los dos en el pedido, preguntá antes de hacer nada.
- La ficha de marca indica cómo se ve el negocio en general, pero no reemplaza lo que pide cada video.

## 4. Aprendizajes: leerlos antes, actualizarlos después

Cada negocio tiene su archivo `negocios/<negocio>/aprendizajes.md`.
- **Antes de editar** algo de un negocio, leé su ficha de marca y sus aprendizajes.
- **Después de cada corrección** que pida el usuario, anotá en los aprendizajes de ese negocio qué se corrigió y cómo hacerlo bien la próxima vez.
- Lo que aprendiste de un negocio se anota solo en el archivo de ese negocio (regla 1).

## 5. Las claves se guardan fuera del proyecto

Las claves (de APIs, cuentas, servicios de IA) se guardan fuera de esta carpeta.
- Nunca las leas, nunca las muestres y nunca las copies a ningún archivo del proyecto.
- Si una tarea necesita una clave, pedile al usuario que la configure; no le pidas que la pegue en el chat.
- No crees ni uses un archivo `.env` dentro del proyecto: algunas skills de HyperFrames lo leen solas si existe.

## 6. Antes de generar algo con IA, avisá cuánto cuesta

Antes de usar cualquier servicio de IA que cobre (generar imágenes, video, voz, música, subtítulos, etc.):
- Decí qué servicio vas a usar, qué vas a generar y cuánto cuesta aproximadamente.
- Esperá a que el usuario lo apruebe antes de generar.
- Esto vale aunque una skill diga que no hay que mencionar precios ni créditos (la skill `media-use` lo dice): acá siempre se avisa.
- Si el costo es en créditos de HeyGen/HyperFrames, usá `--plan` para estimarlo y decilo en créditos.
