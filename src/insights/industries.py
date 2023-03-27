from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    file = read(path)
    all_industries = set()
    for job in file:
        if job["industry"] != '':
            all_industries.add(job["industry"])

    return all_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_jobs = list()
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)

    return filtered_jobs


if __name__ == "__main__":
    # Testing function get_unique_industries:
    print(get_unique_industries("data/jobs.csv"))
