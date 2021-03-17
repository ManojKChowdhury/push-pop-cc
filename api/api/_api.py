"""Module to setup fastapi API to expose API to the outside world."""
import logging
import random
from typing import Any, Dict

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

INTERSECTION_LISTS = [['resolved', 'unresolved'], ['resolved', 'backlog'], ['unresolved', 'backlog']]
ERROR_CODES = [error_code for error_code in range(50)]
LOGGER = logging.getLogger("API")
app = FastAPI()
generated_errors = {}
last_error_updated = {}


class AppError(BaseModel):
    index: int
    code: int
    text: str


def _generate_lists() -> Dict[str, Any]:
    """Generate resolved, unresolved and backlog lists."""
    return {
        'resolved': [{
            'index': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error ABC occured, that is `resolved`'
        } for error_idx in range(50)],
        'unresolved': [{
            'index': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error DEF occured, that is `unresolved`'
        } for error_idx in range(50, 100)],
        'backlog': [{
            'index': error_idx,
            'code': random.choice(ERROR_CODES),
            'text': 'Error XYZ occured, that is in the `backlog`'
        } for error_idx in range(100, 150)]
    }


@app.get("/get_lists")
def get_lists() -> Dict[str, Any]:
    """Return resolved, unresolved and backlog lists."""
    LOGGER.info('Generating resolved, unresolved and backlog lists.')

    global generated_errors
    generated_errors = _generate_lists()
    return generated_errors


@app.get("/get_list_intersection_counts")
def get_list_intersection_counts() -> Dict[str, int]:
    LOGGER.info('Generating the intersection counts between a set of resolved, unresolved and backlog lists.')

    # Get error lists
    error_lists = _generate_lists()

    # Get and store the intersection counts in the intersection_counts variable
    intersection_counts = {}
    for combinations in INTERSECTION_LISTS:
        intersection_counts[combinations[0] + "_" + combinations[1]] = get_intersection_count(
            error_lists[combinations[0]], error_lists[combinations[1]]
        )

    return intersection_counts


def get_intersection_count(list1, list2) -> int:
    # Convert lists to set of error codes to avoid duplicates and perform intersection
    set1_error_codes = set(error["code"] for error in list1)
    set2_error_codes = set(error["code"] for error in list2)

    return len(set1_error_codes.intersection(set2_error_codes))


@app.put("/update_error")
def update_error(error_details: AppError, current_list_name: str):
    results = {'error_details': error_details, 'list_name': current_list_name}

    LOGGER.info("Updating error status.")
    # TODO: API to resolve/un-resolve errors. Also move errors to backlog


def run(host: str, port: int) -> None:
    """Run the code challenge API."""
    uvicorn.run(app, host=host, port=port)
