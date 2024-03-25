# hello_betteromics

hello_betteromics is a simple Flyte workflow that you can register and run on Betteromics

## Prerequisites

> **Note:**
> You must have access to a Betteromics environment, other than https://public-demo.betteromics.com/, in order to run CLI commands. If you need help accessing your Betteromics environment, contact your customer success engineer or reach out to us on our [website](https://betteromics.com/) (click "Try it" and "Request a Tour").

### 1. Install and configure the Betteromics CLI

Follow the instructions on your environment support page (ex: https://your_environment.betteromics.com/support) under <i>"Local Development"</i>. You can check your configuration by running `betteromics info`.

### 2. Install dependencies

You may also need to set up the required software and tools:

- [Python](https://www.python.org/downloads/)
- Docker (you can either use [Docker Desktop](https://www.docker.com/) or type `brew install docker` in your terminal to install docker)
- [Virtualenv](https://pypi.org/project/virtualenv/) or [pyenv](https://github.com/pyenv/pyenv-virtualenv)
- IDE of your choice (e.g. [Visual Studio](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/))

### 3. Log in and authenticate

Use your **terminal prompt** to run the command below, using your team's environment name for the `--context` value. Your environment name is the first part of the URL before ".betteromics.com". For example, on public-demo.betteromics.com, the environment name is `public_demo`. Follow the instructions on your terminal to authenticate.

```bash
# On your terminal, make sure to replace {your_environment} with the name of your environment
$ betteromics --context {your_environment} authenticate
```

## Usage

Then to obtain this workflow code on your machine, run

```
betteromics init hello_betteromics --template hello_betteromics
```

This creates a `hello_betteromics` folder on your machine with Dockerfile

```
$ cd hello_betteromics
$ tree
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
└── workflows
    ├── __init__.py
    └── hello.py
```

Register the workflow by running:

```
betteromics --context {your_environment} register . "Hello Betteromics" workflows.hello.wf
```

This command will build a Docker image, push it to Betteromics, and print out a URL to run the workflow.

Visit this URL to run the workflow.
