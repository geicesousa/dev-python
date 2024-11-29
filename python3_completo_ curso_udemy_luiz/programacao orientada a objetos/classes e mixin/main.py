from log import LogPrintMixin, LogFileMixin

log_file = LogFileMixin()
log_file.log_error('na main')
log_file.log_success('sucesso na main')
log_print = LogPrintMixin()
log_print.log_error('na main')
log_print.log_success('sucesso na main')