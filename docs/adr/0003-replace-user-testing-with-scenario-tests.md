# 3. Replace user testing with scenario tests

- **Status:** Accepted
- **Date:** 2026-11-05

## Context

CompareFlow is an independent portfolio project with no customers. The first plan used 5-8 testers to compare it with Excel, measuring speed, a trust score and a System Usability Scale score. No outside testers will take part, so those numbers can't be measured.

## Decision

Drop the speed, trust and SUS goals. Check the product in two ways that need no outside users:

- **Scenario tests:** automated tests run the 9 fake quotes through the app and compare the results with hand-worked answers: the cheapest supplier, landed cost, and every seeded trap flagged.
- **Heuristic self-review:** the Figma prototype in Phase 3 and the finished app in Phase 5 are reviewed against Nielsen's 10 usability heuristics, with major issues fixed.

## Consequences

- Every goal can be measured and repeated in CI by one person.
- The results show that the app works as specified. They don't show that people use it faster than Excel, or that they trust it, so neither can be claimed.
- A self-review misses problems that a new user would find, and the reviewer built the app. This remains a known limit (risk R4).
