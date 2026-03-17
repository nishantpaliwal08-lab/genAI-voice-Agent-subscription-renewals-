
# Prototype

This repository includes a lightweight chat-based prototype of a GPS subscription renewal conversational agent.

The prototype is intentionally limited.

It is not a telephony system.

It does not include:

* speech-to-text
* text-to-speech
* live calling APIs
* payment workflows

---

## What the prototype demonstrates

The prototype shows how a PM can move from:

call recordings → conversational stages → state logic → objection handling → runnable interface

within a few hours.

---

## Current prototype scope

* one customer at a time
* one-year plan as default
* 3-month fallback only when customer asks cheaper option
* objection interruption allowed at any stage
* simple Streamlit chat interface

---

## Why prototype is useful

A production voice agent requires vendor infra.

But PM learning happens earlier:

by making conversation logic visible and testable before vendor dependency begins.
