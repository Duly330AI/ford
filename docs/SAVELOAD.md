# Save/Load

## Format
- JSON (gzip) standard; MsgPack optional
- Integrität: SHA-256 über unkomprimierte Nutzlast
- `schema_version` im Root

## Slots
`saves/slot-1/last.save`, `auto-###.save`, `quick.save`

## Policy
- Kein Save während aktiver Kampfauflösung/Animation
- Autosave: Raumwechsel, Craft fertig, Elite-Kill (gedrosselt)

## Migration
- `save_migrate.py` vN→vN+1, Tests mit Fixtures
