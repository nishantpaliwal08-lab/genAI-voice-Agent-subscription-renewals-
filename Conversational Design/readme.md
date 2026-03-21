# Conversational Design

Most conversational AI failures do not come from model limitations.

They come from weak understanding of how real human conversations are structured.

Before writing any prompts or code, a product manager must first answer:

What is the repeatable structure behind these conversations?

---

## Why conversational design matters

In the GPS renewal use case, conversations appear flexible on the surface.

Different customers use different words.
Agents use slightly different phrasing.

However, underneath that variation, the structure is highly repetitive.

Almost every call follows a narrow pattern:

* greeting
* renewal reminder
* plan explanation
* objection
* closure attempt

If this structure is not made explicit, the system either:

* becomes too rigid (scripted bot)
* or too unpredictable (free LLM)

---

## What this prototype does differently

Instead of starting with prompts or models, this prototype starts with:

**stage abstraction**

The goal is not to capture every sentence.

The goal is to capture:

what type of conversational move is happening

---

## Core design decision

We reduce conversation into a small number of stages:

* Opening
* Renewal Reminder
* Plan Offer
* Objection Handling
* Closure

This is a simplification.

Real conversations are messier.

But early prototypes benefit from **controlled simplification**.

---

## Where PM judgement enters

AI can help extract patterns from transcripts.

But it cannot decide:

* which stages are operationally meaningful
* which variations can be ignored
* how much complexity should be removed

These decisions directly affect:

* stability of prototype
* realism of interaction
* ease of iteration

---

## Key takeaway

Conversational AI should not begin with models.

It should begin with:

**understanding how humans already solve the problem repeatedly**
