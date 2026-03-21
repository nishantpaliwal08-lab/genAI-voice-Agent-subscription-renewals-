# Architecture

The GPS renewal prototype uses a deliberately constrained architecture.

This was not because richer orchestration was unavailable, but because early conversational prototyping benefits more from visible control than from technical sophistication.

The objective of this prototype was to answer a narrow PM question:

Can a realistic renewal conversation be made testable quickly using only transcript understanding, lightweight Python logic, and local retrieval?

To answer that, the architecture avoids production dependencies such as telephony APIs, speech systems, external orchestration frameworks, or cloud-hosted retrieval services.

---

## Why the prototype is split into four Python files

The codebase is separated into four files because each file represents a different product decision layer.

### graph.py

This file contains stage progression.

It decides whether the bot is currently:

* opening the conversation
* reminding renewal
* offering plan
* responding to objection
* attempting closure

The decision to isolate stage logic here was intentional.

If stage logic remains visible, PMs can refine conversation behavior without touching retrieval or UI.

---

### prompts.py

This file controls wording variation.

The same business intent can be expressed in multiple ways.

For example:

renewal reminder should not sound identical across turns.

Separating wording from stage logic allows naturalness to improve without changing business control.

---

### rag.py

This file handles objection retrieval.

Rather than hardcoding exact objection-response pairs, objections are semantically matched against known examples.

This keeps the prototype closer to real conversations, where customers rarely repeat the same exact words.

---

### app.py

This file contains the Streamlit interface.

It is intentionally minimal because the objective is rapid conversational testing, not frontend development.

A PM should be able to run the prototype locally and immediately inspect whether stage progression feels believable.

---

## Why this architecture matters

The architecture is simple enough to explain in one sitting, yet modular enough that each refinement remains visible.

That makes it suitable for PM teaching, internal demos, and early conversational experimentation.
