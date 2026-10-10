# Kfz-Sachverständigen website (portfolio)

**Live production site:** [https://www.sesa-svb.de/](https://www.sesa-svb.de/)

Static website for an independent automotive expert practice (German market): responsive layout, service pages, contact flow, and brand styling (navy / copper).

This repository holds a **sanitized layout demo** (fictional “NORDEX” branding, no client PII) so recruiters can browse structure and code on GitHub.

**Layout preview (demo):** [pauravi14.github.io/kfz-expert-website-demo](https://pauravi14.github.io/kfz-expert-website-demo/)

## Demo pages in this repo

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

## Stack

- Semantic HTML
- Custom CSS (responsive header, hero, cards)
- Vanilla JS for menu and hero slider

## Note

Layout demo for portfolio reference. Production client site is hosted separately on a custom domain.
