# Infra Automation (mock)

Current Versioning 1.0.0.3
(mock, no major changes, no minor version, 3 git pushes so far)

## Overview

This repo contains a minimal Python-based skeleton to simulate infrastructure provisioning and service configuration. It supports:

- interactive creation of VM definitions
- validation via pydantic
- saving configs to `configs/instances.json`
- running a bash installer to configure a service (nginx)
- logging to `logs/provisioning.log`

## Setup

1. Create a virtualenv and install deps:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Make installer executable:


```bash
chmod +x scripts/install_service.sh
```

3. Run the simulator:

```bash
python infra_simulator.py
```

4. Run main:

```bash
python main.py
```


## Expected behaviour

The script will prompt you to add machines. Leave name blank to finish.

Machines are validated and appended to configs/instances.json.

For each machine the script calls scripts/install_service.sh. The outcome is in the console and in logs/provisioning.log.