class TasmotaConfigToolError(Exception):
    """Base class for exceptions in this module."""
    pass

class ConfigurationError(TasmotaConfigToolError):
    """Exception raised for errors in the configuration."""
    pass

class DeviceCommunicationError(TasmotaConfigToolError):
    """Exception raised for errors in device communication."""
    pass
