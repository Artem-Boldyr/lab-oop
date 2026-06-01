from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
from typing import List


class Asset(ABC):
    def __init__(self, name: str, amount: float) -> None:
        self.name = name
        self.amount = amount

    @abstractmethod
    def get_value_uah(self) -> float:
        raise NotImplementedError


class CurrencyAsset(Asset):
    def __init__(self, name: str, amount: float, rate_to_uah: float) -> None:
        super().__init__(name, amount)
        self.__rate_to_uah = rate_to_uah

    @property
    def rate(self) -> float:
        return self.__rate_to_uah

    def get_value_uah(self) -> float:
        return self.amount * self.__rate_to_uah


class CryptoAsset(Asset):
    def __init__(self, name: str, amount: float, base_rate_to_uah: float) -> None:
        super().__init__(name, amount)
        self.base_rate_to_uah = base_rate_to_uah

    def get_value_uah(self) -> float:
        volatility = randint(-500, 500)
        current_rate = self.base_rate_to_uah + volatility
        return self.amount * current_rate


class Portfolio:
    def __init__(self) -> None:
        self.__assets: List[Asset] = []

    def add(self, asset: Asset) -> None:
        self.__assets.append(asset)

    def total_value_uah(self) -> float:
        return sum(asset.get_value_uah() for asset in self.__assets)
