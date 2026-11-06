# Figma Education to Astro: Limits, Integrations, and Workflow

## Executive Summary

- **Education Is Not Unlimited AI**: Figma Education includes **3,000 AI credits per person per month**, with no pooling or rollover. Exhausting the allowance stops credit-consuming AI actions until the next reset or a move to an eligible paid plan. -> Reserve AI for high-value design decisions rather than repeated whole-site regeneration. [4]
- **Eligibility Changes the Available Products**: Higher-education and bootcamp Education users can access AI tools, including Make and the Design agent; K-12 and high-school Education users cannot. -> Check the existing account's verified education category before planning the workflow. [7]
- **Design Agent and Make Solve Different Problems**: The Design agent edits native design structure; Make produces functional prototypes and web apps. The Design agent began consuming the shared AI credit budget on **October 6, 2026**. -> Use Design for the visual specification and Make selectively for interaction experiments. [18][14][19]
- **Official MCP Is No Longer Read-Only**: Current tools include direct canvas editing through `use_figma`, live-UI capture through `generate_figma_design`, and local-project import through `send_code_to_figma`. -> Distinguish native design editing, rendered-page capture, and code import instead of treating them as interchangeable. [12]
- **Codex Supports a Roundtrip, Not a Sync Guarantee**: OpenAI documents code-to-editable-Figma and design-to-code workflows. Figma separately distinguishes captured flat layers from native component-aware editing. -> Make every transfer an explicit, reviewed operation; do not expect continuous synchronization. [23][10]
- **Lovable's Official Figma Integration Runs Toward Lovable**: The official plugin, MCP connection, and `.fig` upload bring Figma material into Lovable. Reverse transfer into Design is available through rendered-page capture, including html.to.design. -> Preserve Lovable source separately; a captured canvas is not an imported application. [6][5]
- **Keep Astro as the Production Destination**: For the conference website, my recommendation is Figma Design as the visual contract, an Astro repository as the implementation authority, and Make or Lovable as optional experiments. -> Validate responsive behavior, accessibility, content, and performance in the actual site, not just its canvas representation.

**Scope:** Findings are framed for **2 November 2026**. Explicit policy dates appear below. Where the available evidence does not establish an exact quota, price, or compatibility guarantee, it is identified as unresolved rather than assumed. No account, subscription, repository, or permission changes were made.

## 1. Education: 3,000 Credits, With Important Eligibility Boundaries

### Confirmed Education allowances and restrictions

| Area | Confirmed position | Practical consequence |
|---|---|---|
| AI allowance | **3,000 credits per person per month**. [4] | This is not 3,000 prompts or an unlimited AI entitlement. |
| Ownership | Credits are individual, not shared across teammates. [4] | A teammate's unused balance does not replenish yours. |
| Reset and rollover | Monthly reset; unused credits do not roll over. [4] | Plan work around the account's displayed reset date. |
| Exhaustion | Credit-consuming AI actions stop until reset or a move to a plan with additional-credit options. [4] | Do not depend on a last-minute AI-generated redesign. |
| AI eligibility | Higher-education and bootcamp users have access; K-12/high-school Education users do not. [7] | An Education badge alone does not establish Make access. |
| Figma Sites | Eligible higher-education/bootcamp users can publish **one Site file they created**; custom domains are unavailable. [7] | Education Sites is not the same as production hosting for a custom-domain conference site. |
| Visual search | Visual search in the Figma editor is unavailable on Education; Community-resource visual search is available. [7] | Do not assume complete parity with every paid AI feature. |
| Education teams | The higher-education page permits an **unlimited number of Education teams** and describes Professional-equivalent team features and benefits. [17] | Unlimited teams must not be read as unlimited AI usage. |

The actionable distinction is between the collaboration/design entitlement and the separately metered AI allowance. The Education-specific credit article does **not state an additional daily AI cap**; the general credit documentation's daily cap applies to Starter-plan users and View-seat users. These should not be silently substituted for Education's stated monthly allowance. [4][8]

### Eligibility and account status

Figma's Education help article requires a current student or educator in a classroom, a school email, and sufficient age to consent independently. Its higher-education landing page also lists an age floor of **13**, structured classroom participation, and qualifying educational institutions; it excludes self-directed education and educational institutions' marketing departments. The general age floor is not a promise that every younger student can access AI. [7][17]

