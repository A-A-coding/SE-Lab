# Lab 1 – Requirements Engineering & UML Use-Case Modelling

**Course:** Software Engineering
**Problem Statement:** #22 – Smart Cities, Transport & Logistics
**Title:** Smart Parking Space Rental & License Validator

## Problem Overview

A smart city parking system that handles real-time bay reservations, calculates progressive hourly rates, validates vehicle number plates via gate cameras, and flags unauthorized overstays.

**Actors:** Vehicle Owner, Parking Warden, Gate Camera System (external)

## Repository Contents

| File | Description |
|---|---|
| `Requirements_Table.docx` | Requirements table with 5 Functional Requirements (FR-001–FR-005) and 2 Non-Functional Requirements (NFR-001, NFR-002), each with ID, Type, Description, Priority, Acceptance Criteria, and Rationale. |
| `UseCase_Diagram.pdf` | UML use-case diagram showing all actors, use cases, and relationships, including at least one `<<include>>` and one `<<extend>>` dependency. |
| `UseCase_Flow_MakePayment.docx` | One-page use-case flow specification for the "Make Payment" use case, detailing preconditions, postconditions, main success scenario, and an alternate flow (payment declined). |

## Use-Case Summary

| ID | Use Case | Actor(s) |
|---|---|---|
| UC-01 | Reserve Parking Bay | Vehicle Owner |
| UC-02 | Scan License Plate | Vehicle Owner, Gate Camera System |
| UC-03 | Validate Reservation | *(included by UC-02)* |
| UC-04 | Calculate Billing | *(included by UC-05)* |
| UC-05 | Make Payment | Vehicle Owner |
| UC-06 | Apply Discount | *(extends UC-05)* |
| UC-07 | Flag Overstay | Parking Warden |

**Relationships modelled:**
- `<<include>>` — Scan License Plate always includes Validate Reservation
- `<<include>>` — Make Payment always includes Calculate Billing
- `<<extend>>` — Apply Discount optionally extends Make Payment

## Requirements Table Snapshot

| Req ID | Type | Priority | Summary |
|---|---|---|---|
| FR-001 | Functional | High | Record entry time via plate scan; compute tiered billing on exit |
| FR-002 | Functional | High | Allow advance reservation of a specific bay/slot |
| FR-003 | Functional | High | Validate scanned plate against active reservation at gate |
| FR-004 | Functional | Medium | Auto-flag and notify warden on overstay |
| FR-005 | Functional | Medium | Support multiple payment methods and discount codes |
| NFR-001 | Nonfunctional | High | Gate camera lookup API responds in under 300 ms |
| NFR-002 | Nonfunctional | High | System maintains 99.9% uptime |

## Tools Used

- Requirements table & use-case flow: Microsoft Word (.docx)
- Use-case diagram: drawn per UML use-case modelling conventions (actors, system boundary, associations, `<<include>>`/`<<extend>>` stereotypes)

## Author

*Adithya Ajeeth – PES1UG24CS022 – Section 5A*
