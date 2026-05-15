from typing import List


class PromptBuilder:
    def build(self, content: str) -> str:
        return f"Resuma em pontos: {content}"


class LlmApiClient:
    def call(self, prompt: str) -> str:
        return prompt


class ResponseParser:
    def parse(self, response: str) -> List[str]:
        payload = response.replace("Resuma em pontos:", "").strip()
        return [chunk.strip() for chunk in payload.split(".") if chunk.strip()]


class LlmFacade:
    def __init__(
        self,
        builder: PromptBuilder | None = None,
        client: LlmApiClient | None = None,
        parser: ResponseParser | None = None,
    ) -> None:
        self._builder = builder or PromptBuilder()
        self._client = client or LlmApiClient()
        self._parser = parser or ResponseParser()

    def generate_points(self, content: str) -> List[str]:
        prompt = self._builder.build(content)
        response = self._client.call(prompt)
        return self._parser.parse(response)
