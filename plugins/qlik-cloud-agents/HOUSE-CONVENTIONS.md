# Shared house conventions

## The permission model

No agent writes to a live tenant — or a local `.qvf` — unless the task it was dispatched with contains a line beginning `APPROVED:` that names the exact objects. Without that line, an agent returns exactly what it *would* do under a "Proposed changes (awaiting approval)" heading and stops. This exists because a subagent can't pause mid-task to ask a question — whatever needs a human decision has to be settled before dispatch, not during.

Each plugin's README documents the hard stops that apply even under an approval.

## House conventions

Both plugins ship the same defaults — table prefixes (`FACT_`/`DIM_`/`TMP_`/…), field conventions (`%KeyName`, `_HiddenField`, `#Counter`), a namespaced variable scheme (`vL.`/`vG.`/`vD.`/`vP.`/`vT.`/`vU.`), and a canonical script tab order.

If your project has its own `CLAUDE.md` declaring different naming rules or a house regional `SET` block, every writer, reviewer and builder is instructed to check for it and defer to it, falling back to the shipped neutral defaults (`en-GB`, ISO dates) only when nothing is declared.

The conventions are duplicated into each agent file on purpose — plugin agents don't reliably have your project's `CLAUDE.md` in context, so each one is self-sufficient. Changing a shipped default means editing every agent that states it, in both plugins.

