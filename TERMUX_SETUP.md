# KVI Guard Termux Setup

## Install packages

```bash
pkg update && pkg upgrade
pkg install python git
```

## Clone repository

```bash
git clone https://github.com/kailpetr/kvi-guard.git
cd kvi-guard
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run verification CLI

```bash
python verify.py
```

## Example Workflow

1. Enter a response to verify
2. KVI analyzes semantic stability
3. Review score, warnings, and telemetry

## Exit

Type:

```text
exit
```
