# Trainingswunsch WebApp (Variante A: GitHub Pages + Power Automate)

Frontend (GitHub Pages) zeigt belegte Slots je Platz/Halbfeld (A/B) und nimmt **3 Wünsche** pro Team entgegen
(2 Pflichtwünsche für die beiden Trainingstage + 1 Fallback). Wünsche werden via **Power Automate HTTP-Flow**
entgegengenommen (CORS + Coach-PIN + Flood-Guard serverseitig).

## Quick Start
1. Repository erstellen (public) und GitHub Pages auf **GitHub Actions** stellen.
2. Dateien aus diesem Projekt in folgende Struktur legen:
   - `site/index.html`
   - `data/trainingsplan.yaml`
   - `data/sperren.yaml` (optional)
   - `tools/plan_to_json.py`
   - `.github/workflows/publish.yml`
3. Workflow ausführen → erzeugt `site/trainingsplan.json`.
4. In `site/index.html` **REPLACE_WITH_YOUR_FLOW_URL** durch deinen Power-Automate-Endpoint ersetzen.
5. Im Flow CORS erlauben (siehe `docs/cors_response_headers.txt`) und das Schema aus `docs/power_automate_flow_schema.json`
   verwenden. **Pro Wunsch** wird eine Zeile in `tblWunsch` gespeichert.

## Datenquellen
- `data/trainingsplan.yaml` → Master-Plan (Belegungen)
- `data/sperren.yaml` → Sperrzeiten (wöchentlich & optional einmalig)
- Workflow merged beides zu `site/trainingsplan.json` (wird vom Frontend geladen).

## Sicherheit (serverseitig)
- **CORS**: Nur `https://<USER>.github.io/<REPO>/`
- **Coach-PIN**: Tabelle `tblCoachPins` (Team, Pin, GueltigBis)
- **Flood-Guard**: Max. 1 Submission je Team / 5 min

## Einbettung Homepage
Per iFrame:
```html
<iframe src="https://<USER>.github.io/wo-trainingswunsch/"
        style="width:100%;height:900px;border:0;border-radius:12px;overflow:hidden"></iframe>