Education status is tied to the verified email address: changing that address after verification revokes the status. Figma also describes reverification requirements for Make and Sites access. For this project, inspect the existing status rather than changing the account email or moving teams. [7]

**Conference-site case:** A student designing a conference site as coursework has a different eligibility situation from an institution's marketing department commissioning its public event site. The latter is explicitly excluded from the higher-education page's qualifying categories. Do not treat an individual's student status as blanket institutional licensing authorization. [17]

**Decision:** Use the existing Education workspace for eligible design work, but confirm the project's educational purpose. Exact Education-specific maximum member counts, storage limits, and file/page quotas were not established in the available evidence; do not substitute Starter limits or claim every resource is unlimited.

## 2. Design Agent Versus Make: Outputs and Credit Costs

### Choose the output before choosing the AI tool

| Dimension | Agent in Figma Design | Figma Make |
|---|---|---|
| Primary output | Native screens, layouts, auto layout, component edits, styles, variables, and content. [18] | Functional prototypes and web apps, with editable project code. [14] |
| Strong fit for this project | Establishing the conference site's visual system and reusable page patterns. | Testing a schedule filter, registration flow, or other behavior before production implementation. |
| Context | Can use attached material and connected libraries, including components, styles, and variables. [18] | Make supports library/package context through Make kits, including npm packages, library styles, and guidelines. [24] |
| Credit model | Variable by task complexity, agent actions, and supplied context; uses the shared AI balance. [18][19] | Variable consumption; shares the same credit budget as the generally available Design agent. [8][19] |
| Important limitation | Some design operations remain unsupported or forthcoming. [18] | Exported code is not evidence of an automatic Astro conversion or a continuously synchronized Design file. |

For team-file editing, the Design agent requires a **Full seat and edit access**. View, Dev, and Collab seats, or view-only file access, permit chat without file edits. The agent documentation separately allows people to request edits in their Draft files. It is available in Figma Design in a desktop app or web browser. [18]

The agent is not a complete replacement for manual design work. Its documentation marks vector editing/Draw tools, icon creation, slots, and prototyping/interactions as coming soon. Asset export, contacting support, and diagram/data-visualization creation are unsupported by this agent; Figma points to FigJam AI for diagrams and visualizations. [18]

### Exact credit rates that were established

Figma states that the following consumption rates are current as of **October 15, 2026**, and may change. [8]

| AI action | Published credit consumption |
|---|---:|
| FigJam template or diagram prompt | **2-24 credits** |
| Remove an image background | **1-5 credits** |
| Vectorize an image | **2-5 credits** |
| Boost image resolution | **5-10 credits** |
| Add interactions | **20 credits per use** |
| Figma Make and agentic tasks | **Variable**, not a fixed per-prompt price |

These rates come from Figma's credit-consumption table. They do not support a fixed conversion such as "3,000 credits equals 300 Make prompts." [8]

**Conference-site case:** Ask the Design agent to produce and refine the header, typography, speaker card, session card, and ticket call-to-action using a connected library. Then use a small Make experiment only if the schedule interaction is genuinely difficult to specify on a static canvas. This concentrates variable-cost generation on reusable decisions rather than regenerating every page.

**Decision:** Use native Design work for the deliverable that the Astro developer will implement. Use Make for a specific behavioral question, not as a mandatory intermediate destination.

## 3. Current Rules Versus Dated Pricing and Beta Claims

Several apparently contradictory claims are explained by policy changes or by confusing seat allowances with purchased credits.

| Date or status | Official statement | What it does not mean |
|---|---|---|
| **March 2026** | Figma introduced ways to purchase additional AI credits. [19] | Education automatically gains paid-plan top-up options. |
| **August 25, 2026** | Purchased credit subscriptions and pay-as-you-go allocations increased at the same cost: **2x** for Professional and **1.6x** for Organization/Enterprise. [19] | Included seat credits doubled. Figma explicitly says they did not change. [19] |
| **October 6, 2026** | The Design agent moved from open beta to general availability and began consuming AI credits. [19] | Older "Design agent is free during beta" advice remains current. |
| **October 15, 2026** | Figma dates its published consumption-rate table to this day; code layers launched in open beta and consume credits, with a limited-time exception for eligible users. [8] | A promotional allowance applies to every Education user or remains permanent. |
| Current canvas-writing documentation | MCP canvas writing is free during beta and is intended to become usage-based paid functionality. [10] | The Design agent and MCP writing have identical billing rules. |

