class msgs:
    def __init__(self):
        self.menu = """
///////////////////////////////////////////////
//         MENU DE OPÇÕES                    //
// SALVAR E FECHAR PLANILHA ANTES DE INICIAR //
//      *** NÃO HABILITADOS                  //
///////////////////////////////////////////////
// A - Abrir chamados da Planilha            //
// B - Buscar Dados da Planilha              //
// C - Buscar Chamados Abertos da Planilha   //
// E - Planilha utilizada                    //
// F - Se Erro após abertura de chamado      //
// G - Consultar Chamado                     //
// Q - Finalizar Programa                    //
///////////////////////////////////////////////
"""

        self.menu2 = """
///////////////////////////////////////////////
//         MENU DE OPÇÕES 2                  //
// SE OCORRER ERRO APÓS ABERTURA DE CHAMADOS //
//   UTILIZAR AS OPÇÕES ABAIXO, UMA POR VEZ  //  
//  NÃO UTILIZAR SE CONCLUIDO AUTOMATICO - A //
///////////////////////////////////////////////
// F - INICIAR ATENDIMENTO CHAMADOS ABERTOS  //
// G - INICIAR TRANSFERENCIA DE RESPONSAVEL  //
// H - INICIAR DESCRIÇÃO DE ACOMPANHAMENTO   //
// I - CAPTURAR CHAMADO                      //
// Q - RETORNAR MENU ANTERIOR                //
///////////////////////////////////////////////
"""
        self.msg1 = '''
                OPÇÃO INCORRETA!'''

        self.msg2 = '''
                VERIFIQUE OS DADOS DA ABERTURA DE CHAMADO!
                DIGITE "CONFIRMAR" PARA ACEITAR ABERTURA.
                ENTER PARA CANCELAR'''

        self.msg3 = '''
                LISTA DE CHAMADOS!'''

        self.msg4 = '''
                OPERAÇÃO CANCELADA, CONSULTE A PLANILHA.'''

        self.msg5 = '''
                EERO DE DIGITAÇÃO.'''

        self.msg6 = '''
                LISTA DE CHAMADOS ABERTOS!'''

    def getMenu(self):
        return print(self.menu)

    def getMenu2(self):
        return print(self.menu2)

    def getMsg1(self):
        return print(self.msg1)

    def getMsg2(self):
        return print(self.msg2)

    def getMsg3(self):
        return print(self.msg3)

    def getMsg4(self):
        return print(self.msg4)

    def getMsg5(self):
        return print(self.msg5)

    def getMsg6(self):
        return print(self.msg6)