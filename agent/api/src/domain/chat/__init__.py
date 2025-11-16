from fastapi import Depends

from infrastructure.repository.gpt.openai import OpenAiRepository
from routes.hooks.contracts import HookRequestBody



class ChatInteraction:
    
    def __init__(self,
                 gpt: OpenAiRepository = Depends()):
        self.__gpt = gpt

    def build(self, request: HookRequestBody):
        gpt_response = self.__gpt.answer(prompt=request.body)
        return gpt_response