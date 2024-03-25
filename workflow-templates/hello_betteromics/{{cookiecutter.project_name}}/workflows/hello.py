"""
This module defines a simple Flyte workflow that can run on Betteromics
"""
from typing import NamedTuple

from flytekit import task, workflow

# See https://docs.flyte.org/en/latest/flyte_fundamentals/tasks_workflows_and_launch_plans.html
# for explanations of the @task and @workflow decorators


@task
def say_hello(name: str) -> str:
    return f"Hello {name}! Welcome to Betteromics"


@task
def compute_greeting_length(greeting: str) -> int:
    return len(greeting)


# To return multiple outputs from a workflow we define a NamedTuple
HelloOutput = NamedTuple(
    "HelloOutput",
    greeting=str,
    greeting_len=int,
)


@workflow
def wf(name: str) -> HelloOutput:
    greeting = say_hello(name=name)
    greeting_len = compute_greeting_length(greeting=greeting)

    return HelloOutput(greeting=greeting, greeting_len=greeting_len)
