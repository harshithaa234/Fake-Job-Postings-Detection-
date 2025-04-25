import os
from app import app

if __name__ == '__main__':
    # Set working directory to backend/
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app.run(debug=True, host='0.0.0.0', port=5000)