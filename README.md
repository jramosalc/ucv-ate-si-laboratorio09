# Travel ADK Multiagent

Laboratorio UCV — Sistema Multiagente de Viajes con Google ADK.

## Arquitectura

```
Usuario
   |
   v
Travel Coordinator Agent
   |-- Web Search Agent
   |-- Itinerary Agent
   |-- Budget Agent
   |-- Risk Reviewer Agent
   |-- Local Culture Agent  ← Reto del laboratorio
   v
Respuesta final consolidada
```

## Agentes

| Agente | Responsabilidad |
|--------|----------------|
| Travel Coordinator Agent | Recibe la solicitud, coordina subagentes y consolida la respuesta. |
| Web Search Agent | Busca información actualizada usando Google Search. |
| Itinerary Agent | Propone un itinerario por días. |
| Budget Agent | Calcula un presupuesto referencial básico. |
| Risk Reviewer Agent | Evalúa riesgos comunes de viaje. |
| Local Culture Agent | Recomienda gastronomía, costumbres y frases útiles. |

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install poetry
poetry install
```

## Variables de entorno

Crear archivo `.env` a partir de `.env.example`:

```bash
cp .env.example .env
# Editar .env y colocar tu GOOGLE_API_KEY
```

## Ejecutar agente por consola

```bash
poetry run adk run travel_assistant
```

## Ejecutar interfaz web

```bash
poetry run adk web --port 8000
```

Abrir: http://localhost:8000

## Ejecutar pruebas

```bash
poetry run pytest
```

## Ejecutar lint

```bash
poetry run ruff check .
```

## Generar reporte de cobertura para SonarCloud

```bash
poetry run pytest --cov=travel_assistant --cov-report=term-missing --cov-report=xml
```

## Flujo Git

```
feature/travel-multiagent → develop → main
```

## Referencias

- [Google ADK](https://adk.dev/)
- [Poetry](https://python-poetry.org/)
- [Pytest](https://docs.pytest.org/)
- [SonarCloud](https://sonarcloud.io/)
