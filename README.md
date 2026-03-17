# Call Recordings to AI Agent in 4 Hours

A PM-first guide to building a conversational AI prototype from real call recordings.

---

## Why this repository exists

Most conversational AI discussions begin with models, orchestration frameworks, or voice infrastructure.

In practice, the first hard problem is simpler:

understanding how real human calls are structured.

This repository demonstrates how a product manager can move from:

call recordings → transcript patterns → conversation flow → runnable AI prototype

within a few hours.

---

## Current business use case

This repository uses GPS subscription renewals as the working example.

A customer whose GPS plan is near expiry receives an outbound renewal conversation.

The conversational goal is simple:

* remind renewal status
* explain available plan
* handle objection
* attempt closure

Because the objective is narrow and objections repeat frequently, this use case is ideal for lightweight conversational AI prototyping.

---

## What is included

* business context behind GPS renewals
* transcript-to-conversation flow thinking
* lightweight state-machine design
* Python prototype (chat interface only)
* PM refinement examples after first AI draft

---

## What is intentionally excluded

This repository does not cover:

* telephony integration
* speech-to-text
* text-to-speech
* production deployment

The actual production voice layer may be built separately by vendor systems.

The focus here is:

first working conversational intelligence prototype.

---

## Repository philosophy

The goal is not to write perfect production code.

The goal is to make visible where PM intelligence changes the quality of an AI agent after the first AI-generated draft.

---

## Repository structure

Start with:

* Problem Statement & Business Context
* Conversation Design
* Prototype

Additional folders are added only when the prototype itself becomes stable.
