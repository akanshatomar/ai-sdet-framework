import json
import re
from typing import List, Optional
from pydantic import BaseModel, Field
from utils.logger import logger


class TestStep(BaseModel):
    step_number: int
    action: str = Field(..., description="navigate, fill, click, or assert_visible")
    selector: str
    value: Optional[str] = ""
    description: str


class TestPlan(BaseModel):
    test_suite: str
    target_url: str
    steps: List[TestStep]


class JSONValidator:
    """Extracts, cleans, and validates structured Pydantic models from LLM text output."""

    @staticmethod
    def parse_and_validate(raw_text: str) -> TestPlan:
        # Strip markdown code blocks if the LLM includes them
        cleaned_text = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw_text.strip(), flags=re.MULTILINE)

        try:
            data = json.loads(cleaned_text)
            validated_plan = TestPlan(**data)
            logger.info(f"Successfully validated test plan: '{validated_plan.test_suite}'")
            return validated_plan
        except (json.JSONDecodeError, Exception) as e:
            logger.error(f"JSON Validation failed: {str(e)}")
            raise ValueError(f"Invalid JSON response from LLM: {str(e)}")