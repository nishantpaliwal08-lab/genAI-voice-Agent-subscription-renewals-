# From Transcript to Structured Flow

Raw transcripts are noisy.

They contain filler words, interruptions, repeated phrases, and incomplete thoughts.

A conversational AI system cannot directly operate on raw transcripts.

The first step is abstraction.

---

## Example raw interaction

Agent: Namaste sir, Wheelseye se baat kar raha hoon
Customer: Haan bolo

Agent: Sir aapki gaadi ka GPS renewal pending hai
Customer: Achha

Agent: Same one-year plan available hai
Customer: Renew nahi karna

---

## What is actually happening

Although the words vary, the interaction contains clear conversational moves:

* introduction
* renewal reminder
* plan pitch
* rejection

These are not sentences.

These are **stages**.

---

## Stage mapping

| Raw utterance    | Interpreted stage |
| ---------------- | ----------------- |
| greeting         | Opening           |
| renewal mention  | Renewal Reminder  |
| plan explanation | Plan Offer        |
| refusal          | Objection         |

---

## Why this transformation is necessary

If we directly use raw sentences:

* system becomes brittle
* variation breaks logic
* scaling becomes difficult

By converting to stages:

* variation is absorbed
* logic becomes stable
* behavior becomes testable

---

## PM decision layer

This mapping is not automatic.

A model may extract many micro-intents.

A PM simplifies them.

For example:

AI might separate:

* greeting
* identity
* context

PM combines them into:

Opening

---

## Key takeaway

Do not design conversations at sentence level.

Design them at **stage level**.

Sentences are surface.

Stages are structure.

