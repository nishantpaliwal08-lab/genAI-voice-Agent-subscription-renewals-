# graph.py

# Core stage controller for GPS renewal prototype

# This file decides:

# - which conversational stage customer is currently in

# - when objection handling interrupts normal flow

# - when fallback plan should appear

# PM note:

# Prototype deliberately uses explicit stage control instead of free LLM reasoning.

# This keeps behavior stable during early experimentation.


from rag import retrieve_objection
from prompts import (
    OPENING_LINES,
    INTENT_LINES,
    PLAN_LINES,
    CHEAPER_PLAN_LINES,
    CONFIRMATION_LINES,
    CLOSURE_LINES,
    get_prompt
)

def bot_reply(user_input, stage):
    user = user_input.lower()

    # ---------------- Version 1 (AI-generated first draft) ----------------
    # Initial objection detection handled only obvious commercial signals.
    # Limitation observed:
    # customer saying "renew nahi karna" was not treated as objection.

    # objection_words = [
    #     "mehenga", "price", "service", "gps", "network", "baad", "later", "sasta"
    # ]

    # ---------------- Version 2 (PM refinement) ----------------
    # Added refusal signals because refusal is operationally different from
    # neutral customer continuation.

    objection_words = [
        "mehenga",
        "price",
        "service",
        "gps",
        "network",
        "baad",
        "later",
        "sasta",
        "nahi",
        "renew nahi",
        "nahi karna",
        "mat karo"
    ]

    # objection interrupt at any stage
    if any(word in user for word in objection_words):
        objection = retrieve_objection(user_input)

        if "sasta" in user or "cheap" in user:
            return (
                get_prompt(CHEAPER_PLAN_LINES),
                stage
            )

        # ---------------- Version 1 ----------------
        # Earlier every objection pushed yearly plan again.

        # return (
        #     f"Samajh sakta hoon sir, {objection}. Same yearly renewal best rahega.",
        #     stage
        # )

        # ---------------- Version 2 ----------------
        # Softer response added:
        # refusal should not sound repetitive or aggressive.

        return (
            f"Samajh sakta hoon sir, {objection}. Agar abhi yearly nahi toh short validity bhi dekh sakte hain.",
            stage
        )

    # opening
    if stage == "opening":
        return (
            get_prompt(OPENING_LINES),
            "intent"
        )

    # intent
    if stage == "intent":
        return (
            get_prompt(INTENT_LINES),
            "plan_pitch"
        )

    # plan pitch
    if stage == "plan_pitch":
        return (
            get_prompt(PLAN_LINES),
            "confirmation"
        )

    # confirmation
    if stage == "confirmation":

        if any(word in user for word in ["haan", "yes", "kar do", "theek hai"]):
            return (
                get_prompt(CLOSURE_LINES),
                "closure"
            )

        return (
            get_prompt(CONFIRMATION_LINES),
            "confirmation"
        )

    # closure
    if stage == "closure":
        return (
            "Dhanyawaad sir.",
            "done"
        )

    return ("Dobara batayiye sir.", stage)
