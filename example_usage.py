from client import DelegatedAgenticCheckoutGuardrailClient

def main():
    client = DelegatedAgenticCheckoutGuardrailClient()
    res = client.evaluate_checkout_guardrail('api.anthropic.com', 42.50, 100.00)
    print('Agentic Checkout Guardrail: ' + res['guardrail_id'] + ' (' + res['guardrail_verdict'] + ')')
    print('Amount: $' + str(res['purchase_amount_usd']) + ' | Remaining: $' + str(res['remaining_velocity_budget_usd']))
    print('Audit Receipt: ' + res['audit_receipt_url'])

if __name__ == '__main__':
    main()