For comparison, the general credit table lists monthly Full-seat allowances of **500** on Starter, **3,000** on Professional, **3,500** on Organization, and **4,250** on Enterprise. Dev, Collab, and View seats on the paid plans listed receive **500** monthly credits. Starter users and View-seat users also have a **150-credit daily limit**. These are general plan/seat figures, not a replacement for the Education-specific article. [8]

Figma's update FAQ directs administrators to their dashboard for current purchased-credit pricing. The evidence here does not establish a dependable dollar price for each current add-on tier. More importantly, Education's own article describes waiting for reset or moving to a paid plan, rather than purchasing an Education top-up in place. No upgrade is recommended as part of this report. [19][4]

**Decision:** Budget against the Education-specific **3,000-credit monthly balance**, and treat beta promotions and older credit-package examples as dated exceptions. The AI Balance menu shows used credits, remaining credits, and the next reset. [4]

## 4. Official MCP: Platforms, Read Tools, and Write Tools

### Remote and desktop are different capability surfaces

| Connection | Requirements and reach | Important constraints |
|---|---|---|
| **Remote server** | Recommended; connects to `https://mcp.figma.com/mcp`; does not require the Figma desktop app. [13] | Required for direct canvas writing and sending live web UI to Figma. [13] |
| **Desktop server** | Runs through the Figma desktop app; requires a Dev or Full seat on a supported plan, including Education. [11] | Supports selection-based context, but not canvas writing or sending UI to Figma. [11][12] |
| **Figma for Government** | Desktop server only. [11][13] | Remote server, `use_figma` canvas writing, and `generate_figma_design` capture are unavailable. [11] |
| **Xcode** | Remote server only. [9] | Do not follow a desktop-server setup recipe for Xcode. |

The official supported-client list includes Amazon Q, Amp, Android Studio, Augment Code, Claude Code, Claude Desktop, ClickUp, Codex by OpenAI, Copilot CLI, Cursor, Dia, Factory, Firebender, Gemini CLI, Junie by JetBrains, Kiro, Linear, Meta Muse, Mistral, Notion, OpenCode, Openhands, Replit, Sarvam Agents, VS Code, Warp, and Xcode. Client support does not imply that every client exposes every write or capture capability. [13]

### Read and write tool families

| Purpose | Official tool names | What to distinguish |
|---|---|---|
| Design/context inspection | `get_design_context`, `get_metadata`, `get_screenshot`, `get_variable_defs`, `get_figjam`, `download_assets` | Reading structure or imagery is not modifying a file. [12] |
| Libraries and implementation mapping | `get_libraries`, `search_design_system`, `get_code_connect_map`, `get_code_connect_suggestions`, `get_context_for_code_connect`, `add_code_connect_map` | Code Connect mapping is distinct from editing visual design. [12] |
| Motion, shaders, plugins, identity | `get_motion_context`, `get_shader`, `list_shaders`, `list_file_shaders`, `get_generative_plugin`, `list_generative_plugins`, `whoami` | These are specialized context/inspection capabilities, not a universal export pipeline. [12] |
| Native canvas editing | `use_figma` | Runs through the Plugin API to create or edit real design structure. [10] |
| Existing UI and HTML conversion | `generate_figma_design`, `html_to_figma` | Live-UI capture and HTML conversion create design layers; they are different from component-aware native editing. [12][10] |
| Code-project import | `send_code_to_figma` | Imports a local project as a Make file or code layer; it is not itself a promise of continuous synchronization. [12] |
| Content/file creation | `create_new_file`, `generate_diagram`, `generate_image`, `create_shader`, `create_generative_plugin`, `upload_assets` | Separate operations exist for files, diagrams, images, shaders, and plugins. [12] |
| Development guidance | `create_design_system_rules` | Listed among desktop-server tools; do not confuse it with canvas capture. [11] |

`use_figma` supports Design pages, frames, components, variants, variables, styles, text, and images; FigJam objects; and Slides content. It cannot add new images by itself: `upload_assets` supplies images, and `generate_image` can create them first. [12]

Writing requires edit access, a supported client, and the remote server. A Full seat is required to write outside Drafts. The write feature is offered on Professional, Education, Organization, and Enterprise plans. [10][13]

### Quotas: do not confuse MCP calls with AI credits

