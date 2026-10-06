# Question 2: Borrower Tuple Details

# Create an immutable tuple for borrower details
borrower_data = ("John Doe", "B1023", "2025-10-15",)

# Access elements using positive and negative indexing
borrower_name = borrower_data[0]
library_id = borrower_data[1]
membership_date = borrower_data[-1]

print("Borrower Information:")
print("Name:", borrower_name)
print("Library ID:", library_id)
print("Membership Date:", membership_date)

# Prove that immutability
try:
    borrower_data[2] = "Regular"  # Attempting to change membership
except TypeError as error:
    print("\nImmutability Error:", error)


    #Print length and iterate using a loop
    print("tuple length:", len(borrower_data))
