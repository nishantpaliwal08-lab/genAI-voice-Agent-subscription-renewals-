# prompts.py

# Language variation layer for GPS renewal prototype

# This file controls:

# - how same business intent is expressed differently

# - how bot avoids sounding repetitive

# - how simple variation is introduced without full LLM dependency

# PM note:

# Stage logic should remain stable even if wording changes.

# This separation helps test conversation design independently from language style.
import random

# ---------------- Opening ----------------
OPENING_LINES = [
    "Namaste sir, Wheelseye se baat kar raha hoon.",
    "Namaste sir, Wheelseye GPS team se baat kar raha hoon.",
    "Namaste sir, Wheelseye company se baat kar raha hoon."
]

# ---------------- Intent ----------------
INTENT_LINES = [
    "Sir aapki gaadi ka GPS renewal pending hai.",
    "Sir GPS renewal ke regarding call kiya tha.",
    "Sir aapki GPS validity renew karni thi."
]

# ---------------- Plan pitch ----------------
PLAN_LINES = [
    "Sir aapne last time one-year plan liya tha, same yearly renewal available hai.",
    "Sir same one-year GPS plan renew ho sakta hai.",
    "Sir yearly plan continue kar sakte hain."
]

# ---------------- Cheaper plan ----------------
CHEAPER_PLAN_LINES = [
    "Agar cheaper option chahiye toh 3 month plan bhi available hai.",
    "Sir short validity ke liye 3 month plan dekh sakte hain.",
    "Agar kam amount chahiye toh short plan available hai."
]

# ---------------- Confirmation ----------------
CONFIRMATION_LINES = [
    "Sir agar theek lage toh same yearly plan renew kar dete hain.",
    "Sir same plan continue kar dein?",
    "Sir yearly renewal proceed kar dein?"
]

# ---------------- Closure ----------------
CLOSURE_LINES = [
    "Theek hai sir, payment ke liye callback arrange kar deta hoon.",
    "Dhanyawaad sir, shortly callback aa jayega.",
    "Theek hai sir, aage payment team connect karegi."
]

# ---------------- Helper ----------------
def get_prompt(options):
    return random.choice(options)
