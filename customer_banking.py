# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    #item = input("What is the item that you want to purchase? ")
    savings_balance = input("Please enter the savings balance for the savings account ")
    savings_balance = int(savings_balance)
    savings_interest = input("Please enter the interest rate for the savings account ")
    savings_interest = int(savings_interest)
    savings_maturity = input("Please enter the months for the savings account ")
    savings_maturity = int (savings_maturity)


    # Call the create_savings_account function and pass the variables from the user.
    #MWJ
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE!!!!!!!!!!!!
    print ("Interest earned = ", "%.3f" % interest_earned)
    print ("Updated savings balance = ", "%.2f" % updated_savings_balance)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input("Please enter the savings balance for the CD account ")
    cd_balance = int(cd_balance)
    cd_interest = input("Please enter the interest rate for the CD account ")
    cd_interest = int(cd_interest)
    cd_maturity = input("Please enter the months for the CD account ")
    cd_maturity = int (cd_maturity)

    # Call the create_cd_account function and pass the variables from the user.
    #MWJ
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE!!!!!!!!!!!!!!!!
    print ("CD interest earned = ", "%.3f" % cd_interest_earned)
    print ("Updated CD balance = ", "%.2f" % updated_cd_balance)

if __name__ == "__main__":
    # Call the main function.
    main()
