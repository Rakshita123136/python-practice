from tkinter import *

# Create the main window
root = Tk()
root.title("Product Review Form")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Frame for form
frame = Frame(root, bg="#ffffff", padx=10, pady=10)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Canvas for decoration
canvas = Canvas(frame, width=200, height=100, bg="#add8e6")
canvas.grid(row=0, column=0, columnspan=2, pady=10)
canvas.create_text(100, 50, text="Review Form", font=("Helvetica", 16, "bold"), fill="black")

# Labels and Entries
Label(frame, text="Full Name:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
name_entry = Entry(frame, width=40, font=("Arial", 12))
name_entry.grid(row=1, column=1, pady=5)

Label(frame, text="Email:", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
email_entry = Entry(frame, width=40, font=("Arial", 12))
email_entry.grid(row=2, column=1, pady=5)

# Radiobuttons for Gender
Label(frame, text="Gender:", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)

gender_var = StringVar(value="None")
Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=1, sticky="w")
Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=1, padx=80, sticky="w")

# Checkbuttons for Interests
Label(frame, text="Interests:", bg="#ffffff", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=5)

interest1 = IntVar()
interest2 = IntVar()
interest3 = IntVar()

Checkbutton(frame, text="Product Quality", variable=interest1, bg="#ffffff", font=("Arial", 12)).grid(row=4, column=1, sticky="w")
Checkbutton(frame, text="Customer Service", variable=interest2, bg="#ffffff", font=("Arial", 12)).grid(row=5, column=1, sticky="w")
Checkbutton(frame, text="Price", variable=interest3, bg="#ffffff", font=("Arial", 12)).grid(row=6, column=1, sticky="w")

# Listbox for Ratings
Label(frame, text="Rate Us:", bg="#ffffff", font=("Arial", 12)).grid(row=7, column=0, sticky="w", pady=5)

rating_listbox = Listbox(frame, height=4, selectmode=SINGLE, font=("Arial", 12))
rating_listbox.grid(row=7, column=1, sticky="w")
ratings = ["Excellent", "Good", "Average", "Poor"]
for item in ratings:
    rating_listbox.insert(END, item)

# Spinbox for Age
Label(frame, text="Age:", bg="#ffffff", font=("Arial", 12)).grid(row=8, column=0, sticky="w", pady=5)
age_spinbox = Spinbox(frame, from_=18, to=100, width=10, font=("Arial", 12))
age_spinbox.grid(row=8, column=1, sticky="w")

# Menubutton for Country Selection
Label(frame, text="Country:", bg="#ffffff", font=("Arial", 12)).grid(row=9, column=0, sticky="w", pady=5)

menu_btn = Menubutton(frame, text="Select Country", bg="#ffffff", font=("Arial", 12), relief=RAISED)
menu_btn.grid(row=9, column=1, sticky="w")

country_menu = Menu(menu_btn, tearoff=0)
menu_btn.configure(menu=country_menu)

countries = ["India", "USA", "UK", "Australia", "Canada"]
for country in countries:
    country_menu.add_command(label=country)

# Scrollbar for comments
Label(frame, text="Comments:", bg="#ffffff", font=("Arial", 12)).grid(row=10, column=0, sticky="w", pady=5)

scrollbar = Scrollbar(frame)
scrollbar.grid(row=10, column=2, sticky="ns")

comments = Text(frame, width=40, height=4, font=("Arial", 12), yscrollcommand=scrollbar.set)
comments.grid(row=10, column=1, pady=5)

scrollbar.config(command=comments.yview)

# Submit Button
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    age = age_spinbox.get()
    country = menu_btn.cget("text")
    
    interests = []
    if interest1.get():
        interests.append("Product Quality")
    if interest2.get():
        interests.append("Customer Service")
    if interest3.get():
        interests.append("Price")

    rating = rating_listbox.get(ACTIVE)
    comments_text = comments.get("1.0", END).strip()

    # Display results in console
    print("\n--- Form Submission ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Gender: {gender}")
    print(f"Age: {age}")
    print(f"Country: {country}")
    print(f"Interests: {', '.join(interests)}")
    print(f"Rating: {rating}")
    print(f"Comments: {comments_text}")

    # Confirmation message
    confirmation = f"Thank you, {name}!\n\nYour review has been submitted."
    Label(frame, text=confirmation, bg="#ffffff", font=("Arial", 12, "italic"), fg="green").grid(row=12, column=0, columnspan=2, pady=10)

# Submit button
submit_btn = Button(frame, text="Submit", command=submit_form, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))
submit_btn.grid(row=11, column=0, columnspan=2, pady=10)

# Start the GUI loop
root.mainloop()
