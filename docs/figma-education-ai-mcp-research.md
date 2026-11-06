# Figma Education, AI usage, and design–code workflows

**Research checked:** 2–3 November 2026. **Prepared for:** the ACBLPE 2027 conference website and similar projects.

This report separates documented product capabilities from recommended workflows. It does not establish your personal balance or entitlement: your Figma account, Education category, seat, file ownership, and beta rollout were not inspected. No Figma connection, subscription change, import, or Astro build was performed.

## 1. Answers to your main questions

| Question | Finding |
| --- | --- |
| Is Education AI unlimited? | No. Education includes **3,000 AI credits per person per month**. See the allowance and reset rules below. |
| Can I use Figma MCP in Codex? | **Yes.** Figma documents Codex support for reading designs and remote canvas writing. |
| Can changes travel in both directions? | **Yes, through several distinct workflows.** Agent-driven design edits, UI captures, code imports, and Git changes are supported. This does not establish continuous, lossless synchronization between every design layer and source component. |
| Can I bring a Lovable project into Figma? | **Yes:** capture rendered screens as editable design layers, or bring the project code into Figma Make/a code layer. GitHub is the useful bridge for continuing code collaboration. |
| What should I use here? | Keep the vanilla playground for exploration, use Figma for approved visual decisions, and use Codex with the remote Figma connection for implementation and comparison. Start Astro only in the later build phase. |

