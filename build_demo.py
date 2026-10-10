"""Generate static portfolio demo pages (fictional content, no client PII)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
BRAND = "NORDEX"
BRAND_SUB = "KFZ · SACHVERSTÄNDIGENBÜRO"
SITE_TITLE = f"{BRAND} — Kfz-Sachverständigenbüro (Portfolio-Demo)"


def head(title: str, description: str, base: str = "./") -> str:
    return f"""<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
    <title>{title}</title>
    <meta name="description" content="{description}" />
    <meta name="robots" content="noindex, nofollow" />
    <link rel="icon" href="{base}assets/favicon.png" type="image/png" sizes="32x32" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Source+Sans+3:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="{base}css/styles.css?v=1" />
    <link rel="stylesheet" href="{base}css/demo-banner.css?v=1" />
  </head>"""


def demo_banner() -> str:
    return """
    <div class="portfolio-demo-banner" role="note">
      <strong>Portfolio-Demo</strong> — Layout &amp; UI-Showcase von einem Kfz-Sachverständigen-Auftritt.
      Fiktive Inhalte, keine echte Praxis.
    </div>"""


def header(active: str = "home", base: str = "./") -> str:
    links = [
        ("home", f"{base}index.html", "HOME"),
        ("about", f"{base}ueber-uns.html", "Über uns"),
        ("services", f"{base}leistungen/index.html", "Leistungen"),
        ("contact", f"{base}kontakt.html", "Kontakt"),
    ]
    menu = []
    for key, href, label in links:
        cur = ' aria-current="page"' if key == active else ""
        menu.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return f"""
  <body>
    {demo_banner()}
    <a class="skip" href="#main">Zum Hauptinhalt springen</a>
    <header class="header">
      <div class="nav">
        <a class="brand" href="{base}index.html">
          <span class="brand-mark-slot">
            <img class="brand-mark" src="./assets/logo-monogram.png" width="290" height="280" alt="" />
          </span>
          <span class="brand-text">
            <span class="brand-name">{BRAND}</span>
            <span class="brand-sub">{BRAND_SUB}</span>
          </span>
        </a>
        <div class="nav-divider" aria-hidden="true"></div>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-label="Menü">
          <span class="menu-toggle__icon" aria-hidden="true"></span>
          <span class="menu-toggle__label">Menü</span>
        </button>
        <ul class="menu">{"".join(menu)}</ul>
        <div class="nav-divider nav-divider-end" aria-hidden="true"></div>
        <div class="header-contact">
          <a class="btn btn-inquiry" href="{base}kontakt.html">Anfrage</a>
        </div>
      </div>
    </header>"""


def footer(base: str = "./") -> str:
    return f"""
    <footer class="footer">
      <div>
        <strong>{BRAND} Kfz-Sachverständigenbüro</strong><br />
        Demo-Website · Musterstadt, Deutschland
      </div>
      <nav>
        <a href="{base}impressum.html">Impressum (Demo)</a>
        <a href="{base}kontakt.html">Kontakt</a>
      </nav>
      <p class="muted">Portfolio-Showcase. Keine Rechtsberatung. Keine echten Kontaktdaten.</p>
    </footer>
    <script src="{base}js/main.js?v=1" defer></script>
  </body>
