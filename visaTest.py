import re
def findCreditCard(raw):
    visaRE = re.findall("4[46][0-9]{13}", raw)
    if visaRE:
        print "[+] found one Card: " + visaRE[0]
def main():
    tests = []
    tests.append('I would like to buy 1337 copies of that dvd')
    tests.append('Bill my card: 461234567891234 for \$2600')
    for test in tests:
        findCreditCard(test)
if __name__ == "__main__":
    main()