#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Vegeta"), BotFeliz("Qiyana"), BotTriste("Teobaldo")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
