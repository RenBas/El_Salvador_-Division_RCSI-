# ============================================================
# app.py – entry point for Streamlit application
# ============================================================
# 
# IMPORTANT: This file must be run using the command:
#   streamlit run app.py
# 
# Do NOT run with: python app.py
# Running with 'python app.py' will cause errors because
# Streamlit requires its own runtime context.
# ============================================================

import sys

# Verify Python version
print("Python version:", sys.version)

# Import the main Streamlit app function
from cdr_twin.ui import app

# The app() function is called automatically by Streamlit
# when running with 'streamlit run app.py'
if __name__ == "__main__":
    # This block only executes if someone incorrectly runs 'python app.py'
    # Streamlit will handle calling app() when run properly
    print("\n" + "="*70)
    print("WARNING: This script should be run with 'streamlit run app.py'")
    print("         not with 'python app.py'")
    print("="*70)
    print("\nTo start the application, please run:")
    print("  streamlit run app.py\n")
    app()
