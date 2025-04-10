from typing import List

from pydantic import BaseModel, Field

class ConversationalBody(BaseModel):
    role: str = Field(..., description="Role assumed by agent")
    content: str = Field(..., description="Content data sent by user")


class HookRequestBody(BaseModel):
    body: List[ConversationalBody] = Field(..., description="Prompt requested")

    class Config:
        json_schema_extra = {
            "body": [
                        {"role": "user", "content": "preciso de ajuda"},
                        {"role": "assistant", "content": "ok, vou te ajudar"}           
            ]
        }