</html>"""


def write(path: str, body: str) -> None:
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))


def page_index() -> None:
    body = (
        head(
            f"Kfz-Sachverständiger — {SITE_TITLE}",
            "Portfolio-Demo: Unfallgutachten, Fahrzeugbewertung und klarer Ablauf — Layout-Showcase.",
        )
        + header("home")
        + """
    <main id="main">
    <section class="hero hero--home hero--slideshow hero--centered" data-section="hero" data-hero-slider aria-label="Startseite Demo">
      <div class="hero__slides" aria-hidden="true">
        <img class="hero__slide is-active" src="assets/hero/slide-1.jpg" srcset="assets/hero/slide-1-640w.jpg 640w, assets/hero/slide-1-1280w.jpg 1280w, assets/hero/slide-1.jpg 1920w" sizes="100vw" alt="" width="1920" height="1080" loading="eager" decoding="async" fetchpriority="high" />
        <img class="hero__slide" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 1080'%3E%3C/svg%3E" data-src="assets/hero/slide-2.jpg" alt="" width="1920" height="1080" decoding="async" />
        <img class="hero__slide" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 1080'%3E%3C/svg%3E" data-src="assets/hero/slide-3.jpg" alt="" width="1920" height="1080" decoding="async" />
      </div>
      <div class="hero__overlay" aria-hidden="true"></div>
      <div class="hero__inner hero__inner--centered">
        <div class="hero__content hero__content--centered">
          <h1 class="hero__title">Kfz-Sachverständiger für Unfall &amp; Bewertung</h1>
          <p class="hero__region">Region Nord · Demo-Inhalte</p>
          <p class="hero__description">Strukturierte Schadenaufnahme, klare Kommunikation und verständliche Gutachten — so könnte ein moderner Sachverständigen-Auftritt wirken.</p>
          <div class="hero-actions hero-actions--centered">
            <div class="hero-actions__row">
              <a class="btn btn-primary hero-cta-primary" href="./kontakt.html">Kontakt aufnehmen</a>
              <a class="btn btn-outline-light hero-cta-tertiary" href="./leistungen/index.html">Leistungen ansehen</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section home-section home-expert" data-section="expert">
      <div class="expert-spotlight expert-spotlight--premium expert-spotlight--composed">
        <div class="expert-spotlight__media">
          <img class="expert-spotlight__photo" src="assets/service/service-bewertung.jpg" alt="Werkstatt und Dokumentation — Platzhalterbild" width="1280" height="720" loading="lazy" decoding="async" />
        </div>
        <div class="expert-spotlight__content">
          <h2 class="expert-spotlight__title">
            <span class="kicker">Qualifikation &amp; Erfahrung</span>
            <span class="expert-spotlight__name">Ihr Sachverständigenteam</span>
          </h2>
          <p class="expert-spotlight__role">Demo-Profil · fiktive Angaben</p>
          <ul class="expert-credentials">
            <li>Kfz-Technik &amp; Schadenbewertung</li>
            <li>Unabhängige Begutachtung</li>
            <li>Mobile Schadenaufnahme</li>
            <li>Verständliche Ergebnisdarstellung</li>
          </ul>
          <a class="btn btn-outline-copper" href="./ueber-uns.html">Mehr erfahren</a>
        </div>
      </div>
    </section>

    <section class="section content-light home-section home-services" data-section="services">
      <header class="section-header section-header--center">
        <h2>Leistungen im Überblick</h2>
        <p class="section-intro">Typische Leistungsbereiche — als Layout-Beispiel für eine Praxis-Website.</p>
      </header>
      <div class="service-grid">
        <article class="service-card">
          <div class="service-card__media"><img src="assets/service/service-unfall.jpg" alt="Schadendetail am Fahrzeug" width="1280" height="720" loading="lazy" /></div>
          <div class="service-card__body">
            <h3>Unfallgutachten</h3>
            <p>Schadenaufnahme und technische Dokumentation.</p>
            <a class="service-card__link" href="./leistungen/unfallgutachten.html">Mehr erfahren</a>
          </div>
        </article>
        <article class="service-card">
          <div class="service-card__media"><img src="assets/service/service-bewertung.jpg" alt="Fahrzeugbewertung" width="1280" height="720" loading="lazy" /></div>
          <div class="service-card__body">
            <h3>Fahrzeugbewertung</h3>
            <p>Wertermittlung nach Anlass und Fahrzeugtyp.</p>
            <a class="service-card__link" href="./leistungen/index.html">Mehr erfahren</a>
          </div>
        </article>
        <article class="service-card">
          <div class="service-card__media"><img src="assets/service/service-wohnmobile.jpg" alt="Wohnmobil" width="1280" height="720" loading="lazy" /></div>
          <div class="service-card__body">
            <h3>Wohnmobile</h3>
            <p>Begutachtung von Freizeitfahrzeugen.</p>
            <a class="service-card__link" href="./leistungen/index.html">Mehr erfahren</a>
          </div>
        </article>
        <article class="service-card">
          <div class="service-card__media"><img src="assets/service/service-oldtimer.jpg" alt="Oldtimer" width="1280" height="720" loading="lazy" /></div>
          <div class="service-card__body">
            <h3>Oldtimer</h3>
            <p>Klassiker und Youngtimer bewerten.</p>
            <a class="service-card__link" href="./leistungen/index.html">Mehr erfahren</a>
          </div>
        </article>
      </div>
    </section>
    </main>"""
        + footer()
    )
    write("index.html", body)


def main() -> None:
    page_index()

    write(
        "ueber-uns.html",
        head(f"Über uns — {BRAND} Demo", "Demo-Seite: Über uns mit Spotlight-Layout.")
        + header("about")
        + """
    <main id="main">
      <section class="section content-light">
        <header class="section-header section-header--center">
          <h1>Über uns</h1>
          <p class="section-intro">Diese Seite zeigt Typografie, Abstände und Inhaltsstruktur — ohne echte Personendaten.</p>
        </header>
        <div class="expert-spotlight expert-spotlight--premium">
          <div class="expert-spotlight__media">
            <img class="expert-spotlight__photo" src="assets/service/service-unfall.jpg" alt="" width="1280" height="720" loading="lazy" />
          </div>
          <div class="expert-spotlight__content">
            <h2 class="expert-spotlight__title"><span class="expert-spotlight__name">Unabhängige Begutachtung</span></h2>
            <p>Der Auftritt kombiniert seriöse Farben (Navy &amp; Kupfer), klare Navigation und serviceorientierte Karten — optimiert für Desktop und Mobil.</p>
          </div>
        </div>
      </section>
    </main>"""
        + footer(),
    )

    write(
        "leistungen/index.html",
        head(f"Leistungen — {BRAND} Demo", "Demo: Leistungsübersicht mit Bildkarten.", "../")
        + header("services", "../")
        + """
    <main id="main">
      <section class="section content-light home-services">
        <header class="section-header section-header--center">
          <h1>Leistungen</h1>
          <p class="section-intro">Auswahl typischer Gutachter-Leistungen — nur zur Darstellung des Layouts.</p>
        </header>
        <div class="service-grid">
          <article class="service-card">
            <div class="service-card__media"><img src="../assets/service/service-unfall.jpg" alt="" width="1280" height="720" loading="lazy" /></div>
            <div class="service-card__body"><h3>Unfallgutachten</h3><p>Schaden dokumentieren.</p><a class="service-card__link" href="./unfallgutachten.html">Details</a></div>
          </article>
          <article class="service-card">
            <div class="service-card__media"><img src="../assets/service/service-bewertung.jpg" alt="" width="1280" height="720" loading="lazy" /></div>
            <div class="service-card__body"><h3>Fahrzeugbewertung</h3><p>Werte ermitteln.</p><a class="service-card__link" href="../kontakt.html">Anfragen</a></div>
          </article>
        </div>
      </section>
    </main>"""
        + footer("../"),
    )

    write(
        "leistungen/unfallgutachten.html",
        head(f"Unfallgutachten — {BRAND} Demo", "Demo-Unterseite mit Hero und Textspalten.", "../")
        + header("services", "../")
        + """
    <main id="main">
      <section class="hero hero--subpage" aria-label="Unfallgutachten">
        <div class="hero__slides" aria-hidden="true">
          <img class="hero__slide is-active" src="../assets/service/service-unfall.jpg" alt="" width="1280" height="720" />
        </div>
        <div class="hero__overlay" aria-hidden="true"></div>
        <div class="hero__inner"><div class="hero__content">
          <h1 class="hero__title">Unfallgutachten</h1>
          <p class="hero__description">Beispiel einer Leistungs-Unterseite mit Hero-Bild und klarer Hierarchie.</p>
        </div></div>
      </section>
      <section class="section content-light">
        <div class="content-narrow">
          <h2>Ablauf (Demo-Text)</h2>
          <p>Nach Kontaktaufnahme erfolgt die Begutachtung am Fahrzeug. Ergebnisse werden strukturiert dokumentiert — hier nur als Platzhaltertext.</p>
          <p><a class="btn btn-primary" href="../kontakt.html">Zur Kontaktseite</a></p>
        </div>
      </section>
    </main>"""
        + footer("../"),
    )

    write(
        "kontakt.html",
        head(f"Kontakt — {BRAND} Demo", "Demo-Kontaktseite mit Formular-Layout.")
        + header("contact")
        + """
    <main id="main">
      <section class="section content-light">
        <header class="section-header section-header--center">
          <h1>Kontakt</h1>
          <p class="section-intro">Formular und Kontaktblöcke als UI-Demo — keine Daten werden versendet.</p>
        </header>
        <div class="content-narrow">
          <p><strong>Demo-Hinweis:</strong> Felder sind deaktiviert. In der Live-Version würde hier eine sichere Anfrage laufen.</p>
          <form class="contact-form" action="#" method="post" onsubmit="return false;">
            <label>Name<input type="text" name="name" disabled placeholder="Mustername" /></label>
            <label>E-Mail<input type="email" name="email" disabled placeholder="demo@example.com" /></label>
            <label>Nachricht<textarea name="message" rows="5" disabled placeholder="Ihre Nachricht (Demo)"></textarea></label>
            <button type="submit" class="btn btn-primary" disabled>Anfrage senden (Demo)</button>
          </form>
        </div>
      </section>
    </main>"""
        + footer(),
    )

    write(
        "impressum.html",
        head(f"Impressum — {BRAND} Demo", "Demo-Impressum ohne echte Anbieterdaten.")
        + header("home")
        + """
    <main id="main">
      <section class="section content-light">
        <div class="content-narrow legal-text">
          <h1>Impressum (Demo)</h1>
          <p>Diese Website ist ein Portfolio-Showcase. Es handelt sich nicht um eine echte Geschäftspräsenz.</p>
          <p>Verantwortlich für das Demo-Projekt: siehe Repository-Beschreibung (Portfolio-Layout, keine echte Praxis).</p>
        </div>
      </section>
    </main>"""
        + footer(),
    )


if __name__ == "__main__":
    main()
