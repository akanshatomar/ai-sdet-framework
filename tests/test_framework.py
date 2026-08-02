import pytest
from utils.prompt_loader import PromptLoader
from utils.json_validator import JSONValidator, TestPlan


def test_prompt_loader_interpolation(tmp_path):
    prompts_dir = tmp_path / "prompts"
    prompts_dir.mkdir()
    p_file = prompts_dir / "test.txt"
    p_file.write_text("URL is {url}")

    loader = PromptLoader(prompts_dir=str(prompts_dir))
    res = loader.load("test.txt", url="[https://test.com](https://test.com)")
    assert res == "URL is [https://test.com](https://test.com)"


def test_json_validator_valid():
    raw_json = """
    {
      "test_suite": "Unit Test Suite",
      "target_url": "[https://example.com](https://example.com)",
      "steps": [
        {
          "step_number": 1,
          "action": "navigate",
          "selector": "[https://example.com](https://example.com)",
          "value": "",
          "description": "Navigate home"
        }
      ]
    }
    """
    plan = JSONValidator.parse_and_validate(raw_json)
    assert isinstance(plan, TestPlan)
    assert len(plan.steps) == 1


def test_json_validator_invalid():
    raw_json = "{ bad json }"
    with pytest.raises(ValueError):
        JSONValidator.parse_and_validate(raw_json)