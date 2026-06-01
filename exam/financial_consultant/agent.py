from google.adk.agents.llm_agent import Agent
from OOP import CurrencyAsset, CryptoAsset, Portfolio

def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    rates_to_uah = {
        'USD': 41.5,
        'EUR': 45.0,
        'GBP': 52.0,
        'BTC': 3_800_000,
        'UAH': 1.0,
    }

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    rate_from = rates_to_uah.get(from_currency)
    rate_to = rates_to_uah.get(to_currency)

    if rate_from is None or rate_to is None:
        raise ValueError(f'Unsupported currency: {from_currency} or {to_currency}')

    asset = CurrencyAsset(from_currency, amount, rate_from)
    amount_uah = asset.get_value_uah()
    result = amount_uah / rate_to

    return {
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
        'result': result,
        'rate': {
            'from_to_uah': rate_from,
            'to_to_uah': rate_to,
        },
    }

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Фінансовий консультант з обміну валют.',
    instruction='Агент є фінансовим консультантом з обміну валют. Він конвертує суми між валютами та пояснює поточний курс. Відповідає українською мовою.',
)