The first two answers follow the [Education credit policy](https://help.figma.com/hc/en-us/articles/37611757713431-AI-credits-on-the-Education-plan) and [Figma client matrix](https://developers.figma.com/docs/figma-mcp-server/). The workflow conclusions combine the sources in sections 5–7.

## 2. What the Education plan gives you—and where it stops

### Ordinary design access

Higher education, approved bootcamp, and high-school Education accounts receive Professional-plan access; institution-managed K–12 access has a different arrangement. **AI, including Make and the Design agent, and Sites are available to higher-education/bootcamp users, not high-school/K–12 users.** Confirm which category your verification uses. Eligible Education users can publish one Figma Sites file they created, without a custom domain. Editor visual search is also excluded. [Figma for Education](https://help.figma.com/hc/en-us/articles/360041061214-Figma-for-Education)

Professional includes unlimited files/projects for a team and team design libraries. Those ordinary design benefits do not imply unlimited AI generation. [Figma pricing and feature comparison](https://www.figma.com/pricing/)

Education access expires: higher-education students receive one year and educators two years; verified bootcamp students receive six months and educators two years. Reverification is required where applicable. Also ensure that the working team actually has Education status; account verification and team setup are separate steps. [Education access and application process](https://help.figma.com/hc/en-us/articles/360041061214-Figma-for-Education)

### AI allowance and reset

- Credits belong to each person, are not pooled with teammates, reset monthly, and do not roll over.
- At zero, credit-consuming AI actions stop until reset or an eligible plan change.
- Open a Figma file → **Main menu → AI balance** to see usage, remaining credits, and the actual reset date.
- The Education-specific policy directs users needing extra credits to a paid plan; it does not offer an Education top-up path.
- Professional Full has the **same 3,000-credit base allowance**. Paying mainly opens additional-credit options; it does not inherently multiply the included budget.
- A separate paid team lets you retain the Education team. Upgrading the existing team ends free Education collaboration there.

[Education AI credit and upgrade policy](https://help.figma.com/hc/en-us/articles/37611757713431-AI-credits-on-the-Education-plan)

**My recommendation:** measure several normal sessions before considering an upgrade. The generic pricing page says AI add-ons are available across plans, but the Education-specific instructions are narrower. Confirm Education purchase eligibility in your account before spending money; this report uses the specific policy for Education.

## 3. How far those credits will go

### Credits are not prompts

Agent costs depend on the model, task, amount of context, and work performed. One prompt may trigger several actions. Planning and building can both incur costs. The allowance is shared across Figma's credit-consuming features, rather than being a fresh allowance for every product. [How Figma AI credits work](https://help.figma.com/hc/en-us/articles/33459875669015-How-Figma-AI-credits-work)

Figma's published examples give a sense of scale, **not a guaranteed price list for your prompts**:

| Example | Published illustrative consumption |
| --- | ---: |
| Change fonts with the Make/Design agent | 30+ credits |
| Make: add interactivity to a design | 75+ |
| Make: create an app from scratch | 100+ |
| Design agent: create a five-screen checkout | 300+ |
| Create a code layer | 250+ |
| AI search / layer renaming | Free in the listed fixed-action schedule |

Examples vary by model and task; some Make examples are dated February 2026. Use the in-product receipt for actual consumption. [Figma's consumption examples](https://help.figma.com/hc/en-us/articles/33459875669015-How-Figma-AI-credits-work)

A more useful personal estimate is:

```text
Approximate remaining iterations = remaining credits / recent average credits per iteration

Illustration only: 2,400 remaining / 120 average ≈ 20 similar iterations
```

Do not treat this as a guaranteed number of completed screens. A responsive page, its mobile variant, a rewritten navigation, and a second art direction can each be separate substantial jobs.

### Two recent changes explain apparently unlimited usage

The Design agent and Weave tools in Design became generally available on **6 October 2026** and began consuming credits. Older beta announcements can therefore be misleading. [AI credit updates FAQ](https://help.figma.com/hc/en-us/articles/42614902212887-AI-credit-updates-FAQ)

Code-layer generation/editing has a separate promotion **through 4 November 2026 on paid plans**. Other agent work in the same prompt can still cost credits, and normal code-layer charging follows the promotion. The announcement does not clearly grant this paid-plan promotion to Education users; check your receipt rather than assume eligibility. [Config India code-layer promotion](https://help.figma.com/hc/en-us/articles/43663368947863-What-s-new-from-Config-India-2026)

### Practical ways to stretch your allowance

Give a constrained first brief, supply only relevant frames/context, reuse a foundation, and make small text/spacing corrections directly. For Make, reusable guidelines and task-appropriate models can help; long chat histories and unnecessary backend context can add cost. Planning itself is not free. [Figma's credit optimization guidance](https://help.figma.com/hc/en-us/articles/40097793879191-Best-practices-for-optimizing-AI-credits-in-Figma-Make)

For this conference, my suggested experiment is one representative desktop page plus a mobile variant, followed by a speaker card, programme row, and registration call to action. Record the cost after each batch. Reuse the chosen tile motif, type scale, and spacing system across the remaining content instead of repeatedly requesting an entire new site.

## 4. Three separate usage meters

| Meter | Relevant limit or behavior |
| --- | --- |
| Figma AI credits | The monthly allowance described above; native agent/image work can consume it. |
| Figma MCP reads | **Education: up to 200 tool calls/day and 10/minute.** A single user request can cause multiple calls. |
| External agent usage | Codex, Claude, Cursor, or Lovable has its own subscription/usage accounting. Figma Education does not supply that allowance. |

Figma's comparison: Professional Full/Dev also gets 200/day and 10/minute; Organization Full/Dev 200/day and 15/minute; Enterprise Full/Dev 600/day and 20/minute. View/Collab seats generally get 20/month.

The MCP quota concerns reads. Write tools and `whoami` are exempt. Most MCP tools do not spend Figma AI credits; image generation and Make-agent work do. The initial code import is credit-free; subsequent AI changes cost credits. Standalone Weave uses its own credits. [MCP limits and credit exceptions](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/)

**Practical implication:** external-agent canvas work has different accounting from asking Figma's own Design agent to do it. Canvas writing is currently a free beta, with future usage-based pricing announced. It should not be budgeted as permanently free or unlimited. [Write-to-canvas access](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)

## 5. Which agents and platforms support Figma MCP?

MCP is the connection between an agent and Figma's tools. Client support varies by server and operation.

The following groups reproduce Figma's documented client matrix as checked on the research date. “Not listed” means that capability is not marked in the matrix, not proof it can never work.

| Clients | Desktop server | Remote server | Remote canvas writing |
| --- | --- | --- | --- |
| **Codex** | Yes | Yes | Yes |
| Augment Code, Claude Code, Claude Desktop, Copilot CLI, Cursor, Factory, Firebender, Kiro, OpenCode, VS Code, Warp | Yes | Yes | Yes |
| Android Studio, Gemini CLI | Yes | Yes | Not listed |
| Dia, Linear, Meta Muse, Xcode (beta) | Not listed | Yes | Yes |
| Replit | Not listed | Yes | Not listed |
| Amazon Q, Openhands | Yes | Not listed | Not listed |

[Figma's official compatibility matrix](https://developers.figma.com/docs/figma-mcp-server/)

Live-browser capture has a narrower documented client list: Augment, Claude Code, **Codex**, Cursor, Factory, Firebender, VS Code, Warp, and Xcode 27 beta. Check this capability separately from basic design reading. [Code-to-canvas compatibility](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/)

Figma requires a client in its MCP catalog; generic support for the MCP protocol alone is insufficient. For this project, use the recommended **remote endpoint**, `https://mcp.figma.com/mcp`, for broad functionality without needing the Figma desktop app. [Remote installation and supported clients](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)

### Codex setup

**Preferred in the app:** open Plugins, find Figma, install it, and complete Figma authorization. Figma's documented plugin setup includes workflow guidance; manual server configuration alone does not install the skills. The catalog check in this research found Figma available but not installed/connected. [Figma's Codex setup instructions](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)

**CLI alternative**, if using a standalone Codex CLI instead of the app plugin:

```sh
codex mcp add figma --url https://mcp.figma.com/mcp
codex mcp login figma
codex mcp list
```

OAuth is supported; follow the browser sign-in flow. Avoid configuring the same server twice through separate installation paths. The installed local CLI's help was checked for these commands, but they were **not executed** to add a connection. [OpenAI MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

After connecting, ask the agent to identify the active Figma account/plan/seat and list available tools, then read one small test frame. For remote access, paste a **frame or layer link**. Current-selection prompting is specific to the desktop server. [Figma tool usage](https://help.figma.com/hc/en-us/articles/42495147242903-Tools-and-example-prompts)

## 6. What “sync” actually means

| Direction / workflow | What happens | What still needs deliberate work |
| --- | --- | --- |
| Figma design → local code | Codex reads layout, screenshots, variables, assets, and component information, then edits the repository. | Framework choices, semantics, responsiveness, behavior, and verification. |
| Local code → native Figma design | An agent creates or updates native canvas objects using write tools. | Choosing target nodes, preserving design intent, and reviewing modifications. |
| Running webpage → design layers | Capture a page, element, or visible state as editable Figma layers. | Rebuilding a reusable component system and validating capture fidelity. |
| Local project → Make / code layer | Import running-code material into Figma. | Dependencies, runtime compatibility, backend configuration, and later maintenance. |
| Figma-connected code → GitHub | Work on a clone/branch and push changes or create a pull request. | Review/merge decisions and deployment. |
| Lovable ↔ its synced Git branch | Code commits synchronize through the configured Git integration. | Unsynced branches, publishing, and backend changes. |

This table is a workflow synthesis of the sources below; it is not a claim that MCP supplies one universal synchronization engine.

### Native canvas edits

The remote `use_figma` tool can create/edit actual frames, components, variants, variables, and auto layout through the Plugin API. This is more structured than taking a screenshot or capturing rendered HTML. Canvas writing requires appropriate plan/file access and is in beta; Figma's documentation lists Education. Use the official workflow skills and a named exploration page when trying it. [Write to canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)

Writing outside Drafts requires a Full seat. [Figma MCP access overview](https://developers.figma.com/docs/figma-mcp-server/)

### Screen capture

`generate_figma_design` captures live UI as editable **flat layers**. Capturing the programme page does not establish a permanent binding to its programme-row source component. After editing the captured design, supply the changed frame link and ask the agent to implement the changes. This is an explicit iteration loop. [Code to canvas](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/)

`html_to_figma` is another route for self-contained HTML. It does not fetch external resources referenced by the document, so assets/styles must be packaged appropriately. It is not equivalent to running a complete application with its backend. [Developer tool reference](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)

### Running code inside Figma

A **code layer** is an interactive prototype backed by code on the Design canvas. You can extract its visible states as design layers and apply design changes back through the agent. This feature is rolling out in open beta, so availability can differ between accounts. MCP code-layer imports require a Full seat and may take ten minutes or more. [Code layers in Figma Design](https://help.figma.com/hc/en-us/articles/44193259600535-Code-layers-in-Figma-Design)

Figma Make code/assets can also be read by an agent through MCP resources when supported by the client. That enables reuse in a repository; it does not itself maintain an automatic repository connection. [Make resources through MCP](https://developers.figma.com/docs/figma-mcp-server/bringing-make-context-to-your-agent/)

### Code Connect is a mapping aid

Code Connect associates design components with real code components and their usage. It improves the context an agent receives; it does not keep all source code and design geometry synchronized. Current eligibility pages list Professional, Organization, Government, and Enterprise Full/Dev seats, but do **not explicitly name Education**. Verify entitlement before making it a dependency. For this conference, a simple component-to-file mapping document is a reasonable starting point. [Code Connect access and behavior](https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect)

## 7. Bringing a Lovable project into Figma

### Route A: editable screens for visual redesign

1. Open the relevant Lovable preview or run its exported repository locally.
2. Put it in the required page/state and viewport.
3. Ask Codex to capture that UI into a specified Figma file.
4. Repeat for mobile and important states, then organize/rework the layers in Figma.

This is my recommended route when the objective is **visual exploration or a designer handoff**. Capture is based on the rendered interface, so it is useful even when the app's full runtime is difficult to reproduce inside Figma. It should not be described as importing the application's database or business logic. The official Figma Chrome extension offers a browser-based alternative for creating editable design layers. [Figma webpage-to-design workflows](https://help.figma.com/hc/en-us/articles/40826832449303-Turn-coded-screens-into-editable-design-layers)

### Route B: project code through MCP

1. Connect the Lovable project to GitHub and clone its repository locally.
2. Confirm the app runs and identify its actual startup/build commands.
3. Ask Codex to import the project into the chosen Figma Make file or as a code layer.
4. Resolve any unsupported runtime or backend assumptions and verify the resulting preview.

The developer reference calls the archive-import tool **`send_code_to_figma`** and documents ZIP/TAR archives. This creates Make/code-layer content, **not native design layers**. [Developer import reference](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)

The Help Center currently calls the same category of operation **`import_codebase`**. This naming discrepancy is why your prompt should describe the outcome and let the agent inspect the live tool catalog, rather than rely on a hardcoded tool name. [Help Center tool list](https://help.figma.com/hc/en-us/articles/42495147242903-Tools-and-example-prompts)

### Route C: GitHub for continuing code iteration

Lovable's GitHub integration is available across plans and creates a repository for the connected project. Use that repository as the shared code source for Codex and Figma. This is different from importing an arbitrary existing repository to create a new Lovable project. [Lovable GitHub integration](https://docs.lovable.dev/integrations/github)

Figma can clone a GitHub web repository, use branches, and push changes or open pull requests. Its documented requirements include a runnable frontend, an entry point and build command, and a repository under **3 GB**. Any web framework is supported in principle; private npm registries and repositories requiring private-network access are not. Local-folder uploads are limited to **100 MB** and have no live GitHub connection. A one-time MCP/archive import should likewise not be assumed to establish Git sync automatically. [Figma Git integration and repository limits](https://help.figma.com/hc/en-us/articles/44220165255063-Use-Git-with-Figma-Make-and-code-layers)

```text
Lovable ↔ configured Git branch ← reviewed merges ← Figma code branch / Codex branch
                                          |
                                          └─ run preview → capture states → Figma designs
```

Lovable synchronizes one branch at a time. A Figma/Codex branch reaches Lovable after merging into that branch or changing the selected branch. Sync updates the preview; publishing remains separate. Git transfers code, not a complete copy of hosted data and managed credentials. Local code changes do not consume Lovable chat credits, but called services may still incur charges. [Lovable Git-sync behavior](https://docs.lovable.dev/integrations/git-sync-overview)

**My recommendation:** begin with a front-end-only import or representative page using sample content. Do not assume a Lovable app's managed backend and credentials will work inside a Figma runtime. Check the actual repository rather than treating every Lovable project as the same framework/template.

## 8. Tools and libraries worth considering

These are selective recommendations for this workflow, not a proposal to install everything.

| Tool | Useful role here | Recommendation |
| --- | --- | --- |
| **Figma variables, components, auto layout** | Palette, type, spacing, tile motifs, speaker cards, programme rows. | Start here; a consistent source design improves handoff. [Figma feature reference](https://www.figma.com/pricing/) |
| **Tokens Studio + Style Dictionary** | Store design tokens and transform them into CSS/custom properties or other platform outputs. | Add if the four visual themes become a maintained system. Define which side owns tokens and review updates in Git. Some Tokens Studio sync features are paid. [Tokens Studio](https://docs.tokens.studio/), [Style Dictionary](https://styledictionary.com/) |
| **Figma Chrome extension** | Capture an existing browser page as editable design layers without an agent-driven capture session. | Useful for the vanilla playground and Lovable previews. [Official extension guide](https://help.figma.com/hc/en-us/articles/9067379354135-Figma-Chrome-extension) |
| **Motion for JavaScript** | Staggered tile entrances, SVG path drawing, and coordinated transitions in vanilla JS or later Astro client scripts. | Introduce only if CSS animations become awkward; it does not require React. [Motion JS documentation](https://motion.dev/docs/quick-start) |
| **Figma Motion / motion-context handoff** | Communicate keyframes, easing, and timing rather than describing animation only in prose. | Check feature availability; MCP's motion tool can provide keyframe information and CSS/Motion snippets. [Motion-context tool](https://help.figma.com/hc/en-us/articles/42495147242903-Tools-and-example-prompts) |
| **Playwright** | Compare approved browser screenshots after later code changes. | Establish stable desktop/mobile baselines after design approval; keep rendering conditions consistent. [Visual comparisons](https://playwright.dev/docs/test-snapshots) |
| **axe-core with Playwright** | Catch common contrast, label, and semantic issues. | Combine with keyboard, screen-reader, and reduced-motion review; automation is incomplete. [Accessibility testing](https://playwright.dev/docs/accessibility-testing) |
| **Code Connect** | Map a reusable design system to an established component library. | Optional later; check Education entitlement first. [MCP integration](https://developers.figma.com/docs/figma-mcp-server/code-connect-integration/) |

For this content-driven conference site, I would begin with native Figma structure, the existing CSS/JS playground, Codex, and eventual browser verification. Add token automation or a motion library only when the design creates a concrete need.

## 9. Suggested workflow for ACBLPE 2027

1. **Explore:** choose an azulejo-related palette and motif in the existing vanilla study. Keep content from the conference outline and distinguish supplied facts from placeholders.
2. **Bring the study into Figma:** capture representative desktop/mobile views, then turn repeated visual elements into deliberate components and variables.
3. **Design and approve:** supply responsive frames, component states, real content, asset rights, and motion/reduced-motion behavior using the existing intake specification.
4. **Implement later:** provide the final Figma node links to Codex, explicitly request Astro and reuse the agreed tokens/components. Figma's default React/Tailwind snippets do not dictate the project's framework. [Framework-specific prompting](https://help.figma.com/hc/en-us/articles/42495147242903-Tools-and-example-prompts)
5. **Close the loop:** compare the browser output at agreed widths, capture relevant differences back into Figma where useful, and apply reviewed changes through Git.

Suggested prompts to save:

```text
Read this Figma frame and its variables: <frame URL>.
Explain its responsive rules and missing states. Do not edit the repo yet.

Capture the existing conference playground into <Figma file URL> at desktop
and mobile widths. Put the captures on a new Exploration page.

Import this local Lovable project as a code layer in <Figma file URL>.
Inspect the available import tool and runtime requirements first.
Report what transferred and what needs configuration.

For the later build: implement <approved frame URL> in Astro using our
existing content specification and design tokens. Verify browser output
against the supplied desktop/mobile designs and reduced-motion behavior.
```

These are recommendations and reusable prompts, not actions performed by this research.

Related project files: [website and design-intake specification](/Users/saheelwagh/coding/hackathon/confsite/docs/acblpe-2027-website-spec.md) · [vanilla design-study guide](/Users/saheelwagh/coding/hackathon/confsite/design-study/README.md).

## 10. What remains account-specific

Before relying on the workflow, check your Education category and team status, AI balance/reset date, Full-seat access for code-layer import, beta availability, and the live MCP tool list. Code Connect Education eligibility and the paid-plan code-layer promotion were not conclusively established for your account. No particular import or design-to-code result was tested because no Figma connection or Lovable repository was supplied for execution.

The linked official documentation is the basis for the conclusions. Product limits and beta terms may change; recheck sections 2–5 when beginning the actual build. Community-tool research could not be completed because the connector required authentication; no community consensus is claimed.

An additional automated deep-research run completed under interaction ID `trun_d3e68bfaf0ec423699f05f09ccfd0f46`. Its original [Markdown output](/Users/saheelwagh/coding/hackathon/confsite/docs/research/figma-parallel-research.md) and [metadata/source basis](/Users/saheelwagh/coding/hackathon/confsite/docs/research/figma-parallel-research.json) are preserved as supplementary material. Those raw outputs were not individually audited and may differ from current documentation; use this verified synthesis for decisions. The interaction ID can be reused for follow-up research.