An exact Education-specific numeric MCP call ceiling was **not established in the available evidence**. Education support is confirmed, but this report does not label it unlimited or apply a Starter call allowance to it. The tools reference specifically says `generate_figma_design` does not count toward the standard MCP server rate limits; this exception does not establish the allowance for every other tool. [11][12]

**Decision:** Prefer remote MCP for the proposed Codex workflow. Check the client's specific capture/write support and the account's live access limits before relying on a large automated operation.

## 5. Codex: A Practical Roundtrip, Not Automatic Synchronization

OpenAI's **February 26, 2026** partnership announcement describes bringing context from Figma Design, Make, or FigJam into Codex to implement in code, then turning UI from code into editable Figma designs for further exploration. It describes this as a roundtrip workflow and provides a Figma MCP installation route in the Codex desktop application. [23]

The practical distinction is between three operations:

| Operation | Result | What remains your responsibility |
|---|---|---|
| Design -> Codex | Design context informs implementation. [23] | Choosing the Astro architecture, checking fidelity, and reviewing generated code. |
| Running UI -> Design | Capture produces editable layers; Figma describes this path as flat-layer capture. [23][10] | Reconstructing reusable components, variables, and responsive intent where needed. |
| Agent -> Native canvas | `use_figma` can create and update real components, variables, and layout structure. [10] | Reviewing the edits and deciding which changes should be implemented in code. |

Editable output is therefore not synonymous with a fully reconstructed design system. Nor does a successful return capture prove a stable mapping between every source component and every Figma layer.

**Conference-site case:** Start with an approved Figma home page, speaker detail page, and schedule pattern. Give Codex those specific references and the implementation requirements, then review the Astro result in a browser. Capture selected implemented views back into a separate Figma review area when visual iteration would help.

Keep the return capture separate from the approved component library. If the captured speaker grid reveals spacing or hierarchy problems, improve the canonical design and implement an explicit patch in Astro. This prevents an imperfect capture from silently replacing the source design.

**Decision:** Treat the loop as **inspect -> implement -> render -> capture/review -> patch**. Do not promise automatic two-way sync, lossless conversion, shared component identity, or conflict resolution merely because both directions are possible. The documented capabilities are transfers and edits, not a guarantee of a continuously reconciled shared source of truth. [23][10]

## 6. Lovable: Import the Right Artifact Into the Right Product

### What each transfer actually brings across

| Route | Confirmed capability | Fidelity or access limitation |
|---|---|---|
| **Figma plugin -> Lovable** | Exports designs directly into a Lovable workspace. [6] | Requires at least a Dev seat in the Figma organization; one export supports up to **100 files**, each up to **20 MB**. [6] |
| **Figma MCP -> Lovable** | Lovable reads open Figma design files. [6] | Requires Lovable desktop, Figma desktop with Dev Mode, and a Dev or Full Figma seat; unavailable on Starter. Enterprise local MCP is disabled by default unless an admin enables it. [6] |
| **`.fig` upload -> Lovable** | Supplies design-system values and a high-level file summary. [6] | Does **not** recreate the designs or components. [6] |
| **Lovable rendered page -> Figma Design** | html.to.design converts a captured preview or published URL into editable Figma layers. [5] | Complex CSS animations do not transfer; custom fonts need manual installation. [5] |
| **Local code project -> Make/code layer** | Figma's MCP tool list includes `send_code_to_figma` for this purpose. [12] | This is not a documented Lovable-specific, lossless project importer or an established Astro compatibility guarantee. |

Lovable says plugin export and `.fig` upload are free; prompting Lovable to build from the supplied design is normal credit-consuming build usage. These Lovable build credits should not be confused with Figma's AI balance. [6]

### Reverse capture is useful, but it is not application migration

html.to.design's own documentation describes editable frames/groups, text, colors, styling, component arrangements, spacing, and auto layout. Its Chrome-extension route can capture a preview; its URL route fetches a published page. The documented animation and font losses are important warnings against calling the conversion lossless. [5]

For a Lovable conference prototype, import representative rendered states into a reference page in Design. Then rebuild the reusable header, speaker cards, session cards, and ticket CTA as deliberate native components. Preserve the working Lovable project separately; a visual capture is not evidence that data, routes, authentication, or application logic migrated.

### Preserve code separately, and distinguish real Git sync

Lovable's GitHub documentation does describe **two-way code sync**: Lovable changes go to GitHub, and changes pushed to the active GitHub branch return to Lovable. It edits and syncs one branch at a time. Git sync creates a new repository rather than attaching the project to an existing one; repository code can instead enter through ZIP/Upload code before connecting sync. [15]

