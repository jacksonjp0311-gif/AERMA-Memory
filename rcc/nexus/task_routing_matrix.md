# RCC Nexus Task Routing Matrix

| Task type | Read first | Likely edit surface | Required validation | Nexus update obligation |
|---|---|---|---|---|
| Read-only review | `README.md`, `docs/context/rcc_nexus_index.json` | None | None unless claims are made | No update unless stale context found |
| Documentation change | `README.md`, target folder README | README/docs files | RCC check + Nexus check | Update affected Echo Location if role/hooks changed |
| RCC/Nexus change | `rcc/nexus/README.md`, `docs/context/rcc_nexus_index.json` | `rcc/nexus`, `docs/context`, README | RCC check + Nexus check | Always update Nexus index/report |
| Runtime change | `src/aerma/README.md` | `src/aerma/**`, tests | pytest + suite + guard | Update Echo Location if hooks/validation/evidence changed |
| Scoring change | `src/aerma/benchmarks/README.md` | scoring/classifier/runner/tests | pytest + suite + guard | Update validation/evidence claims |
| Task-suite change | `tasks/README.md` | tasks/suite/tests | pytest + suite + guard | Update route map and validation surface |
| Evidence change | `src/aerma/evidence/README.md` | evidence compiler/ledgers/reports | pytest + suite + evidence inspection | Update evidence surface in Nexus |
| Public claim change | README + validation surface | README/docs/context | full validation | Update non-claim locks and claim boundaries |
