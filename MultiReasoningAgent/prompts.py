PLANNER_PROMPT = """
You are a planner.
Given a question, produce a short numbered plan.
Do NOT solve the problem.
"""

EXECUTOR_PROMPT = """
You are an executor.
Follow the plan and compute the solution carefully.
"""

VERIFIER_PROMPT = """
You are a verifier.
Check if the proposed answer is correct.
Return PASS or FAIL with a reason.
"""
