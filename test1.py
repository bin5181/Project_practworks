import math
import random
import sys

problem = "A farmer sells his product at a loss of 15\%. If his S.P. was Rs 20000, what was his actual loss? What was his cost price?"

# Calculation for the cost price
selling_price = 20000
loss_percentage = 15
cost_price = selling_price * 100 / (100 - loss_percentage)

# Calculation for the actual loss
actual_loss = cost_price - selling_price

# Formatting the solution in LaTeX
solution = f"\\noindent Given, {problem} \\\\ \n\n"
steps = [
    ["Let the cost price be CP", None, None],
    ["Loss percentage = 15\%", None, None],
    ["Selling price = Rs 20000", None, None],
    [f"Using the formula: Selling Price = Cost Price - Loss, we get", None, None],
    [f"20000 = CP - (15/100)*CP", None, "Substitute the given values"],
    [f"20000 = CP - 0.15CP", None, "Convert the percentage to decimal"],
    [f"20000 = 0.85CP", None, "Simplify the expression"],
    [f"CP = 20000/0.85 = Rs {cost_price:.2f}", None, "Solve for CP"],
    [f"Hence, the cost price is Rs {cost_price:.2f}", None, None],
    [f"Actual loss = CP - Selling price = Rs {actual_loss:.2f}", None, None]
]

for i, (step_txt, verifier, explain) in enumerate(steps, start=1):
    if verifier is not None and verifier() is False:
        break
    solution += f"Step {i}: {step_txt} \\\\ \n"
    if explain is not None:
        solution += f"\\hspace{{1cm}} ({explain}) \\\\ \n\n"

solution += f"\n\\noindent Therefore, the actual loss is Rs {actual_loss:.2f} and the cost price is Rs {cost_price:.2f}."
print(solution)
