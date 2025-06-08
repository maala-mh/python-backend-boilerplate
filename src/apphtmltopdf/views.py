import os
import io
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, Response, FileResponse, StreamingResponse
from weasyprint import HTML


from libhtmltopdf.models import contracts


router = APIRouter()


@router.get("/hc")
def execute():
    return {"message": "ok"}


@router.post("/convert-to-pdf")
def execute(payload: contracts.GeneratePdfRequestPayload):
    html = HTML(string=payload.html)
    pdf_bytes = html.write_pdf()
    return StreamingResponse(io.BytesIO(pdf_bytes), media_type="application/pdf",
                             headers={"Content-Disposition": "inline; filename=output.pdf"})

