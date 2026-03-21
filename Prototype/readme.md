# Prototype

This repository includes a lightweight, runnable prototype of a GPS subscription renewal conversational agent.

The goal of this prototype is not to simulate a production voice system.

The goal is to make conversational behavior **visible, testable, and improvable** using simple tools.

---

## What this prototype demonstrates

This prototype shows how a PM can move from:

call recordings → stage abstraction → controlled logic → objection handling → runnable interaction

within a few hours.

It is intentionally constrained so that each design decision remains inspectable.

---

## Scope of the prototype

The prototype supports a narrow but realistic renewal flow:

* customer is informed about pending GPS renewal
* yearly plan is offered as default
* objections can occur at any stage
* 3-month plan is offered only after price resistance
* conversation continues across multiple turns

---

## What is intentionally not included

The prototype excludes:

* telephony integration
* speech-to-text and text-to-speech
* payment workflows
* CRM integrations

These systems introduce additional complexity that can hide core conversational issues.

---

## Architectural philosophy

The prototype separates conversation into four layers:

* **graph.py** → stage control
* **prompts.py** → language variation
* **rag.py** → objection retrieval
* **app.py** → interface

This separation ensures that:

* business flow remains controllable
* language can evolve independently
* objection handling can be improved without rewriting logic

---

## Why this approach was chosen

A fully generative system can produce fluent conversations quickly.

However, early prototypes built this way often suffer from:

* inconsistent flow
* repeated offers
* weak objection handling
* unpredictable closure

This prototype instead uses a **deterministic backbone with limited semantic flexibility**.

This makes behavior easier to debug and refine.

---

## What to observe when running the prototype

When interacting with the system, focus on:

* how the bot maintains stage despite interruptions
* how objections are handled before returning to flow
* when fallback plan is introduced
* whether responses feel repetitive or natural

The goal is not perfection.

The goal is to identify where behavior deviates from real human calls.

---

## PM takeaway

A prototype becomes valuable when it exposes its own weaknesses.

This system is designed to make those weaknesses visible, so they can be refined iteratively.
