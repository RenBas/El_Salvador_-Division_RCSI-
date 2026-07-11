# ============================================================
# __init__.py – cdr_twin package initialization
# ============================================================
"""
CDR Twin Package - Research Culture Sustainability Index Simulation

This package provides tools for simulating and analyzing research culture
sustainability in educational institutions.

Quick Start:
    To run the Streamlit application:
    
    $ streamlit run app.py
    
    IMPORTANT: Do NOT run with 'python app.py' as Streamlit requires
    its own runtime context.
"""

__version__ = "1.0.0"

from .constants import (
    VARIABLES,
    VAR_FULL_NAMES,
    VAR_INTERPRETATION,
    MILESTONE_NAMES,
    RCSI_LEVELS,
    USTP_DARK_BLUE,
    USTP_GOLD,
)

__all__ = [
    "VARIABLES",
    "VAR_FULL_NAMES",
    "VAR_INTERPRETATION",
    "MILESTONE_NAMES",
    "RCSI_LEVELS",
    "USTP_DARK_BLUE",
    "USTP_GOLD",
]
