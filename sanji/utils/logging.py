"""Logging utilities for SANJI."""

import logging

class SANJILogger:
    """Custom logger for SANJI framework."""
    
    _instances = {}
    
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        
        # FIXME: Logger handler leak
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)
    
    def info(self, msg):
        self.logger.info(msg)
    
    def error(self, msg):
        self.logger.error(msg)
