from openpyxl import load_workbook, Workbook
from openpyxl.styles import Color, Font, PatternFill
import os

def getLogin():
    login = 'login'
    return login

def getPassword():
    password = 'senha'
    return password

def getWsdl():
    wsdl = 'https://qualitor.com.br/ws/services/service.php?wsdl=WSTicket'
    return wsdl