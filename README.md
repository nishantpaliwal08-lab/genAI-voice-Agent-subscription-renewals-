# Call Recordings to AI Agent in 4 Hours

A product-first guide to building a conversational AI prototype from real call recordings.

---

## Why this repository exists

Most conversational AI discussions start with models, tools, or infrastructure.

In practice, the harder problem is earlier:

understanding how real human conversations are structured.

This repository demonstrates how a PM can move from:

call recordings → conversation design → runnable prototype

within a few hours.

---

## Working use case

The repository uses GPS subscription renewals as a reference scenario.

A customer with an expiring GPS plan is contacted for renewal.

The conversational goal is simple:

* remind renewal
* offer plan
* handle objection
* attempt closure

This narrow scope makes it ideal for early-stage AI prototyping.

---

## What makes this repository different

Most AI repos show code.

This repository shows **decision-making**:

* how transcripts become stages
* how flow is simplified
* how PM refinement improves behavior
* why certain architectures were chosen

---

## Repository structure

* **Problem Statement & Business Context** → why this problem matters
* **Conversational Design** → how conversations are structured
* **Prototype** → runnable Python implementation
* **PM Refinement** → how behavior improved after first draft
* **Architecture** → design decisions and tradeoffs
* **Appendix** → alternative approaches (e.g., full LLM control)

---

## What is intentionally excluded

This repository does not cover:

* telephony systems
* speech-to-text / text-to-speech
* production deployment

These are handled by vendor systems in real implementations.

The focus here is:

**early-stage conversational intelligence design**

---

## How to use this repository

1. Start with Problem Statement
2. Move to Conversational Design
3. Understand Prototype structure
4. Review PM Refinement
5. Explore Architecture decisions

---

## Key takeaway

A conversational AI system is not built by prompts alone.

It is built by:

understanding human behavior → structuring it → refining it → then automating it
