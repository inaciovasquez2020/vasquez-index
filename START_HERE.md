# Start Here: Verified Frontier Tracking

## One-sentence description

Vasquez Research builds **Verified Frontier Tracking**: an AI-readable and human-checkable system for tracking hard research claims without confusing proved results, conditional bridges, interface objects, and open frontiers.

## Layman description

This is a truth scoreboard for difficult research.

It shows:

- what is actually verified,
- what is conditional,
- what is only an interface,
- what remains open,
- and what must not be overclaimed.

## Why it matters

Hard research often fails publicly because claims become unclear.

A reader may not know whether something is:

- a finished theorem,
- a proposed reduction,
- a conditional bridge,
- a formal interface,
- a verified software surface,
- or an open frontier.

Verified Frontier Tracking exists to keep those categories separate.

## Public stack

| Layer | Repository | Role |
|---|---|---|
| Front door | `vasquez-index` | Public navigation and start-here map |
| Transparency proof | `frontier-status-dashboard` | Public dashboard for CI health, repository integrity, theorem-boundary status, and review readiness |
| Explanation layer | `urf-textbook` | Human-readable exposition, archive, and release-facing documentation |
| Definitions layer | `urf-core` | Trusted definitions, schemas, verification artifacts, and claim-boundary infrastructure |
| Technical demonstration | `chronos-urf-rr` | Executable URF/Chronos frontier implementation with tests, verifiers, status files, and CI |

## First thing to inspect

Start with the dashboard.

The dashboard is the first public proof of transparency because it exposes repository health and theorem-boundary status instead of hiding unresolved frontiers.

Dashboard:

https://frontier-status-dashboard.vercel.app

## What is already real

Verified Frontier Tracking already provides:

- public repositories,
- status documents,
- verifier scripts,
- tests,
- CI checks,
- dashboard reporting,
- release-facing documentation,
- and explicit boundary statements.

## What is not claimed

This public stack does not claim theorem-level closure of:

- Chronos-RR,
- H4.1/FGL,
- P vs NP,
- any Clay Millennium problem,
- or any frontier whose assumptions remain open.

A result is treated as theorem-level closed only when the relevant artifact explicitly names the theorem and discharges its assumptions.

## How to read the work

Read in this order:

1. `vasquez-index` — start-here map.
2. `frontier-status-dashboard` — public transparency surface.
3. `urf-textbook` — explanation and archive layer.
4. `urf-core` — definitions and schemas.
5. `chronos-urf-rr` — technical demonstration.

## Minimal claim

The minimal public claim is:

> Verified Frontier Tracking is a public, AI-readable, human-checkable infrastructure method for separating verified results, conditional bridges, interface objects, and open research frontiers.

## Boundary

This document is a navigation object.

It does not prove any theorem.

It does not promote any conditional result.

It does not convert any open frontier into theorem-level closure.

It identifies the public entry path for inspecting the system.

## Formal Status

Status: Documentation / Index Surface

It does not independently prove mathematical claims.

Every theorem-level claim must inherit from a buildable formal source repository.

`docs/status/SOURCE_OF_TRUTH_2026_04_27.md`
