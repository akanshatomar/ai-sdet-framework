from pathlib import Path
from utils.logger import logger


class PromptLoader:
    """Loads and formats prompt templates from the prompts directory."""

    def __init__(self, prompts_dir: str = "prompts"):
        self.prompts_dir = Path(__file__).parent.parent / prompts_dir

    def load(self, filename: str, **kwargs) -> str:
        file_path = self.prompts_dir / filename

        if not file_path.is_file():
            logger.error(f"Prompt template missing at: {file_path}")
            raise FileNotFoundError(f"Prompt template '{filename}' not found.")

        with open(file_path, "r", encoding="utf-8") as f:
            template = f.read()

        rendered = template.format(**kwargs) if kwargs else template
        logger.info(f"Loaded prompt template: '{filename}'")
        return rendered


prompt_loader = PromptLoader()