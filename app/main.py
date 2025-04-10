from fastapi import FastAPI, Request
import lexnlp.extract.en.dates as dates
import lexnlp.extract.en.entities.nltk_re as entities

app = FastAPI()

@app.post("/extract")
async def extract_entities(request: Request):
    data = await request.json()
    text = data.get("text", "")

    return {
        "dates": [str(d) for d in dates.get_dates(text)],
        "organizations": list(entities.get_organizations(text)),
        "jurisdictions": list(entities.get_jurisdictions(text))
    }
