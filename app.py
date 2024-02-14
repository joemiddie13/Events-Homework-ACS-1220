import sys
print(sys.path)
from events_app import app

if __name__ == "__main__":
		app.run(debug=True)
