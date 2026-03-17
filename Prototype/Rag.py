# rag.py

# Lightweight objection retrieval layer for GPS renewal prototype

# This file controls:

# - semantic matching of customer objections

# - retrieval of closest known response pattern

# - local retrieval without external API dependency

# PM note:

# Full production systems may use larger retrieval pipelines.

# Prototype uses lightweight local retrieval so objection behavior remains explainable.
from sentence_transformers import SentenceTransformer
import chromadb

# ---------------- Persistent Chroma Setup ----------------

DB_PATH = "./gps_objection_db"
COLLECTION_NAME = "gps_objections"

client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------- Objection Seed Data ----------------

OBJECTIONS = [
    "Paise nahi hain",
    "Wheelseye GPS dusre company se mehenga hai",
    "Pehle kam price bola tha",
    "Meri gaadi nahi chal rahi",
    "Abhi kaam nahi hai",
    "Tum kyu nahi bhar dete",
    "Gaadi parked hai, renew karne ka fayda nahi",
    "Gaadi Delhi NCR ke bahar hai",
    "Vehicle bech diya, renew nahi karna",
    "Renewal date galat hai",
    "Service se khush nahi hoon",
    "Vehicle sirf local chalti hai",
    "Vehicle scrap ho gaya",
    "Bas renew nahi karna",
    "Dusri company join kar raha hoon",
    "AutoPay use nahi karna",
    "Price kam hone ka wait karunga",
    "Main promise karta hoon paise dunga",
    "Escalation kabhi raise hi nahi hua",
    "Escalation resolve nahi hua",
    "Distributor se karwa lenge",
    "GPS kaam nahi kar raha",
    "SIM inactive hai",
    "Network issue aa raha hai",
    "Refund chahiye",
    "Vehicle nahi dikh raha app mein",
    "Wrong login ho gaya",
    "Plan nahi aa raha"
]

# ---------------- Seed Function ----------------

def seed_data():
    existing = collection.count()

    if existing > 0:
        return

    embeddings = model.encode(OBJECTIONS).tolist()
    ids = [f"obj_{i}" for i in range(len(OBJECTIONS))]

    collection.add(
        ids=ids,
        documents=OBJECTIONS,
        embeddings=embeddings
    )

# ---------------- Retrieval Function ----------------

def retrieve_objection(query):
    query_embedding = model.encode([query]).tolist()

    result = collection.query(
        query_embeddings=query_embedding,
        n_results=1
    )

    if result["documents"] and result["documents"][0]:
        return result["documents"][0][0]

    return "samajh sakta hoon"

# ---------------- Seed at Startup ----------------

seed_data()

# Why local embeddings:
# keeps prototype fully runnable on local machine
# avoids cloud dependency during PM experimentation
