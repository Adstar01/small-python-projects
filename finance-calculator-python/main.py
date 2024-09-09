def calculate_finances(monthly_income, tax_rate, rent, food, gym, currency) -> None:
    monthly_tax = monthly_income * (tax_rate / 100)
    monthly_expense = rent + food + gym
    monthly_net_income = monthly_income - (monthly_tax + monthly_expense)
    yearly_salary = monthly_income * 12
    yearly_tax = monthly_tax * 12
    yearly_expense = monthly_expense * 12
    yearly_net_income = yearly_salary - (yearly_tax + yearly_expense)

    print("-------------------------------------------")
    print(f"Monthly Income: {currency} {monthly_income:,.2f}")
    print(f"Tax Rate: {tax_rate:,.0f}%")
    print(f"Monthly Tax: {currency} {monthly_tax:,.2f}")
    print(f"Monthly Expenses: {currency}{monthly_expense:,.2f}")
    print(f"Monthly Net Income: {currency} {monthly_net_income:,.2f}")
    print(f"Yearly Salary: {currency} {yearly_salary:,.2f}")
    print(f"Yearly Tax Paid: {currency} {yearly_tax:,.2f}")
    print(f"Yearly Expenses: {currency}{yearly_expense:,.2f}")
    print(f"Yearly Net Income: {currency} {yearly_net_income:,.2f}")
    print("-------------------------------------------")

def main() -> None:
    monthly_income = float(input("Enter your monthly salary: "))
    tax_rate = float(input("Enter tax rate(%): "))

    monthly_rent = float(input("Enter your monthly rent: "))
    monthly_food = float(input("Enter your monthly food expense: "))
    monthly_gym = float(input("Enter your monthly gym membership fee: "))

    calculate_finances(monthly_income, tax_rate, monthly_rent , monthly_food, monthly_gym,currency="INR",)


if __name__ == "__main__":
    main()
