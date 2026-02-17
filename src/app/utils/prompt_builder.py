def build_prompt(notes: str) -> str:
    return f"""
You are an insurance claims assistant.

Given the claim notes below, generate:
1. overallSummary
2. customerSummary
3. adjusterSummary
4. recommendedNextStep

Return strictly in JSON format.

<NOTES>
{notes}
</NOTES>
"""
