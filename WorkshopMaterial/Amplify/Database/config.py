import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("Database/YOUR-KEY-HERE") # Key should be placed in the same directory
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()
