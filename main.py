import datetime
from datetime import timedelta, date
from pyqualitor import QualitorWS
from WSQualitor import webServicesQualitor
import login
from openPyxl import listCalledExcel
from xmlElement import xmlRefactor
import time
from msgs import msgs

# CARREGA METODO DO WEBSERVICE JÁ COM TOKEN DE LOGIN
def getTokenWS():
    qualitorws = QualitorWS(login.getWsdl())
    qualitorws.login(login=login.getLogin(), password=login.getPassword())
    time.sleep(1)
    return qualitorws

# BUSCA CAMINHO E NOME DO ARQUIVO XLSX
def getFileCalled():
    fileCalled = 'PlanilhaAberturaDeChamados.xlsx'
    return fileCalled

# CHAMA METODO DE ABERTURA DE CHAMADO
# ABRE LISTA DE CHAMADOS
def initOpenTickets(planList):
    webService = webServicesQualitor(getTokenWS())
    numCalledList = []
    for list in range(len(planList)):
        time.sleep(1)
        if planList[list]['cdcategoria'].upper() == 'INCIDENTE':
            openTick = webService.addTicketByDataIncident(planList[list])
        else:
            openTick = webService.addTicketByData(planList[list])
        print("\nCHAMADO", list + 1, xmlRefactor(openTick).getNumChamado(), "ABERTO!")
        xmlRefactor(openTick).printFullItens()
        numCalledList.append(xmlRefactor(openTick).getNumChamado())
    return numCalledList

def initStartTicket(planList):
    webService = webServicesQualitor(getTokenWS())
    for list in range(len(planList)):
        time.sleep(2)
        start = webService.startTicket(planList[list]['cdchamado'])
        try:
            print("\nCHAMADO",list+1, xmlRefactor(start).getNumChamado(), "EM ATENDIMENTO!")
        except IndexError:
            pass
        xmlRefactor(start).printFullItens()

def initHistoryTiket(planList):
    webService = webServicesQualitor(getTokenWS())
    for list in range(len(planList)):
        time.sleep(1)
        history = webService.addTicketHistory(planList[list])
        print("\nCHAMADO", list+1, xmlRefactor(history).getNumChamado(), "REGISTRO DE ACOMPANHAMENTO!")
        xmlRefactor(history).printFullItens()

def initCaptureCalled(planList):
    webService = webServicesQualitor(getTokenWS())
    for list in range(len(planList)):
        time.sleep(1)
        team = webService.transferTicketTeam(planList[list]['cdchamado'], str(listCalledExcel(getFileCalled()).ws.cell(row=1, column=4).value))
        time.sleep(1)
        respons = webService.transferTicketResponsible(planList[list]['cdchamado'], str(listCalledExcel(getFileCalled()).ws.cell(row=1, column=2).value))
        print("\nCHAMADO", list+1, xmlRefactor(respons).getNumChamado(), "EM ATENDIMENTO POR:", xmlRefactor(webService.getTicket(planList[list]['cdchamado'])).getresponseChamado())
        xmlRefactor(respons).printFullItens()

def initExtendTicket(cdchamado, daySum):
    date_required = date.today() + timedelta(days=daySum)
    webService = webServicesQualitor(getTokenWS())
    response = webService.extendTicket(
        cdchamado,
        str(datetime.datetime.strftime(date_required, '%Y-%m-%d')),
        str(datetime.datetime.strftime(date_required, '%Y-%m-%d')),
        str(datetime.datetime.strftime(date_required, '%Y-%m-%d %H:%M')),
        str(datetime.datetime.strftime(date_required, '%H:%M'))
    )
    return response

def initCloseTiket(planList):
    webService = webServicesQualitor(getTokenWS())
    for list in range(len(planList)):
        time.sleep(1)
        try:
            history = webService.closeTicket(planList[list]['cdchamado'],)
            print("\nCHAMADO", list+1, xmlRefactor(history).getNumChamado(), "ENCERRADO!")
            xmlRefactor(history).printFullItens()
        except IndexError:
            history2 = webService.setTicketStep(planList[list]['cdchamado'], str(1068))
            history = webService.setTicketStep(planList[list]['cdchamado'], str(1362))
            print("\nCHAMADO", list+1, xmlRefactor(history).getNumChamado(), "ENCERRADO!")
            xmlRefactor(history).printFullItens()

