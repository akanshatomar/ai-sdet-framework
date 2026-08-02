from playwright.sync_api import sync_playwright
from utils.json_validator import TestPlan, TestStep
from utils.logger import logger


class PlaywrightExecutor:
    """Executes structured AI test plans using Playwright Browser Automation."""

    def __init__(self, headless: bool = True):
        self.headless = headless

    def execute_plan(self, plan: TestPlan) -> bool:
        logger.info(f"--- Starting Execution: {plan.test_suite} ---")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()

            try:
                for step in plan.steps:
                    self._execute_step(page, step)

                logger.info("--- Test Suite Execution Passed Successfully ---")
                return True

            except Exception as e:
                logger.error(f"Execution failed on step {step.step_number}: {str(e)}")
                # Capture screenshot on failure
                page.screenshot(path="logs/failure_screenshot.png")
                logger.info("Saved failure screenshot to logs/failure_screenshot.png")
                raise e

            finally:
                browser.close()

    def _execute_step(self, page, step: TestStep):
        logger.info(f"Step {step.step_number} [{step.action.upper()}]: {step.description}")

        action = step.action.lower()

        if action == "navigate":
            page.goto(step.selector)
        elif action == "fill":
            page.fill(step.selector, step.value)
        elif action == "click":
            page.click(step.selector)
        elif action in ["assert_visible", "assert"]:
            page.wait_for_selector(step.selector, state="visible", timeout=5000)
        else:
            raise ValueError(f"Unsupported action step: '{action}'")