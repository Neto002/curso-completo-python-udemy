from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error("a")
lp.log_success("b")

lf = LogFileMixin()
lf.log_error("a")
lf.log_success("b")
