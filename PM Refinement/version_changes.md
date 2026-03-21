# Version Changes

This section captures how the prototype evolved after initial implementation.

The goal is not to show code differences.

The goal is to show **behavioral improvement**.

---

## Version 1 — Linear Flow

### Behavior

* Conversation followed fixed stage order
* Bot continued plan pitch even when customer objected
* No differentiation between types of objections

### Result

* conversation felt scripted
* customer interruptions were ignored
* interaction broke under realistic input

---

## Version 2 — Interruptible Flow

### Change introduced

Objections can interrupt any stage.

Instead of forcing stage completion, the system:

* detects objection
* responds immediately
* resumes original stage

---

### Behavior after change

* conversation adapts to user input
* objections feel acknowledged
* flow remains consistent

---

## Version 3 — Conditional Plan Offer

### Change introduced

Fallback (3-month plan) is shown only when customer signals price sensitivity.

---

### Behavior after change

* avoids premature discounting
* maintains business intent
* feels closer to human agent behavior

---

## Version 4 — Reduced Repetition

### Change introduced

Prompt and response logic updated to avoid repeating identical phrasing.

---

### Behavior after change

* interaction feels less robotic
* improves perceived intelligence
* reduces drop-off in multi-turn conversation

---

## Key insight

Most improvements did not require new models.

They required:

* better control over flow
* better understanding of user intent
* tighter alignment with real-world behavior
