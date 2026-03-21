# Prototype Design Choices

Several architectural choices were deliberately constrained even though more advanced alternatives were possible.

The goal was not to maximize technical sophistication.

The goal was to preserve explainability.

---

## Why full LLM control was avoided

A fully free LLM can generate fluent conversations quickly.

However, in early testing it usually introduces instability:

* stage skipping
* repeated offers
* inconsistent objection handling
* weak closure discipline

For a renewal use case, this becomes risky because business flow is narrow and interruptions are frequent.

A bounded stage controller therefore gives better early results.

---

## Why local retrieval was preferred over external API retrieval

Objection handling needed semantic flexibility, but the prototype still had to run locally.

Using local embeddings allows:

* no cloud dependency
* fast experimentation
* transparent objection dataset updates

This also helps PMs inspect why certain objections trigger certain responses.

---

## Why Streamlit was chosen

A prototype should run without frontend dependency.

Streamlit reduces setup friction.

A PM can edit one Python file and immediately observe conversational change.

This dramatically shortens refinement cycles.

---

## Why telephony was excluded

Voice introduces multiple simultaneous variables:

* speech recognition errors
* latency
* voice naturalness
* interruption timing

For first-stage PM learning, these variables hide the real conversational question.

The prototype therefore isolates conversation logic before voice complexity is introduced.

---

## PM takeaway

A prototype becomes useful when business decisions remain inspectable.

This architecture was chosen to keep every meaningful decision visible.
