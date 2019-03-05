fib ?= 1

ifeq ($(origin _A), undefined)
  _A = 0
  _B = 1
  _C = 1
else
  private _C := $(shell echo $(_A) + $(_B) | bc)
  _A := $(_B)
  _B := $(_C)
endif
export _A  _B fib

_fib:
ifeq ($(fib), $(MAKELEVEL))
	@$(MAKE) -C . _done --no-print-directory
else
	@echo lv=$(MAKELEVEL), A=$(_A) B=$(_B)
	@$(MAKE) -C . _fib --no-print-directory
endif

_done:
	@echo result=$(_A)
