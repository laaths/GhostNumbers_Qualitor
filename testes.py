import datetime

from openpyxl import load_workbook, Workbook
from openpyxl.styles import Color, Font, PatternFill
import os
from datetime import timedelta, date, time, datetime
from openPyxl import listCalledExcel


def getFileCalled():
    fileCalled = 'PlanilhaAberturaDeChamados.xlsx'
    return fileCalled

def mainOpen():
    getListHistory = listCalledExcel(getFileCalled()).getListHistory()
    for list in range(len(getListHistory)):
        if getListHistory[list]['cdcategoria'].upper() != 'INCIDENTE':
            getListHistory[list]['cdcategoria'] = 'INTERNO'
        else:
            pass
        print(getListHistory[list]['cdcategoria'], getListHistory[list]['dschamado'])


mainOpen()