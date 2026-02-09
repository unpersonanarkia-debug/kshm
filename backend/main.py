from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from email_utils import send_email_with_pdf

app = FastAPI()

@app.post("/api/order_report")
async def order_report(request: Request):
    data = await request.json()
    name = data["name"]
    email = data["email"]
    haplo = data["haplogroup"]
    notes = data.get("notes", "")

    story_html = generate_story_html(fetch_full_haplogroup_data(haplo), user_name=name, notes=notes)
    pdf_file = generate_pdf(story_html, filename=f"{haplo}_{name.replace(' ', '_')}.pdf")

    send_email_with_pdf(email, haplo, story_html, pdf_file, user_name=name)

    return JSONResponse({"message": "Raportti tilattu onnistuneesti."})
