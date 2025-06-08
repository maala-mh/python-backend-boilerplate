from pydantic import BaseModel


class GeneratePdfRequestPayload(BaseModel):
    html: str