By contrast, Make's general advanced guide describes ZIP download and pushing Make code to a newly created GitHub repository. It says edits made outside Make do not automatically return and must be supplied manually. That documented hosted-Make export flow must not be confused with Lovable's explicit two-way Git sync. [14]

Figma also has local-codebase documentation that labels access **closed beta for a limited number of users**. The existence of that route is not a general Education entitlement. Exact local-import framework support, size limits, and eligibility were not established here. [20]

**Decision:** For this project, use reverse capture to recover visual ideas and preserve Lovable code as reference. Do not make the Astro delivery dependent on a universal Lovable-to-Make importer or on presumed local-beta access.

## 7. Complementary Tools: A Small Stack With Clear Jobs

The following is a recommended evaluation stack, not a claim that every product, integration, or paid feature is included in Figma Education.

| Need | Suggested tools | How I would use them for the conference site |
|---|---|---|
| Canonical design system | Native Figma components, variables, styles, and auto layout | Define typography, spacing, colors, speaker cards, session cards, buttons, and responsive rules before page generation. |
| Repository-owned tokens | Tokens Studio + Style Dictionary | Evaluate when token changes need a controlled path into CSS variables; begin with a small token set rather than a complex synchronization system. |
| Component review | Storybook, if a substantial component library warrants it | Evaluate framework support before committing; do not assume an Astro-native setup is identical to a React setup. |
| Lightweight motion | CSS first; Motion's JavaScript API where useful | Keep effects isolated from the page framework and require a reduced-motion behavior. |
| Bespoke interactive graphics | Rive | Reserve for a distinctive hero or meaningful interactive illustration, with a static fallback. |
| Functional and visual regression | Playwright | Test mobile navigation, schedule filtering, registration links, anchor navigation, and approved viewport screenshots. |
| Accessibility review | axe-based automated checks plus keyboard and screen-reader testing | Use automation as one layer, not the acceptance decision by itself. |
| Performance and delivery | Lighthouse and browser performance tools | Evaluate the actual Astro build, images, fonts, motion, and third-party embeds. |
| Recovering an existing Lovable visual | html.to.design | Capture a useful reference state, then normalize the design system. |

The first-party documentation discovered for these candidates includes Tokens Studio's GitHub sync and Style Dictionary guides, Motion's `animate` reference, Rive's reduced-motion guide, and Playwright's visual-comparison and accessibility-testing guides. Their current paid-tier terms and any account-specific quotas are outside the confirmed findings in this report.

**Conference-site case:** The schedule is the highest-value validation target. A visually attractive grid is insufficient if attendees cannot identify the day, track, time zone, room, or registration action. Build the schedule with realistic long titles and speaker names, then test keyboard access and narrow-screen behavior before spending time on decorative motion.

This separation of appearance from usability is supported by the research context: a CHI study evaluates **138 mobile UI screens** from Figma, Banani, and Stitch against Nielsen's **10 usability heuristics**. UI-Bench also explains why pairwise judgments can be more useful than noisy absolute aesthetic scores. Neither source establishes a current winner for this particular conference workflow. [25][26]

**Decision:** Start with native Figma design structure and a compact browser-testing stack. Add token automation or advanced motion only when a concrete recurring need justifies the maintenance.

## 8. Conference Website: Recommended Design-to-Astro Workflow

This is an implementation recommendation, not a claim that Figma or Lovable automatically produces production-ready Astro code.

| Stage | Deliverable | Acceptance gate |
|---|---|---|
| **1. Establish constraints** | Audience, content inventory, event dates/time zone, ticket destination, accessibility target, and ownership | Confirm existing Education access and project eligibility; no account changes. |
| **2. Preserve the prototype** | Lovable source/reference and selected rendered captures | Separate source code, screenshots, and editable Figma layers. |
| **3. Build the design system** | Tokens and native components for navigation, cards, schedule, sponsors, tickets, and footer | Components work with long content and narrow layouts. |
| **4. Resolve difficult behavior** | One focused Make experiment if necessary | The experiment answers a specific question; it is not a compulsory site rewrite. |
| **5. Approve representative pages** | Home, programme/schedule, speaker detail, venue/travel, ticket information | Approve hierarchy and responsive behavior before filling every page. |
| **6. Implement in Astro** | Repository-owned pages, layouts, components, assets, and structured content | Review code, content, browser rendering, and external registration boundaries. |
| **7. Review the roundtrip** | Selected implementation captures in a separate Figma review area | Record intentional differences and implement explicit patches. |
| **8. Validate and release** | Functional, visual, accessibility, and performance results | Test the real deployed experience, not only the prototype. |

