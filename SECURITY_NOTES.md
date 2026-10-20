# Security notes before cloud deployment

- No API keys, passwords, access tokens, or IBM credentials should be committed to Git or placed in source code.
- Keep `.env` local; `.gitignore` excludes it. Use IBM Cloud / watsonx secret or credential management for deployed credentials.
- The `.env.example` file contains placeholders only.
- The bundled HR dataset and row-level employee records should be treated as sensitive. Upload only when authorized and necessary; prefer aggregate data for dashboard sharing.
- The dashboard currently displays and permits downloading filtered row-level data. Before sharing publicly or with broad audiences, remove that table/download or restrict access and minimize fields.
- The API error response has been changed not to return raw exception text to callers. Keep detailed errors in protected server logs if needed.
- `.git` history was excluded from this secured package to avoid carrying any credentials that might have existed in earlier commits. This does not clean the original repository history. If a real credential was ever committed, revoke/rotate it and clean the remote history as appropriate.
- Only load trusted `.joblib` model files; joblib/pickle artifacts can execute code when loaded.
