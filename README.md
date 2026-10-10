# Kfz expert office — portfolio demo

Static **portfolio showcase** of a German automotive expert (Sachverständiger) website: navy/copper branding, hero slideshow, service cards, and contact layout.

- **Not a client site** — fictional brand **NORDEX**, placeholder text, no real phone numbers or addresses.
- **Purpose:** demonstrate design and front-end build quality on [GitHub Pages](https://pauravi14.github.io/kfz-expert-website-demo/).

## Pages

| Page | What it shows |
|------|----------------|
| `index.html` | Hero, expert spotlight, service grid |
| `leistungen/` | Service listing + sample detail page |
| `kontakt.html` | Contact form layout (disabled) |
| `ueber-uns.html` | About layout |

## Local preview

```bash
python build_demo.py
python -m http.server 8765
```

Open http://localhost:8765/

## Stack

- Semantic HTML
- Custom CSS (responsive header, hero, cards)
- Vanilla JS (`js/main.js`) for menu and hero slider

## Author

**Pauravi Pardeshi** — portfolio project. Client production sites are separate and not included here.
