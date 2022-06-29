class webServicesQualitor():
    def __init__(self, object):
        self.qws = object

    def getToken(self):
        return self.qws.token

    #Busca as informações de apenas um chamado. Os campos padrão de retorno do WebService são:
    #No XML de entrada é possível informar os campos que deverão ser retornados.
    def getTicketData(self, cdchamado):
        responseGetTicketData = self.qws.getTicketData(
            cdchamado=cdchamado,
            campos='cdchamado, nmsituacao, nmequipe, dschamado, nmlocalidade, nmresponsavel, nmcontato, dsultimoacompanhamento, dtprevisaoresposta'
        )
        return responseGetTicketData

    def getTicket(self, cdchamado):
        responseGetTicketData = self.qws.getTicketData(
            cdchamado=cdchamado
        )
        return responseGetTicketData

    # Abre um chamado na base do Qualitor. Essa operação irá abrir um chamado no Qualitor, sendo passado por parâmetro todos os valores necessários para abertura de um novo chamado.
    def addTicketByData(self, newTicketData):
        responseAddTicketByData = self.qws.addTicketByData(
            cdperfilchamado='20',
            cdcliente='1',
            cdcontato=newTicketData['cdcontato'],
            idchamado='1',
            cdtipochamado='14',
            cdlocalidade='1',
            cdseveridade='4',
            cdcategoria='17000100',
            cdcategoria1='17000100',
            cdorigem='7',
            nmtitulochamado='INTERNO / ATIVIDADES TECNOLOGIA E SOLUÇÕES',
            dschamado='Descrição: '+newTicketData['dschamado'],
        )
        return responseAddTicketByData

    # Abre Chamado como Incidente
    def addTicketByDataIncident(self, newTicketData):
        responseAddTicketByDataIncident = self.qws.addTicketByData(
            cdperfilchamado='20',
            cdcliente='1',
            cdcontato=newTicketData['cdcontato'],
            idchamado='1',
            cdtipochamado='1',
            cdlocalidade='1',
            cdseveridade='4',
            cdcategoria='26074258',
            cdcategoria1='26074258',
            cdcategoria2='26074278',
            cdorigem='7',
            nmtitulochamado='ERROS / PROBLEMAS TECNOLOGIA E SOLUÇÕES',
            dschamado='Descrição: '+newTicketData['dschamado'],
        )
        return responseAddTicketByDataIncident

    #Inicializa o atendimento de um chamado.
    def startTicket(self, cdchamado):
        responseStartTicket = self.qws.startTicket(
            cdchamado=cdchamado
        )
        return responseStartTicket

    #Adiciona um registro no chamado como solução.
    def addTicketHistory(self, addTicketHistoryData):
        responseAddTicketHistory = self.qws.addTicketHistory(
            cdchamado=addTicketHistoryData['cdchamado'],
            cdtipoacompanhamento='5',
            dsacompanhamento=addTicketHistoryData['dsacompanhamento'],
            dsacaocorretiva=addTicketHistoryData['dsacompanhamento'],
            idsolucao='Y',
            hrduracao=addTicketHistoryData['hrduracao'],
            #dtinicioacompanhamento=addTicketHistoryData['dtinicioacompanhamento'],
            #dtterminoacompanhamento=addTicketHistoryData['dtinicioacompanhamento']
        )
        return responseAddTicketHistory

    #Captura um chamado.
    #Se o cdresponsavel não for informado, o Qualitor irá buscar o código do usuário logado no WS.(hmd.qualitor)
    def CaptureTicket(self, cdchamado, cdresponsavel):
        responseCaptureTicket = self.qws.captureTicket(
            cdchamado=cdchamado,
            cdresponsavel=cdresponsavel,
        )
        return responseCaptureTicket

    #Altera a equipe do chamado.
    def transferTicketTeam(self, cdchamado, cdequipe):
        responseTransferTicketTeam = self.qws.transferTicketTeam(
            cdchamado=cdchamado,
            cdequipe=cdequipe, # FIELD_HMD: 20
            cdmotivorepasse='0'
        )
        return responseTransferTicketTeam

    #Altera o responsável do chamado.
    def transferTicketResponsible(self, cdchamado, cdresponsavel):
        responseTransferTicketResponsible = self.qws.transferTicketResponsible(
            cdchamado=cdchamado,
            cdresponsavel=cdresponsavel,
        )
        return responseTransferTicketResponsible

    #Extende data de atendimento.
    def extendTicket(self, cdchamado, dtlimiteatendimentoprorrogacao, dtprevisaoresposta, dtprorrogacao, hrprevisaoresposta):
        responseExtendTicket = self.qws.extendTicket(
            cdchamado=cdchamado,
            cdmotivoprorrogado='1',
            dtlimiteatendimentoprorrogacao=dtlimiteatendimentoprorrogacao,
            dtprevisaoresposta=dtprevisaoresposta,
            hrprevisaoresposta=hrprevisaoresposta,
            dtprorrogacao=dtprorrogacao,
        )
        return responseExtendTicket

    #Retorna proximas etapas do chamado
    def getTicketNextSteps(self, cdchamado):
        responsegetTicketNextSteps = self.qws.getTicketNextSteps(
            cdchamado=cdchamado
        )
        return responsegetTicketNextSteps

    # Retorna etapa atual do chamado
    def getTicketStep(self, cdchamado):
        responsegetTicketNextSteps = self.qws.getTicketStep(
            cdchamado=cdchamado
        )
        return responsegetTicketNextSteps

    # Retorna etapa atual do chamado
    def setTicketStep(self, cdchamado, cdetapa):
        responsegetTicketNextSteps = self.qws.setTicketStep(
            cdchamado=cdchamado,
            cdetapa=cdetapa,
        )
        return responsegetTicketNextSteps

    # Retorna etapa atual do chamado
    def getServicesByUser(self):
        responsegetServicesByUser = self.qws.getServicesByUser(
            cdcliente='1',
            cdcontato='14997',
        )
        return responsegetServicesByUser

    # Encerra chamado
    def closeTicket(self, cdchamado):
        responsecloseTicket = self.qws.closeTicket(
            cdchamado=cdchamado,
            idfecharrelacionados='Y',
        )
        return responsecloseTicket