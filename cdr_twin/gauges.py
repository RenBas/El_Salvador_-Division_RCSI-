"""
gauges.py – Plotly gauge chart builders for CDR Twin visualization.

This module provides functions to create gauge charts for displaying
RCSI scores, utilisation rates, and other metrics.
"""

import plotly.graph_objects as go
import streamlit as st
from typing import List, Optional, Tuple
from .constants import USTP_GOLD, USTP_DARK_BLUE


def create_gauge(
    value: float,
    title: str,
    min_val: float = 0,
    max_val: float = 1.0,
    threshold: Optional[float] = None,
    threshold_color: str = "black",
    steps: Optional[List[Tuple[float, float, str]]] = None,
    dark_mode: bool = False
) -> go.Figure:
    """
    Create a circular gauge chart with customizable appearance.
    
    Args:
        value: The value to display on the gauge
        title: Gauge title
        min_val: Minimum value for the gauge axis
        max_val: Maximum value for the gauge axis
        threshold: Optional threshold value to highlight
        threshold_color: Color for the threshold line
        steps: Custom color steps for the gauge background
        dark_mode: Whether to use dark mode colors
        
    Returns:
        Plotly Figure object containing the gauge chart
    """
    if steps is None:
        steps = [
            (0.0, 0.2, "#D32F2F"),
            (0.2, 0.4, "#F5A623"),
            (0.4, 0.6, "#FFD54F"),
            (0.6, 0.8, "#66BB6A"),
            (0.8, 1.0, "#2E7D32"),
        ]
    
    bar_color = USTP_GOLD if dark_mode else USTP_DARK_BLUE
    
    # Use value as threshold if not specified
    if threshold is None:
        threshold = value
        threshold_color = "black"
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={
            'text': title,
            'font': {'size': 14, 'color': USTP_GOLD if dark_mode else USTP_DARK_BLUE}
        },
        gauge={
            'axis': {
                'range': [min_val, max_val],
                'tickwidth': 1,
                'tickvals': [0, 0.2, 0.4, 0.6, 0.8, 1.0],
                'ticktext': ['0', '', '', '', '', '1'],
                'showticklabels': False
            },
            'bar': {'color': bar_color, 'thickness': 0.6},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 0,
            'steps': [{'range': [s[0], s[1]], 'color': s[2]} for s in steps],
            'threshold': {
                'line': {'color': threshold_color, 'width': 2},
                'thickness': 0.75,
                'value': threshold
            }
        },
        number={
            'font': {'size': 20, 'color': USTP_GOLD if dark_mode else USTP_DARK_BLUE},
            'suffix': '  '
        }
    ))
    
    fig.update_layout(
        height=220,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=USTP_GOLD if dark_mode else USTP_DARK_BLUE)
    )
    
    return fig


def create_utilisation_gauge(value: float, title: str, dark_mode: bool = False) -> go.Figure:
    """
    Create a utilisation gauge chart (0-100 scale).
    
    Args:
        value: Utilisation percentage to display
        title: Gauge title
        dark_mode: Whether to use dark mode colors
        
    Returns:
        Plotly Figure object containing the utilisation gauge
    """
    steps = [
        (0, 20, "#D32F2F"),
        (20, 40, "#F5A623"),
        (40, 60, "#FFD54F"),
        (60, 80, "#66BB6A"),
        (80, 100, "#2E7D32"),
    ]
    
    bar_color = USTP_GOLD if dark_mode else USTP_DARK_BLUE
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={
            'text': title,
            'font': {'size': 14, 'color': USTP_GOLD if dark_mode else USTP_DARK_BLUE}
        },
        gauge={
            'axis': {
                'range': [0, 100],
                'tickwidth': 1,
                'tickvals': [0, 20, 40, 60, 80, 100],
                'ticktext': ['0', '', '', '', '', '100'],
                'showticklabels': False
            },
            'bar': {'color': bar_color, 'thickness': 0.6},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 0,
            'steps': [{'range': [s[0], s[1]], 'color': s[2]} for s in steps],
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': value
            }
        },
        number={
            'font': {'size': 20, 'color': USTP_GOLD if dark_mode else USTP_DARK_BLUE},
            'suffix': '%  '
        }
    ))
    
    fig.update_layout(
        height=200,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=USTP_GOLD if dark_mode else USTP_DARK_BLUE)
    )
    
    return fig


def create_rcsi_gauge(value: float, title: str, dark_mode: bool = False) -> go.Figure:
    """
    Create an RCSI gauge chart (0-1 scale).
    
    Args:
        value: RCSI score to display (0.0 to 1.0)
        title: Gauge title
        dark_mode: Whether to use dark mode colors
        
    Returns:
        Plotly Figure object containing the RCSI gauge
    """
    steps = [
        (0.0, 0.2, "#D32F2F"),
        (0.2, 0.4, "#F5A623"),
        (0.4, 0.6, "#FFD54F"),
        (0.6, 0.8, "#66BB6A"),
        (0.8, 1.0, "#2E7D32"),
    ]
    
    bar_color = USTP_GOLD if dark_mode else USTP_DARK_BLUE
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={
            'text': title,
            'font': {'size': 14, 'color': USTP_GOLD if dark_mode else USTP_DARK_BLUE}
        },
        gauge={
            'axis': {
                'range': [0, 1],
                'tickwidth': 1,
                'tickvals': [0, 0.2, 0.4, 0.6, 0.8, 1.0],
                'ticktext': ['0', '', '', '', '', '1'],
                'showticklabels': False
            },
            'bar': {'color': bar_color, 'thickness': 0.6},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 0,
            'steps': [{'range': [s[0], s[1]], 'color': s[2]} for s in steps],
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': value
            }
        },
        number={
            'font': {'size': 20, 'color': USTP_GOLD if dark_mode else USTP_DARK_BLUE},
            'suffix': '  '
        }
    ))
    
    fig.update_layout(
        height=200,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=USTP_GOLD if dark_mode else USTP_DARK_BLUE)
    )
    
    return fig


def display_gauge_with_interpretation(
    fig: go.Figure,
    value: float,
    interpretation_list: List[str],
    dark_mode: bool
) -> None:
    """
    Display a Plotly gauge chart with an interpretation text below it.
    
    Args:
        fig: Plotly Figure object containing the gauge
        value: Value displayed on the gauge
        interpretation_list: List of interpretation strings for different levels
        dark_mode: Whether dark mode is enabled (unused but kept for API compatibility)
    """
    st.plotly_chart(fig, use_container_width=True)
    
    # Determine the appropriate interpretation level
    if value < 0.2:
        idx = 0
    elif value < 0.4:
        idx = 1
    elif value < 0.6:
        idx = 2
    elif value < 0.8:
        idx = 3
    else:
        idx = 4
    
    level_text = interpretation_list[idx] if interpretation_list else ""
    st.markdown(
        f"<div style='text-align: center;'><b>{level_text}</b></div>",
        unsafe_allow_html=True
    )
