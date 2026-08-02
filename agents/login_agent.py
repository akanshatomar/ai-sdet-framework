import os
from google import genai
from utils.prompt_loader import prompt_loader
from utils.json_validator import JSONValidator, TestPlan
from utils.retry_manager import create_retry_decorator
from utils.logger import logger


class LoginAgent:
    """AI Agent that converts user login intent into structured execution steps."""

    def __init__(self, model_name: str = "gemini-2.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing.")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name

    @create_retry_decorator(max_attempts=3, delay_seconds=2)
    def generate_test_plan(self, target_url: str, username: str = "tomsmith", password: str = "SuperSecretPassword!") -> TestPlan:
        """Loads prompt, executes Gemini request, and returns validated TestPlan."""
        logger.info(f"Generating login test plan for URL: {target_url}")

        prompt = prompt_loader.load(
            "login_prompt.txt",
            target_url=target_url,
            username=username,
            password=password
        )

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )

        raw_response = response.text
        logger.debug(f"Raw response from Gemini:\n{raw_response}")

        # Validate structured JSON output
        return JSONValidator.parse_and_validate(raw_response)