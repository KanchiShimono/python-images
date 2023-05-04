import json
from argparse import ArgumentParser, Namespace
from typing import Any, TypedDict


class Job(TypedDict):
    name: str
    version: str
    short_version: str
    variant: str


class Matrix(TypedDict):
    include: list[Job]


def build_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('--versions-json', type=str, default='versions.json')
    args = parser.parse_args()
    return args


def generate_jobs(versions: dict[str, Any]) -> list[Job]:
    jobs: list[Job] = []
    for short_version, v in versions.items():
        version = v['version']
        for variant in v['variants']:
            name = f'{version}-{variant}'
            job: Job = {
                'name': name,
                'version': version,
                'short_version': short_version,
                'variant': variant,
            }
            jobs.append(job)
    return jobs


def main() -> None:
    args = build_args()
    with open(args.versions_json, 'r') as f:
        versions = json.load(f)
    jobs = generate_jobs(versions)
    matrix: Matrix = {'include': jobs}
    print(json.dumps(matrix))


if __name__ == '__main__':
    main()
