from typing import override
from bot.game_model.game_intel import GameIntel
from bot.game_model.card_to_play import CardToPlay
from bot.game_model.interfaces import BotServiceProvider

class DjangoRemoteBot(BotServiceProvider):
  def __init__(self):
    pass
  
  @override
  def getMaoDeOnzeResponse(intel: GameIntel) -> bool:
    return False
  
  @override
  def decideIfRaises(intel: GameIntel) -> bool:
    return False
  
  @override
  def chooseCard(intel: GameIntel) -> CardToPlay:
    intel.cards
    return 
  
  @override
  def getRaiseResponse(intel: GameIntel) -> int:
    return 0