### Keep production structure independent of the prototype tool

For a mostly informational conference site, I would begin with static Astro pages and structured speaker/session data. Add client-side behavior only where it earns its complexity, such as schedule filtering. Keep secrets and registration authorization out of browser-only prototypes; even OpenAI's site-building guidance explicitly calls for server-enforced access rules for shared or personal records. [27]

Ask Codex to implement approved patterns in small increments. A useful first slice is the global layout plus one speaker card and one session card, followed by a full schedule state. This exposes content and responsive problems before a large generation creates expensive rework.

### Make the credit budget serve decisions

Use the Design agent's library context to keep new material consistent with existing components and variables. Its support for connected libraries makes this preferable to asking for unrelated fresh designs at every iteration. [18]

Keep an issue list outside the AI conversation: visual mismatch, missing content, keyboard failure, performance regression, or intentional deviation. Batch related design corrections, review them, and then request a targeted code patch. Do not let repeated whole-site prompting consume the shared **3,000-credit** Education allowance. [4][19]

**Decision:** The final handoff is an approved design system plus an independently testable Astro site. A functioning Make or Lovable prototype is useful evidence, but not the production acceptance criterion.

## Synthesis: Choose the Authority, Then Control the Transfers

The central distinction is not which tool can generate the most impressive first screen. It is which artifact should remain authoritative, how changes cross the boundary, and what is lost during transfer.

| Approach | Mechanism | Scope | Main trade-off | Recommended role |
|---|---|---|---|---|
| **Figma Design agent** | Native component/layout/variable editing. [18] | Design specification | Shared, variable-cost AI usage; incomplete operation coverage. [18][19] | Canonical visual design |
| **Figma Make** | Functional prototype/web-app generation and editable code. [14] | Behavioral exploration | Another code artifact to maintain; do not assume bidirectional hosted export. [14] | Targeted experiment |
| **Lovable** | Application building with documented two-way Git sync. [15] | Prototype/application code | Its code sync does not establish synchronization with Figma or Astro | Preserve an existing prototype and its source |
| **Codex + official Figma MCP** | Read context, implement code, capture UI, or edit native canvas. [23][10] | Bridge between tools | Broad capabilities do not guarantee lossless conversion or conflict-free sync | Explicit, reviewed transfers |
| **Astro repository** | Recommended production implementation authority | Deployed conference experience | Requires deliberate implementation and validation | Final source of truth for behavior and delivery |

Three tensions matter. First, **editable is not necessarily reusable**: captured layers can be useful without recovering the original component model. Second, **bidirectional capability is not automatic synchronization**: Lovable explicitly documents two-way Git behavior, while the Figma/Codex roundtrip describes separate operations. Third, **free Education collaboration is not free unlimited generation**: the Design agent and Make share a finite AI balance. [10][15][23][4][19]

My recommendation is therefore straightforward: **keep Figma Design authoritative for appearance, Astro authoritative for production, and use Codex/MCP to move deliberately between them**. Import the existing Lovable site's rendered appearance only where it saves useful work. Use Make only when a behavioral experiment reduces uncertainty. This produces a clearer handoff and avoids making the conference launch dependent on an unverified quota, a closed beta, or an imagined automatic-sync feature.

## References

### Figma official documentation

- **AI credits on the Education plan** - monthly allowance, reset, ownership, and exhaustion rules. [4]
- **Figma for Education** - eligibility, product restrictions, Sites allowance, and verification. [7]
- **Figma for higher education** - classroom categories, exclusions, and Education-team entitlement. [17]
- **How Figma AI credits work** - plan allocations, daily-cap scope, action costs, and rate date. [8]
- **AI credit updates FAQ** - purchased-credit changes and Design-agent general availability. [19]
- **Work with the Figma agent in design files** - access, outputs, and limitations. [18]
- **Guide to the Figma MCP server** - remote/desktop distinction and client catalog. [13]
- **Set up the desktop server** - seat requirements and unsupported remote capabilities. [11]
- **Set up the remote server** - Xcode and connection details. [9]
- **Tools and prompts** - tool names, canvas operations, and capture-rate exception. [12]
- **Write to canvas** - native editing, capture distinction, permissions, and beta billing. [10]
- **Beyond the basics: Using Figma Make** - ZIP export and GitHub push workflow. [14]
- **Make in your local codebase: Setup, gotchas, and troubleshooting** - limited closed-beta availability. [20]
- **Figma Make** - Make-kit design-system context. [24]

