from django.http import JsonResponse
from django.shortcuts import render
from bot.game_model.interfaces import BotServiceProvider
from bot.game_model.game_intel import GameIntel
from bot.django_remote_bot import DjangoRemoteBot;

bot_instance = DjangoRemoteBot();
# Create your views here.
def getMaoDeOnzeResponse(self,intel: GameIntel):
  return bot_instance.get_mao_de_onze_response(intel)
   
def decideIfRaises(self,intel: GameIntel):
  return bot_instance.decide_if_raises(intel)
   
def chooseCard(self,intel: GameIntel):
  return bot_instance.choose_card(intel)
   
def getRaiseResponse(self,intel: GameIntel):
  return bot_instance.get_raise_response(intel)

def getName(self):
  return bot_instance.getName()
