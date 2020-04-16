# context.py
"""Provides the context for the test files to import the game of life module.

USAGE: from .context import gameoflife
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import gameoflife
