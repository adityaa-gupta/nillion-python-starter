from nada_dsl import *

def getInt(name, party):
  return SecretInteger(Input(name=name, party=party))

def nada_main():
    creditor = Party(name="creditor")
    debtor = Party(name="debtor")

    payment_history = getInt("payment_history", debtor)
    credit_utilization = getInt("credit_utilization", debtor)
    debt_to_income = getInt("debt_to_income", debtor)
    credit_history_length = getInt("credit_history_length", debtor)
    inquiries = getInt("inquiries", debtor)

    payment_history_weight = getInt("payment_history_weight", creditor)
    credit_utilization_weight = getInt("credit_utilization_weight", creditor)
    debt_to_income_weight = getInt("debt_to_income_weight", creditor)
    credit_history_length_weight = getInt("credit_history_length_weight", creditor)
    inquiries_weight = getInt("inquiries_weight", creditor)

    normalized_credit_utilization = Integer(10000) - credit_utilization

    condition = credit_history_length < Integer(2000)
    capped_credit_history_length = condition.if_else(credit_history_length, Integer(2000))
    eight_fifty = Integer(85000)

    payment_history_score = (payment_history / Integer(10000)) * eight_fifty
    credit_utilization_score = (normalized_credit_utilization / Integer(10000)) * eight_fifty
    debt_to_income_score = (Integer(100) - debt_to_income) * eight_fifty
    credit_history_length_score = (capped_credit_history_length / Integer(2000)) * eight_fifty
    inquiries_score = (eight_fifty - (inquiries * Integer(5000)))

    weighted_score = (
        payment_history_weight * payment_history_score
        + credit_utilization_weight * credit_utilization_score
        + debt_to_income_weight * debt_to_income_score
        + credit_history_length_weight * credit_history_length_score
        + inquiries_weight * inquiries_score
    )

    return [Output(weighted_score, "weighted_score", debtor)]