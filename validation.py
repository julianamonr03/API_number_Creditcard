def checkLuhn(cardNumber):

    # Remove empty spaces for correct validation
    cardNumber = cardNumber.replace(" ", "")
    nDigits = len(cardNumber)
    digit_sum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNumber[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        # Add two digits to handle
        # cases that make two digits after
        # doubling
        digit_sum += d // 10
        digit_sum += d % 10

        isSecond = not isSecond

    if (digit_sum % 10 == 0):
        return True

    else:
        return False
