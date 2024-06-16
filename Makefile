# Define variables
VENV_DIR := venv
BIN_DIR := bin
OS := $(shell uname -s)
DECODE_CONFIG_URL :=
ifeq ($(OS),Linux)
	DECODE_CONFIG_URL := https://github.com/tasmota/decode-config/releases/latest/download/decode-config-ubuntu-22.04.tar.gz
else ifeq ($(OS),Darwin)
	DECODE_CONFIG_URL := https://github.com/tasmota/decode-config/releases/latest/download/decode-config-macos-11.zip
else
	$(error Unsupported OS: $(OS))
endif
DECODE_CONFIG_TAR := $(BIN_DIR)/decode-config.tar.gz
DECODE_CONFIG_ZIP := $(BIN_DIR)/decode-config.zip
DECODE_CONFIG_BIN := $(BIN_DIR)/decode-config

.PHONY: all install_venv install_deps download_decode_config install

# Default target
all: install

# Target to install everything
install: install_venv install_deps download_decode_config
	@echo "Installation complete."

# Target to create virtual environment if it does not exist
install_venv:
	@if [ ! -d $(VENV_DIR) ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV_DIR); \
	fi
	@echo "Virtual environment is ready."

# Target to install Python dependencies
install_deps:
	@echo "Activating virtual environment and installing dependencies..."
	. $(VENV_DIR)/bin/activate && pip install -e .

# Target to download the latest decode-config binary
download_decode_config:
	@mkdir -p $(BIN_DIR)
	@if [ "$(OS)" = "Linux" ]; then \
		echo "Downloading decode-config for Linux..."; \
		curl -L $(DECODE_CONFIG_URL) -o $(DECODE_CONFIG_TAR); \
		tar -xzf $(DECODE_CONFIG_TAR) -C $(BIN_DIR); \
		mv $(BIN_DIR)/decode-config* $(DECODE_CONFIG_BIN); \
		chmod +x $(DECODE_CONFIG_BIN); \
		rm $(DECODE_CONFIG_TAR); \
	elif [ "$(OS)" = "Darwin" ]; then \
		echo "Downloading decode-config for macOS..."; \
		curl -L $(DECODE_CONFIG_URL) -o $(DECODE_CONFIG_ZIP); \
		unzip $(DECODE_CONFIG_ZIP) -d $(BIN_DIR); \
		mv $(BIN_DIR)/decode-config* $(DECODE_CONFIG_BIN); \
		chmod +x $(DECODE_CONFIG_BIN); \
		rm $(DECODE_CONFIG_ZIP); \
	fi
	@echo "decode-config binary is ready."
