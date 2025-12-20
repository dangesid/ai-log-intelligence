def build_prompt(query, logs):
    logs_text = "\n".join(logs)
    
    prompt = f"""
You are a senior Site Reliability Engineer (SRE).

You are analyzing a production incident.

USER QUESTION:
{query}

OBSERVED LOGS (ONLY SOURCE OF TRUTH):
{logs_text}

TASK:
1. Identify the PRIMARY root cause
2. Identify any SECONDARY contributing factors
3. Explain how they are related
4. Suggest next debugging steps

RULES:
- Base conclusions strictly on the logs
- If cache misses are present, explain whether they are a cause or a symptom

ANSWER FORMAT:
Primary Cause:
Secondary Factors:
Explanation:
Next Steps:
"""

    return prompt