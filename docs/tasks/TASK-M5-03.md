- [ ] ID: TASK-M5-03
  Title: Serializer (JSON/Gzip + MsgPack, Checksummen)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/serializer.py`, `tests/systems/test_serializer.py`
  DependsOn: TASK-M5-01, TASK-M5-02
  Notes:
  API: dump(data, format="json", gzip=True) -> bytes; load(payload, format) -> data. Speichere SHA-256 ueber unkomprimierte Nutzlast in meta.checksum.
  Acceptance:
  - [ ] Serializer unterstuetzt JSON+gzip obligatorisch und optional MsgPack.
  - [ ] Checksumme validiert Payload; Fehler bei Mismatch.
  Tests:
  - [ ] Roundtrip fuer JSON+gzip und MsgPack.
  - [ ] Checksumme-Korruption fuehrt zu ValidationError.
