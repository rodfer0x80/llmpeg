SCRIPTS_DIR := ./scripts
SCRIPTS := $(wildcard $(SCRIPTS_DIR)/*.sh)
SCRIPT_NAMES := $(notdir $(basename $(SCRIPTS)))

.PHONY: default
default:
	@echo "[make] $(SCRIPT_NAMES)"

.PHONY: $(SCRIPT_NAMES)
$(SCRIPT_NAMES): %: $(SCRIPTS_DIR)/%.sh
	@echo "[make] $@"
	@bash $<

.PHONY: all
all: $(SCRIPT_NAMES)

