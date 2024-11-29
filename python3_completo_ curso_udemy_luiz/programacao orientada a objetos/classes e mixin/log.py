from pathlib import Path

LOG_FILE =  Path(__file__).parent / 'log.txt'
print(LOG_FILE)

class Log: # classe abstrata
    # parece não ter utilidade, mas é uma forma de padrão de projeto: template method - método não implementado;
    def _log(self, msg): # metodo abstrato, toda classe que for herdar de log obrigatoriamente tem que usar esse metodo
        raise NotImplementedError('Implemente o método log') # NotImplementedError, esse erro é para quando a classe não deve ser usada diretamente; nesse caso, devemos usar o método em subclasses e não na própria classe (mãe)

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    

class LogFileMixin(Log): # mixin indica que devemos adc funcionalidades na herança múltipla, que não são necessariamente da mesma família
    def _log(self,msg): # há um pricipio de poo (liskov subtitution) onde não podemos mudar a assinatura do método, ou seja, manter os parâmetros, tipos e retorno; se estamos sobrepondo um método a assinatura deve ser igual
        print(f'Salvando no log... {msg}, class: {self.__class__.__name__}')
        with open(LOG_FILE,'a') as arquivo: # a - adiciona
            arquivo.write(msg)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)

   
if __name__ == '__main__': # garante que o teste só seja executado no módulo corrente
    log_file = LogFileMixin()
    log_file.log_error('log erro')
    log_file.log_success('log sucesso')
    log_print = LogPrintMixin()
    log_print.log_error('log erro')
    log_print.log_success('log sucesso')