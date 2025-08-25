# Trainingswunsch WebApp (Variante A, GitHub Pages)

Frontend (Pages) visualisiert belegte Slots und sendet Wünsche an einen Power-Automate-HTTP-Flow.
**Schutz**: CORS (nur von Pages-URL), Coach-PIN (serverseitig prüfen), Flood-Guard (Rate-Limit je Team).

## Quick Start
1. **Repo pushen**, in GitHub unter **Settings → Pages**: Build & Deployment = GitHub Actions.
2. Unter **Actions** den Workflow „Publish Trainingsplan“ ausführen (oder push auf `data/`).
3. In `site/index.html` `REPLACE_WITH_YOUR_FLOW_URL` durch deine Flow-URL ersetzen.
4. Optional: `data/trainingsplan.yaml` anpassen; der Workflow erzeugt `site/trainingsplan.json`.
5. Power Automate Flow: Schema in `docs/power_automate_flow_schema.json`; CORS-Header aus `docs/cors_response_headers.txt` übernehmen.

## Datenmodell
- `data/trainingsplan.yaml` → YAML mit Plätzen, Tagen, Slots (A/B über `halves: true`).
- Workflow baut `site/trainingsplan.json`, die das Frontend lädt.

## Sicherheit (Server)
- CORS: Nur `https://<user>.github.io/wo-trainingswunsch/`
- Coach-PIN: Tabelle `tblCoachPins` (Team, Pin, GueltigBis)
- Flood-Guard: max. 1 Wunsch je Team/5 Minuten
