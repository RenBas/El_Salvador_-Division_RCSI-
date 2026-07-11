"""
data.py – Data loading, validation, and processing functions.

This module handles CSV file processing, validation, and data preparation
for the CDR Twin simulation system.
"""

import pandas as pd
import streamlit as st
from typing import Optional, Tuple, List, Dict, Any
from .constants import REQUIRED_SURVEY_COLS, REQUIRED_META_COLS, OPTIONAL_META_COLS, VARIABLES
from .utils import month_str_to_num


@st.cache_data(show_spinner="Processing survey data...")
def process_survey(_survey_df: pd.DataFrame) -> Tuple[Optional[pd.DataFrame], Optional[pd.DataFrame], Optional[str]]:
    """
    Process and validate survey data from uploaded CSV.
    
    Args:
        _survey_df: Raw survey DataFrame
        
    Returns:
        Tuple of (processed_df, school_info_df, error_message)
    """
    if _survey_df is None:
        return None, None, "No survey file uploaded."
    
    try:
        df = _survey_df.copy()
        
        # Validate required columns
        missing = [col for col in REQUIRED_SURVEY_COLS if col not in df.columns]
        if missing:
            return None, None, f"Missing columns: {', '.join(missing)}"
        
        # Extract school ID
        if 'school_id_no' in df.columns:
            df['school_id_no'] = df['school_id_no'].astype(int)
        elif 'school_id' in df.columns:
            df['school_id_no'] = df['school_id'].astype(str).apply(
                lambda x: int(x.split('_')[-1]) if '_' in str(x) else int(x)
            )
        else:
            return None, None, "Need 'school_id_no' or 'school_id' column."
        
        # Generate school names if missing
        if 'school_name' not in df.columns:
            df['school_name'] = df['school_id_no'].apply(lambda x: f"School_{x}")
        else:
            df['school_name'] = df['school_name'].fillna(
                df['school_id_no'].apply(lambda x: f"School_{x}")
            )
        
        # Convert month to numeric
        df['month_num'] = df['month'].apply(month_str_to_num)
        
        # Validate and convert variable columns
        for var in VARIABLES:
            if not pd.api.types.is_numeric_dtype(df[var]):
                df[var] = pd.to_numeric(df[var], errors='coerce')
            if df[var].isna().any() or (df[var] < 0).any() or (df[var] > 1).any():
                return None, None, f"Column '{var}' must be numeric between 0 and 1."
        
        # Extract unique school information
        school_info = df[['school_id_no', 'school_name']].drop_duplicates().sort_values('school_id_no')
        
        return df, school_info, None
    
    except Exception as e:
        return None, None, f"Survey processing error: {str(e)}"


@st.cache_data(show_spinner="Processing metadata...")
def process_metadata(_metadata_df: pd.DataFrame) -> Tuple[Optional[pd.DataFrame], Optional[str]]:
    """
    Process and validate research metadata from uploaded CSV.
    
    Args:
        _metadata_df: Raw metadata DataFrame
        
    Returns:
        Tuple of (processed_df, error_message)
    """
    if _metadata_df is None:
        return None, "No metadata file uploaded."
    
    try:
        df = _metadata_df.copy()
        
        # Validate required columns
        missing = [col for col in REQUIRED_META_COLS if col not in df.columns]
        if missing:
            return None, f"Missing columns: {', '.join(missing)}"
        
        # Extract school ID
        if 'school_id_no' not in df.columns:
            if 'school' in df.columns:
                df['school_id_no'] = df['school'].astype(str).apply(
                    lambda x: int(x.split('_')[-1]) if '_' in str(x) else int(x)
                )
            else:
                return None, "Need 'school_id_no' or 'school' column."
        
        df['school_id_no'] = df['school_id_no'].astype(int)
        
        # Fill optional columns with defaults
        for col, default in OPTIONAL_META_COLS.items():
            if col not in df.columns:
                df[col] = default
            else:
                df[col] = df[col].fillna(default)
        
        # Parse dates
        df['upload_date'] = pd.to_datetime(df['upload_date'], errors='coerce')
        if df['upload_date'].isna().any():
            return None, "Invalid dates in 'upload_date' column."
        
        # Convert boolean field
        if df['utilized_by_school'].dtype != bool:
            df['utilized_by_school'] = df['utilized_by_school'].astype(str).str.lower().map(
                {'true': True, '1': True, 'yes': True, 
                 'false': False, '0': False, 'no': False}
            ).fillna(False)
        
        return df, None
    
    except Exception as e:
        return None, f"Metadata processing error: {str(e)}"


def get_latest_survey(survey_df: pd.DataFrame, school_id: int) -> Optional[pd.Series]:
    """
    Get the most recent survey record for a specific school.
    
    Args:
        survey_df: Processed survey DataFrame
        school_id: School ID number
        
    Returns:
        Latest survey record as a Series, or None if not found.
    """
    sdf = survey_df[survey_df['school_id_no'] == school_id]
    if sdf.empty:
        return None
    return sdf.sort_values('month_num').iloc[-1]
