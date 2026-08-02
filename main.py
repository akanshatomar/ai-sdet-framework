import sys
from dotenv import load_dotenv
from agents.login_agent import LoginAgent
from executor.runner import PlaywrightExecutor
from utils.logger import logger

# Load environment variables (.env)
load_dotenv()


def run_pipeline():
    logger.info("Initializing AI-SDET Automation Framework...")

    # Configuration
    target_login_url = "[https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)"

    try:
        # 1. Initialize Agent
        agent = LoginAgent()

        # 2. Generate AI Test Plan
        plan = agent.generate_test_plan(
            target_url=target_login_url,
            username="tomsmith",
            password="SuperSecretPassword!"
        )

        logger.info(f"Generated {len(plan.steps)} test steps.")

        # 3. Execute with Playwright
        executor = PlaywrightExecutor(headless=True)
        success = executor.execute_plan(plan)

        if success:
            logger.info("Execution Pipeline Completed: SUCCESS")

    except Exception as e:
        logger.critical(f"Execution Pipeline Failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    run_pipeline()