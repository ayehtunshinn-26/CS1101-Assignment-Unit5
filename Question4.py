# Question 4: Weekly Statistics Slicing and Processing

# Borrowed list in each week

borrowed_books = [23, 19, 31, 27, 22, 30, 25]

# Extract records from week 2 to week 5 using slicing

sliced_record = borrowed_books[1:5]

#Replace the number of books borrowed in week 1

borrowed_books[0]=20

# Display the sliced portion and the updated list

print("Sliced Records(Week 2 to Week 5):", sliced_record)
print("Updated Borrowed Book List:", borrowed_books)


