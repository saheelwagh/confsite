# Site content and visual map

The canonical deliverable is `../ACBLPE-2027-Site-Content-and-Visual-Map-Linked.docx`. It was refreshed from the local site preview on 7 November 2026. `inventory.json` and `screenshots/` contain 69 current component captures across five pages at desktop, tablet and mobile widths.

`inventory-before-site-update.json` and `update_inventory_for_site_changes.py` retain the earlier pending-preview workflow for reference. Do not run that update script on the current inventory: it deliberately starts from the older capture.

Use the configured document Python environment with Playwright, `python-docx`, `Pillow`, `lxml`, and `pypdfium2`. Follow the Documents skill's artifact-operation marker, Google Docs title sanitizer, and render-and-inspect requirements. With `http://localhost:4321` running, regenerate from this directory with:

```text
python capture.py
python capture.py --cuts-only
python build_document.py
python link_document.py
python <Documents skill>/scripts/google_docs_title_sanitize.py ../ACBLPE-2027-Site-Content-and-Visual-Map-Linked.docx --out linked-sanitized.docx
python <Documents skill>/scripts/google_docs_title_sanitize.py linked-sanitized.docx --check
mv linked-sanitized.docx ../ACBLPE-2027-Site-Content-and-Visual-Map-Linked.docx
python render_document.py ../ACBLPE-2027-Site-Content-and-Visual-Map-Linked.docx --output_dir render-linked --dpi 144 --emit_pdf
python check_linked_render.py
```

`link_document.py` regenerates the component-to-device and screenshot-to-text bookmarks and validates their targets. `check_linked_render.py` validates the rendered link destinations. Inspect every rendered page image before delivering the document. `render_document.py` expects the bundled LibreOffice image at its configured mount path.
Replace `<Documents skill>` in the commands above with the installed Documents skill directory.

`capture.py` requires Playwright Chromium and the locally installed Google Chrome at the path configured in that script. It uses reduced motion and captures all five pages plus shared navigation and footer at 1440, 768, and 390 pixel widths. The `--cuts-only` pass records safe image-splitting positions for long components.

The current map includes the landing hero's 25th-conference heading and September 2027 label, both new-tab ACBLPE links, the registration notice, and the four-language review guidance. The exact site copy, including `guidlines` and `Langauges`, is preserved for review in the document.
