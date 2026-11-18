# HyperFrames

HyperFrames arma videos a partir de páginas web (texto, imágenes, animaciones) y los convierte en MP4.
A diferencia de CapCut o DaVinci, **no se edita con el mouse**: se le pide a Claude lo que querés y Claude arma el video.

## Para qué sirve

- Videos con texto animado, títulos, subtítulos y gráficos
- Reels con la misma estructura para varios negocios (cambia solo la marca)
- Subtítulos automáticos a partir de un video con voz (usa el modelo Parakeet, gratis y local)
- Voz en off y música de fondo gratis, generadas en el propio entorno (Kokoro y MusicGen)
- Presentaciones animadas

## Cómo pedir un video

Decile a Claude, como mínimo:

1. **Para qué negocio** es (regla 1)
2. **El formato**: Reel, feed, YouTube… (regla 3)
3. **El estilo**: tono, ritmo, música (regla 3)
4. **El contenido**: textos, fotos o clips que tiene que usar

Ejemplo: *"Para negocio-a, un Reel de 15 segundos, alegre y rápido, anunciando el 20% de descuento en noviembre. Usá las fotos de `material/`."*

## Qué hace Claude

1. Lee la `ficha-de-marca.md` y los `aprendizajes.md` del negocio (regla 4).
2. Arma el proyecto en `negocios/<negocio>/proyectos/<proyecto>/edicion/`.
3. Revisa cuadros sueltos del video y te muestra una vista previa antes de renderizar.
4. Guarda el video final en `exportados/`.
5. Si corregís algo, lo anota en los aprendizajes del negocio.

## Gratis y pago

| Gratis | Pago (siempre se avisa antes el costo, regla 6) |
|---|---|
| Armar y renderizar videos en este entorno | Voces, imágenes, música y video generados por HeyGen (créditos) |
| Subtítulos con Parakeet | Render en la nube |
| Voz en off con Kokoro (hay voz en español: `ef_dora`) | |
| Música de fondo con MusicGen (tarda unos 30 segundos por cada 3 segundos de música) | |
| Bloques de la biblioteca (transiciones, títulos, efectos) | Funciones Pro: copiar el estilo de un video existente, plantillas de estilo |

## Cuentas y claves

Si algún día hace falta una cuenta de HeyGen, la clave se guarda con `npx hyperframes auth login`, fuera del proyecto. **Nunca** en un archivo `.env` dentro del repositorio (regla 5).

## ElevenLabs (voces pagas)

- La clave de ElevenLabs está guardada en el entorno **Editor-de-Video-Claude** como *Network secret* de `api.elevenlabs.io` (encabezado `xi-api-key`). No está en el proyecto y Claude nunca la ve: el sistema la agrega sola a cada pedido.
- Las herramientas que buscan la variable `ELEVENLABS_API_KEY` se corren con el valor de relleno `ELEVENLABS_API_KEY=proxy-injected`; la clave real la pone el sistema.
- La clave tiene que tener estos permisos en ElevenLabs (*API Keys* → editar la clave):
  - **Voices: Read** → para listar las voces
  - **Text to Speech: Access** → para generar voz
  - **User: Read** → para ver cuántos créditos quedan (y poder avisar el costo, regla 6)
- Generar voz con ElevenLabs consume créditos: siempre se avisa antes (regla 6).

## Datos de uso

El envío de datos de uso a HeyGen está **apagado** (`hyperframes telemetry disable` y la variable `HYPERFRAMES_NO_TELEMETRY=1` del entorno).
