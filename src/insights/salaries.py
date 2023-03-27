from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    file = read(path)
    salaries = list()
    for salary in file:
        if salary["max_salary"].isdigit():
            salaries.append(int(salary["max_salary"]))

    return max(salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    file = read(path)
    salaries = list()
    for salary in file:
        if salary["min_salary"].isdigit():
            salaries.append(int(salary["min_salary"]))

    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        max = int(job["max_salary"])
        min = int(job["min_salary"])
        salary = int(salary)
    except Exception:
        raise ValueError('Err')

    if max < min:
        raise ValueError('Err')
    return min <= salary <= max


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    all_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                all_jobs.append(job)
        except ValueError:
            ...
    return all_jobs


if __name__ == "__main__":
    # Testing function get_max_salary:
    print(get_max_salary("data/jobs.csv"))
    # Testing function get_min_salary:
    print(get_min_salary("data/jobs.csv"))
