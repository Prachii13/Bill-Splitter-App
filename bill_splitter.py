def calculate_split(total_amount, people, tip_percent):
    total_with_tip = total_amount + (total_amount * tip_percent / 100)
    per_person = total_with_tip / people
    return per_person

def main():
    print("🧾 Bill Splitter App")

    try:
        total = float(input("Enter total bill amount (₹): "))
        people = int(input("Enter number of people: "))
        tip = float(input("Enter tip percentage (e.g., 10 for 10%): "))

        if people <= 0:
            print("❌ Number of people must be greater than zero.")
            return

        share = calculate_split(total, people, tip)
        print(f"\nEach person should pay: ₹{share:.2f}")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