def getCalledOpened():
        calledList = listCalledExcel(getFileCalled()).getListHistory()
        for x in range(len(calledList)):
            print("\nChamado", x + 1)
            xmlRefactor(webServicesQualitor(getTokenWS()).getTicketData(calledList[x]['cdchamado'])).printFullItens()

def mainOpen():
        numCalledList = initOpenTickets(listCalledExcel(getFileCalled()).getListCalled())
        listCalledExcel(getFileCalled()).sendNumCalled(numCalledList)
        getListHistory = listCalledExcel(getFileCalled()).getListHistory()
        for list in range(len(getListHistory)):
            if getListHistory[list]['cdcategoria'].upper() != 'INCIDENTE':
                getListHistory[list]['cdcategoria'] = 'INTERNO'
            else:
                pass
        initStartTicket(getListHistory)
        initCaptureCalled(getListHistory)
        initHistoryTiket(getListHistory)
        initCloseTiket(getListHistory)

# Menu de opções
def main():
    while True:
        msgs().getMenu()
        opt = input("OPÇÃO DESEJADA: ").upper()
        if opt == 'Q':
            break
        elif opt == 'A':
            listCalledExcel(getFileCalled()).getFormatedDataPlan()
            msgs().getMsg2()
            resp = input("RESPOSTA: ").upper()
            if resp != 'CONFIRMAR':
                msgs().getMsg4()
            else:
                mainOpen()
                pass
        elif opt == 'B':
            msgs().getMsg3()
            listCalledExcel(getFileCalled()).getFormatedDataPlan()
        elif opt == 'C':
            msgs().getMsg6()
            getCalledOpened()
        elif opt == 'D':
            try:
                cdchamado = str(input("Digite o numero do chamado: "))
                daySum = int(input("Aprazar quantos dias?: "))
                xmlRefactor(initExtendTicket(cdchamado, daySum)).printFullItens()
                #xmlRefactor(webServicesQualitor(getTokenWS()).extendTicket(cdchamado, daySum, daySum)).printFullItens()
            except ValueError:
                msgs().getMsg5()
        elif opt == 'E':
            print(getFileCalled())
        elif opt == 'F':
            while True:
                msgs().getMenu2()
                opt2 = input("OPÇÃO DESEJADA: ").upper()
                if opt2 == 'Q':
                    break
                elif opt2 == 'F':
                    initStartTicket(listCalledExcel(getFileCalled()).getListHistory())
                    break
                elif opt2 == 'G':
                    initCaptureCalled(listCalledExcel(getFileCalled()).getListHistory())
                    break
                elif opt2 == 'H':
                    initHistoryTiket(listCalledExcel(getFileCalled()).getListHistory())
                    break
                elif opt2 == 'I':
                    initCloseTiket(listCalledExcel(getFileCalled()).getListHistory())
                elif opt2 == 'J':
                    xmlRefactor(webServicesQualitor(getTokenWS()).CaptureTicket((str(input("Numero do Chamado: "))), (str(input("Codigo do Atendente: "))))).printFullItens()
                elif opt == 'J':
                    xmlRefactor(webServicesQualitor(getTokenWS()).getTicketNextSteps((str(input("Numero do Chamado: "))))).printFullItens()
                elif opt == 'K':
                    xmlRefactor(webServicesQualitor(getTokenWS()).setTicketStep((str(input("Numero do Chamado: "))),(input("N STEP: ")))).printFullItens()
                elif opt == 'L':
                    xmlRefactor(webServicesQualitor(getTokenWS()).getTicketStep((str(input("Numero do Chamado: "))))).printFullItens()
                else:
                    msgs().getMsg1()
                    break
        elif opt == 'G':
            xmlRefactor(
                webServicesQualitor(getTokenWS()).getTicketData((str(input("Numero do Chamado: "))))).printFullItens()
        else:
            msgs().getMsg1()

if __name__ == '__main__':
    main()