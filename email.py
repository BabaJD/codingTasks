### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():

        # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        # Declare the class variable, with default value, for emails. 
        self.has_been_read = False

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox(inbox,email_address, subject_line, email_content):
    recieved_email = Email(email_address, subject_line, email_content)
    inbox.append(recieved_email)

# Create 3 sample emails and add it to the Inbox list. 
populate_inbox(inbox,"ronniedums@gmail.com","Project Date Enquiry","Hello, When is the start date of the next project? Kind Regards")

populate_inbox(inbox, "smithlee@yahoo.com","Soccer Practice Dates","Hello Parents, This is a reminder for this session's soccer practice for pupils in years one to four. Please find attached the dates in the document. Thank you, Kind regards")

populate_inbox(inbox, "dogtrainers@gmail.com", "Doggy Class Promo","Hello, Pet lover, we have a 65 percent discount on all our offers, here's a link for more information")
    
    
# Create a function which prints the email’s subject_line, along with a corresponding number.

def list_emails(inbox):
    for i, recieved_email in enumerate(inbox, start = 0):
        print(f"{i} {recieved_email.subject_line}")


def read_email(inbox, index):

    # Check if the index is within the range of the inbox
    if 0 <= index < len(inbox):
        # Get the email at the given index
        recieved_email = inbox[index]
        print(f"\nEmail Address: \n{recieved_email.email_address}")
        print(f"\nSubject Line: \n{recieved_email.subject_line}")
        print(f"\nEmail content: \n{recieved_email.email_content}")
        # Mark the email as read
     # Once displayed, call the class method to set its 'has_been_read' variable to True.
        recieved_email.mark_as_read()
        print(f"\nThe email from {recieved_email.email_address} has been marked as read.")
    else:  
        print("\nInvalid Index. Please provide a valid index within range")

def display_email(inbox, index):

    # Check if the index is within the range of the inbox
    if 0 <= index < len(inbox):
        # Get the email at the given index
        recieved_email = inbox[index]
        print("\nSubject Line: " + recieved_email.subject_line)
    else:  
        print("\nInvalid Index. Please provide a valid index within range")
    




# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
         # Display the subject lines of all emails
        print("\nInbox: \n")
        list_emails(inbox)

        # Ask the user which email they want to read
        index = int(input("\nEnter the index of the email you want to read: "))

        # Display the selected email and mark it as read
        read_email(inbox, index)
        
    elif user_choice == 2:
        # add logic here to view unread emails
        print("\nUnread emails: ")
        for i, email in enumerate(inbox):
            if not email.has_been_read:
                print(f"{i}: {email.subject_line}")
            
    elif user_choice == 3:
        # add logic here to quit appplication
        print("\nQuitting application . . .")
        menu = False

    else:
        print("Oops - incorrect input.")

