from app import create_app
from app.db import check_mongo_connection

app = create_app()

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=80,debug=True)