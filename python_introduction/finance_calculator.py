#!/bin/bash
monthly_income = int(input(“Enter your monthly income: ”))
total_monthly_expenses = int(input(“Enter your total monthly expenses: ”))
monthly_savings = monthly_income - total_monthly_expenses
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is:{Projected_Savings}")