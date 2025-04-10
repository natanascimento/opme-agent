from openai import OpenAI

from core.config import settings
from core.logging import logger
from infrastructure.repository.gpt import GPTRepository


class OpenAiRepository(GPTRepository):

	def __init__(self):
		self._client = OpenAI(api_key=settings.oai.AUTH_TOKEN)

	def setup(self, config):
		return config

	def answer(self, prompt):
		try:
			logger.info(f"Communicating with GPT model")
			model_engine = "gpt-4o-mini"
			prompt = [
					{"role": "system", "content": settings.agent.SYSTEM_ROLE},
					{"role": "user", "content": f"{prompt} \n {settings.user.preference}"},
    		]

			response = self._client.chat.completions.create(
				model=model_engine,
				messages=prompt,
				max_tokens=10000,
				temperature=0.8,
			)

			logger.info(response)

			return response.choices[0].message.content
		except Exception as exception:
			return logger.error(exception)