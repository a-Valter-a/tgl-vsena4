# Tilda landing — централизованный промпт

Промпт **уже подключён глобально** в Cursor. Вводить каждый раз не нужно.

## Где лежит

| Файл | Назначение |
|------|------------|
| `~/.cursor/skills/tilda-landing/SKILL.md` | Полный workflow (автоподхват по URL / «перенеси лендинг») |
| `~/.cursor/rules/tilda-landing.mdc` | Глобальное правило Cursor |

Путь на этом ПК: `C:\Users\nikar\.cursor\skills\tilda-landing\SKILL.md`

## Что писать в новом проекте

Достаточно одного сообщения:

```
Перенеси лендинг в HTML/CSS/JS.
URL: https://example.tilda.ws/
Телефон: +7 (848) 268 85-59
Формы без отправки.
```

Опционально: «без логотипа в хедере», «начни с hero», «свайп без стрелок».

## Что агент делает сам

- Скачивает HTML → сохраняет `page.html`
- Парсит секции Тильды и брейкпоинты
- Качает картинки/шрифты с CDN
- Собирает `index.html`, `css/styles.css`, `js/main.js`

## Если что-то не качается

Тогда можно вручную положить `page.html` / `tilda-source/` — как запасной вариант.

## Другой компьютер

Скопируй папки:
- `C:\Users\nikar\.cursor\skills\tilda-landing\`
- `C:\Users\nikar\.cursor\rules\tilda-landing.mdc`
