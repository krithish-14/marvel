import sys
import os

# Make the project root importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the WSGI app - Vercel looks for 'app' at module level
from marvel_site.wsgi import app
