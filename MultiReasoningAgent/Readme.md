# Multi-Step Reasoning Agent

## Architecture
- Planner: creates a plan
- Executor: computes answer
- Verifier: validates correctness

## Why no chain-of-thought?
To follow LLM safety best practices and avoid leaking internal reasoning.

## How to Run
python agent.py

## Retry Logic
Agent retries up to 2 times if verification fails.

## Improvements
- Plug real LLM APIs
- Add symbolic math solver
- Improve verifier robustness
