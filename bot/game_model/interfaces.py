from abc import ABC, abstractmethod
from bot.game_model.card_to_play import CardToPlay
from bot.game_model.game_intel import GameIntel

class BotServiceProvider(ABC):
  @abstractmethod
  def getMaoDeOnzeResponse(intel: GameIntel) -> bool:
    raise NotImplementedError
  
  @abstractmethod
  def decideIfRaises(intel: GameIntel) -> bool:
    raise NotImplementedError
  
  @abstractmethod
  def chooseCard(intel: GameIntel) -> CardToPlay:
    raise NotImplementedError
  
  @abstractmethod
  def getRaiseResponse(intel: GameIntel) -> int:
    raise NotImplementedError
  
  def getName(self) -> str:
    return self.__class__.__name__