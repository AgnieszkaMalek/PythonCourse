import  exchange_rates


def convert_gbp_to_bgn(amount):
    return amount * exchange_rates.GBP_TO_BGN


def convert_gbp_to_pln(amount):
    return amount * exchange_rates.GBP_TO_PLN


def convert_gbp_to_czk(amount):
    return amount * exchange_rates.GBP_TO_CZK


def convert_gbp_to_huf(amount):
    return amount * exchange_rates.GBP_TO_HUF


def main():
    user_input = input("Enter amount to convert:")
    gbp_amount = float(user_input)
    bgn_amount = convert_gbp_to_bgn(gbp_amount)
    pln_amount = convert_gbp_to_pln(gbp_amount)
    czk_amount = convert_gbp_to_czk(gbp_amount)
    huf_amount = convert_gbp_to_huf(gbp_amount)

    print(f"£{gbp_amount} British pounds is equal to:")
    print("%.2f" % round(bgn_amount, 2), "Bulgarian lev \"BGN\"")
    print("%.2f" % round(pln_amount, 2), "Polish Zloty \"PLN\"")
    print("%.2f" % round(czk_amount, 2), "Czech Koruna \"CZK\"")
    print("%.2f" % round(huf_amount, 2), " Hungarian Forint \"HUF\"")


if __name__ == "__main__":
    main()