### OpenAI, Lovable, and import documentation

- **OpenAI Codex and Figma launch seamless code-to-design experience** - announcement and roundtrip workflow. [23]
- **OpenAI: Create a site** - server-enforced access rules for shared/personal records. [27]
- **Lovable: Bring Figma designs into Lovable** - plugin, MCP, `.fig`, limits, and credit treatment. [6]
- **Lovable: Sync your Lovable project with GitHub** - two-way sync, repository creation, and code-upload alternative. [15]
- **html.to.design: All the ways to import from Lovable to Figma** - rendered-page import and fidelity limitations. [5]

### Complementary first-party guides and validation research

- Tokens Studio: **GitHub - Git Sync Provider**; **Style Dictionary + SD Transforms**.
- Motion: **animate** documentation.
- Rive: **Reduced Motion** documentation.
- Playwright: **Visual comparisons**; **Accessibility testing**.
- Astro: **View transitions** documentation.
- **Looks Good, But Is It Usable? Evaluating Usability in AI-Generated Mobile User Interfaces** - heuristic evaluation of 138 screens. [25]
- **UI-Bench** - rationale for pairwise design comparisons. [26]

## References

1. *Manage AI credits – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits
2. *Make in your local codebase – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/40775535020695-Make-in-your-local-codebase
3. *How Figma AI credits work – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work
4. *AI credits on the Education plan – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/37611757713431-AI-credits-on-the-Education-plan
5. *All the ways to import from Lovable to Figma*. https://html.to.design/docs/from-lovable-to-figma
6. *Bring Figma designs into Lovable*. https://docs.lovable.dev/integrations/figma
7. *Figma for Education – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/360041061214-Figma-for-Education
8. *How Figma AI credits work – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/33459875669015-How-Figma-AI-credits-work
9. *Set up the remote server (recommended) | Developer Docs*. https://developers.figma.com/docs/figma-mcp-server/remote-server-installation
10. *Write to canvas | Developer Docs*. https://developers.figma.com/docs/figma-mcp-server/write-to-canvas
11. *Set up the desktop server | Developer Docs*. https://developers.figma.com/docs/figma-mcp-server/local-server-installation
12. *Tools and prompts | Developer Docs*. https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/
13. *Guide to the Figma MCP server – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server
14. *Beyond the basics: Using Figma Make – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/35710574222487-Beyond-the-basics-Using-Figma-Make
15. *Sync your Lovable project with GitHub*. https://docs.lovable.dev/integrations/github
16. *Figma for Education | Free tools*. https://www.figma.com/education
17. *Figma for higher education*. https://www.figma.com/education/higher-education/
18. *Work with the Figma agent in design files – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/37998629035799-Work-with-the-Figma-agent-in-design-files
19. *AI credit updates FAQ – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/42614902212887-AI-credit-updates-FAQ
20. *Make in your local codebase: Setup, gotchas, and troubleshooting – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/40789739982871-Make-in-your-local-codebase-Setup-gotchas-and-troubleshooting
21. *Use Git with Figma Make and code layers – Figma Learn - Help Center*. https://help.figma.com/hc/en-us/articles/44220165255063-Use-Git-with-Figma-Make-and-code-layers
22. *Figma Make, Now on Your Local Code | Figma Blog*. https://www.figma.com/blog/figma-make-now-on-your-local-code
23. *OpenAI Codex and Figma launch seamless code-to-design experience | OpenAI*. https://openai.com/index/figma-partnership
24. *Figma Make: Create with AI-Powered Design Tools*. https://www.figma.com/make
25. *Looks Good, But Is It Usable? Evaluating Usability in AI-Generated Mobile User Interfaces | Proceedings of the Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems*. https://dl.acm.org/doi/full/10.1145/3772363.3799002
26. *UI-Bench: A Benchmark for Evaluating Design Capabilities of AI Text-to-App Tools*. https://arxiv.org/pdf/2508.20410
27. *Create a site | ChatGPT Learn*. https://learn.chatgpt.com/docs/sites/creating-a-site
