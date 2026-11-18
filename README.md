# Editor de Video — varios negocios

Este repositorio ordena el trabajo de video de **varios negocios**.
Cada negocio tiene su carpeta propia, separada del resto. Lo único que se comparte son las **herramientas**.

## Cómo está organizado

```
herramientas/   → Compartido: guías, formatos, plantillas y recursos genéricos
negocios/       → Una carpeta por negocio (logos, ficha de marca, proyectos)
```

## Reglas básicas

1. **Nada de un negocio va en `herramientas/`.** Si tiene un logo, un color o una música de una marca, va en la carpeta de ese negocio.
2. **Nada de un negocio va en la carpeta de otro.**
3. **Antes de editar, leé la `ficha-de-marca.md`** del negocio con el que vas a trabajar.

## Sumar un negocio nuevo

1. Copiá la carpeta `negocios/_plantilla-negocio/`.
2. Cambiale el nombre por el del negocio (en minúsculas y con guiones, por ejemplo `panaderia-sol`).
3. Completá `marca/ficha-de-marca.md` y cargá los logos en `marca/logos/`.

## Empezar un proyecto nuevo

1. Dentro de `negocios/<negocio>/proyectos/`, copiá la carpeta `AAAA-MM-nombre-del-proyecto`.
2. Cambiale el nombre con la fecha y un nombre corto, por ejemplo `2026-11-promo-navidad`.
3. Poné los clips y fotos en `material/`, trabajá en `edicion/` y guardá el video final en `exportados/`.

## Sobre los videos

Los archivos de video y audio pesan demasiado para GitHub, así que **no se suben** (lo indica el archivo `.gitignore`).
En el repositorio quedan la estructura, las guías y las fichas de marca. Los videos guardalos en Drive o en un disco, respetando la misma estructura de carpetas.
