class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin, balance, age = map(int, input().split(", "))

while True:
    command = input().split("#")
    if command[0] == "End":
        break

    if command[0] == "Send Money":
        money_to_send = int(command[1])
        pin_code = int(command[2])
        if money_to_send > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        print(f"Successfully sent {money_to_send:.2f} money to a friend")
        print(f"There is {(balance - money_to_send):.2f} money left in the bank account")

    if command[0] == "Receive Money":
        money_to_receive = int(command[1])
        if money_to_receive < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        print(f"{(money_to_receive / 2):.2f} money went straight into the bank account")
