from ...model import Trait

def populateTrait(daily):
    trait = Trait()
    trait.date = daily.date
    trait.last_close=float(daily.last_close)
    trait.open = float(daily.open)
    trait.high = float(daily.high)
    trait.low = float(daily.low)
    trait.close = float(daily.current)
    return trait
