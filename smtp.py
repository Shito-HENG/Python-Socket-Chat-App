import smtplib

def info():
    send_email = input("Enter your email: ")
    recieve_email = input("Enter the email you want to send to: ")
    subject = input("Enter the subject: ")
    message = input("Enter the message: ")

    text = f"Subject: {subject}\n\n{message}"
    return send_email, recieve_email, text


def server(send_email, recieve_email, text):
    try:
        # Initialize the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Prompt the user for their app password (use Google App Password)
        password = input("Enter your password: ")

        # Log in to the email account
        server.login(send_email, password)

        # Send the email
        server.sendmail(send_email, recieve_email, text)
        print("Email sent successfully!")

        # Close the connection
        server.quit()
    except Exception as e:
        print(f"An error occurred: {e}")


def verification(send_email, recieve_email, text):
    user_input = input("Are you sure? y/n ").lower()

    if user_input == "y":
        server(send_email, recieve_email, text)
    elif user_input == "n":
        # If the user says no, recollect the email info
        send_email, recieve_email, text = info()
        verification(send_email, recieve_email, text)
    else:
        print("Invalid input")
        verification(send_email, recieve_email, text)


# Collect email info from the user
send_email, recieve_email, text = info()
# Ask the user for confirmation
verification(send_email, recieve_email, text)
