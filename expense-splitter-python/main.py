def calculate_split(total_amount , number_of_people , currency) -> None:
    if number_of_people < 1:
        raise ValueError("Number of people must be greater than 1")
    
    share_per_person = total_amount / number_of_people

    print(f"Total Expense: {currency} {total_amount:,.2f}")
    print(f"Number of people: {number_of_people}")
    print(f"Per person payment: {currency} {share_per_person:,.2f}")

def main() -> None:
    try:
        total = float(input("Enter total amount: "))
        number_of_people = int(input("Enter total no. of people: "))

        calculate_split(total, number_of_people, "INR")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()