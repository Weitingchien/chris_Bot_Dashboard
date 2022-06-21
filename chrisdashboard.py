from app.main import app
import os

if __name__ == '__main__':
    # This tells our app to use the port assigned by heroku, if not, use 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
