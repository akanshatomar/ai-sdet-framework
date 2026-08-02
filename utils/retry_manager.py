from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from utils.logger import logger


def create_retry_decorator(max_attempts: int = 3, delay_seconds: int = 2):
    """Returns a tenacity retry decorator configured for LLM call failures."""
    
    def log_retry_attempt(retry_state):
        logger.warning(
            f"Attempt {retry_state.attempt_number} failed. Retrying in {delay_seconds}s... "
            f"Error: {retry_state.outcome.exception()}"
        )

    return retry(
        stop=stop_after_attempt(max_attempts),
        wait=wait_fixed(delay_seconds),
        retry=retry_if_exception_type((ValueError, Exception)),
        after=log_retry_attempt,
        reraise=True
    )