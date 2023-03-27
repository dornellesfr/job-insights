from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    try:
        with open(path) as file:
            jobs = list(csv.DictReader(file))
        return jobs
    except FileNotFoundError as error:
        return error


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)
    type_jobs = set()
    for job in jobs:
        type_jobs.add(job["job_type"])

    return type_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_jobs = list()
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


if __name__ == "__main__":
    # Testing funct read:
    # print(read('data/jobs.csv'))
    # Testing func get_unique_job_types:
    print(get_unique_job_types('data/jobs.csv'))
    # Testing func filter_by_job_type:
    # print(filter_by_job_type(read('data/jobs.csv'), "OTHER"))
