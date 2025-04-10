from fastapi import Depends

from routes.hooks.contracts import HookRequestBody
from routes.factory import RouterFactory
from domain.chat import ChatInteraction

router = RouterFactory(version="v1", tag="chat").get

@router.post("/hook",
             response_description="Hook received from chat channel",
             status_code=201)
async def webhook(request: HookRequestBody,
                  chat_interaction: ChatInteraction = Depends()):
    return chat_interaction.build(request)
