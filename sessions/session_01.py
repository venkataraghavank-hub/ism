"""Session 1: a guided, decision-led Vandelay management tutorial."""
from __future__ import annotations

import html
import streamlit as st

# Each decision teaches a distinction, then asks the student to use it as Chris's manager.
DECISIONS = [
    dict(block="The management problem", title="The Red Queen", concept="The Red Queen race: firms keep investing just to hold their position when rivals can copy their technology.",
         scene="Vandelay has bought ERP, service tools and sensors. Rivals can buy similar products. Chris Burns asks why the spending never seems to end.",
         prompt="Before another purchase, what would you ask Chris to define?",
         options=["The newest vendor feature", "The business result to improve and how the system would produce it", "The rival's IT budget"],
         feedback=["Features can be copied. Trace the feature to a change in work and an outcome.", "The Red Queen explains the investment pressure; a business value anchor makes a purchase purposeful.", "Rival spending shows the race, but cannot tell Chris where Vandelay will create value."], key=1),
    dict(block="The management problem", title="An information system", concept="An information system joins technology and data with people and processes to accomplish work. A software licence is one component.",
         scene="The ERP vendor promises accurate inventory. Departments still disagree about product codes, stock ownership and approvals.",
         prompt="What should Chris coordinate alongside the software?",
         options=["More ERP features alone", "Common data, process steps, roles and decision rights", "A more attractive dashboard alone"],
         feedback=["More features do not reconcile conflicting product records or approvals.", "These arrangements allow the technology to support reliable transactions across departments.", "A dashboard may display discrepancies without fixing their cause."], key=1),
    dict(block="Criterion 1 · the IT portfolio", title="Infrastructure", concept="Infrastructure is the shared technical foundation on which many applications run: connectivity, computing, storage, security and identity services.",
         scene="The service app fails whenever Vandelay's network link drops. Chris can fund one common upgrade.",
         prompt="Which request is primarily an infrastructure investment?",
         options=["A company-wide reliable network and identity service", "A custom technician scheduling application", "A cleaned customer list"],
         feedback=["Yes. The shared foundation enables multiple applications; manage its reliability, capacity and standards.", "This is an application using infrastructure to perform a task.", "This is a data asset; it depends on infrastructure but is not itself the foundation."], key=0),
    dict(block="Criterion 1 · the IT portfolio", title="Applications", concept="Applications perform particular tasks. Operational applications support recurring work; strategic applications support a distinctive way to compete.",
         scene="Vandelay considers standard order processing and a proprietary uptime service built around its installed base.",
         prompt="How would you distinguish the two applications?",
         options=["Both are infrastructure because they need servers", "Order processing is operational; the distinctive uptime service may be strategic", "Both are data because they generate records"],
         feedback=["Running on servers does not make an application infrastructure.", "The first needs dependable routine transactions; the second needs a defensible customer promise and ongoing adaptation.", "They produce and use data, but both are applications that organise work."], key=1),
    dict(block="Criterion 1 · the IT portfolio", title="Data", concept="Data are the records and definitions that systems use. Quality, ownership, access and shared meaning matter as much as storage.",
         scene="Three teams use different customer IDs. Chris wants a reliable view of service history across plants.",
         prompt="Which request directly addresses the data asset?",
         options=["Buy another server", "Clean and reconcile customer IDs, define ownership and access", "Launch another service app before reconciling records"],
         feedback=["A server stores records but cannot decide which customer IDs refer to the same account.", "This creates a usable shared asset for applications and decisions.", "A new app will inherit conflicting records and may spread the problem."], key=1),
    dict(block="Criterion 1 · the IT portfolio", title="A portfolio choice", concept="The portfolio lens separates infrastructure, operational and strategic applications, and data. Each category calls for a different managerial priority.",
         scene="Chris has four requests: network resilience, order processing, a differentiated uptime offer and clean installed-base records.",
         prompt="How should he frame the investment meeting?",
         options=["Rank requests only by purchase price", "Separate their roles, value and managerial imperatives", "Treat them as one interchangeable digital budget"],
         feedback=["Price alone hides what each asset enables and how it must be managed.", "This exposes the distinct decisions: shared reliability, process performance, differentiation and trusted data.", "A single budget is possible, but the management questions remain different."], key=1),
    dict(block="Criterion 2 · three worlds", title="Function IT", concept="Function IT assists an individual's task. It can enable experimentation and more precise work, but users need skill and a suitable task.",
         scene="Vandelay engineers need to test pump designs and compare performance before manufacturing.",
         prompt="Which proposal most directly builds this capability?",
         options=["An engineer's design simulator", "A technician discussion network", "A company-wide ERP purchasing workflow"],
         feedback=["The simulator supports an engineer's experimentation and precision: function IT.", "A discussion network connects people and their contributions: network IT.", "ERP coordinates a shared process across units: enterprise IT."], key=0),
    dict(block="Criterion 2 · three worlds", title="Network IT", concept="Network IT connects people to exchange knowledge and coordinate less prescribed interactions. Participation and useful contributions matter.",
         scene="Field technicians repeatedly solve the same unusual pump failure at different customer sites.",
         prompt="What would let their solutions travel across Vandelay?",
         options=["A personal simulator for each technician", "A searchable technician community with norms for sharing cases", "A mandated purchase approval sequence"],
         feedback=["A personal tool may help one worker without spreading the solution.", "The network enables discovery and sharing; norms and participation make it valuable.", "A prescribed workflow coordinates transactions, not emergent field knowledge."], key=1),
    dict(block="Criterion 2 · three worlds", title="Enterprise IT", concept="Enterprise IT coordinates activities across groups through a common process. It usually requires process redesign and standard data.",
         scene="Procurement, inventory and finance must agree on purchase orders and stock movements.",
         prompt="Which proposal addresses their shared workflow?",
         options=["A stand-alone engineering tool", "An informal discussion forum", "An ERP process with common item codes, approvals and roles"],
         feedback=["A local task tool does not coordinate these departments.", "A forum can help discussion, but does not enforce a common transaction process.", "This is enterprise IT: coordinated work supported by agreed process and data."], key=2),
    dict(block="CCR · making value real", title="Capability and complement", concept="A capability is what the technology lets people do. A complement is a change around the technology needed to realise that capability.",
         scene="A simulator can test design alternatives, but engineers rarely use it because they lack training and time in the design review.",
         prompt="Which statement correctly separates the capability from its complement?",
         options=["Capability: training; complement: simulation", "Capability: test alternatives; complement: training and time in design reviews", "Capability and complement both mean the software licence"],
         feedback=["This reverses the terms. Training helps realise the simulator's capability.", "The tool enables experimentation; skills and task routines turn it into actual practice.", "The licence alone cannot describe the work enabled or the organisational change needed."], key=1),
    dict(block="CCR · making value real", title="Responsibility", concept="Responsibility means a manager owns selection, adoption and realised business value, rather than stopping at purchase or installation.",
         scene="The ERP goes live, but teams bypass it and inventory errors persist. Chris asks whether the project is finished.",
         prompt="What should the accountable manager do next?",
         options=["Declare success because the software is live", "Track use and outcomes, resolve process and data barriers, and assign owners", "Wait for a newer ERP version"],
         feedback=["Go-live is a milestone, not evidence of business value.", "Responsibility continues through adoption, changed work and outcomes. This completes the CCR lens.", "A version upgrade does not resolve the present ownership and workflow problem."], key=1),
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def go_to(stage: int) -> None:
    st.session_state.ism_stage = stage
    st.rerun()


def render_session_01() -> None:
    count = len(DECISIONS)
    st.session_state.setdefault("ism_stage", 0)
    stage = min(st.session_state.ism_stage, count)
    st.markdown('<div class="hero"><div class="eyebrow">SESSION 01 · INTERACTIVE TUTORIAL</div><h1>Vandelay: manage the IT race</h1><p>Advise Chris Burns. Each short concept prepares you for a management decision; compare options as you go.</p></div>', unsafe_allow_html=True)
    if stage < count:
        item = DECISIONS[stage]
        st.progress(stage / count, text=f"Decision {stage + 1} of {count} · {item['block']}")
        with st.container(border=True):
            st.markdown(f'<div class="stage">{esc(item["block"])} · {esc(item["title"])}</div><div class="case"><strong>Before you decide</strong><br>{esc(item["concept"])}</div><div class="compact">VANDELAY SITUATION</div><p>{esc(item["scene"])}</p><div class="prompt">{esc(item["prompt"])}</div>', unsafe_allow_html=True)
            selection = st.radio("Your call", item["options"], index=None, key=f"ism_s1_choice_{stage}")
            if selection is not None:
                idx = item["options"].index(selection)
                st.markdown(f'<div class="debrief"><strong>What your choice means</strong><br>{esc(item["feedback"][idx])}</div>', unsafe_allow_html=True)
                st.caption("You can choose another option to compare its implications. There are no marks.")
        left, _, right = st.columns([1.2, 3, 1.5])
        with left:
            if stage and st.button("← Previous", use_container_width=True):
                go_to(stage - 1)
        with right:
            label = "View summary →" if stage == count - 1 else "Continue →"
            if st.button(label, type="primary", disabled=selection is None, use_container_width=True):
                go_to(stage + 1)
    else:
        st.progress(1.0, text=f"{count} of {count} decisions complete · Summary")
        render_summary()
    with st.expander("Concept map and reading trail"):
        st.markdown("""
| Lens | Question | Course reading |
|---|---|---|
| Red Queen | Why can investments fail to create lasting advantage? | Amrit Tiwana, *IT Strategy for Non-IT Managers*, introductory chapter |
| Information system and portfolio | What assets and arrangements produce business value? | Tiwana; Session 1 deck; *A Conversation About Information Technology* (2004 and 2026 edition) |
| Three worlds | What does each type of IT enable and require? | Andrew McAfee, *Mastering the Three Worlds of Information Technology* |
| CCR | Who makes the capability work and owns the result? | Session 1 course framework |
""")
        st.caption("The tutorial paraphrases the assigned readings; consult the course copies for the full arguments.")


def render_summary() -> None:
    count = len(DECISIONS)
    if any(st.session_state.get(f"ism_s1_choice_{i}") is None for i in range(count)):
        go_to(0)
    st.markdown('<div class="hero"><div class="eyebrow">SESSION 01 · SUMMARY</div><h1>From technology purchase to business value</h1><p>Your choices show where the manager must look beyond the product.</p></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("### What to take into the next session")
        st.markdown("""
1. **Red Queen → value anchor.** Rivalry pressures firms to invest; begin with the business outcome.
2. **Information system → working arrangement.** Technology, data, people and processes must fit together.
3. **Criterion 1 → portfolio.** Infrastructure provides a shared foundation; applications perform work; data provide usable records. Operational and strategic applications serve different purposes.
4. **Criterion 2 → three worlds.** Function IT aids individual tasks; network IT connects contributors; enterprise IT coordinates a common process.
5. **CCR → managerial action.** Name the capability, build the complements and assign responsibility for adoption and value.
""")
    with st.container(border=True):
        st.markdown("### Your Configuration")
        picks = [DECISIONS[i]["options"].index(st.session_state[f"ism_s1_choice_{i}"]) for i in range(count)]
        for heading, indices in [
            ("The business problem", (0, 1)), ("The portfolio", (2, 3, 4, 5)),
            ("The three worlds", (6, 7, 8)), ("CCR", (9, 10)),
        ]:
            with st.expander(heading):
                for i in indices:
                    item = DECISIONS[i]
                    st.markdown(f"**{item['title']}:** {item['options'][picks[i]]}")
                    st.caption(item["feedback"][picks[i]])
        portfolio = sum(picks[i] == DECISIONS[i]["key"] for i in (2, 3, 4, 5))
        worlds = sum(picks[i] == DECISIONS[i]["key"] for i in (6, 7, 8))
        ccr = sum(picks[i] == DECISIONS[i]["key"] for i in (9, 10))
        parts = ["You anchored the decision in a business outcome." if picks[0] == 1 else "Revisit the business outcome behind the purchase.",
                 "You connected technology with people, process and data." if picks[1] == 1 else "Revisit what makes a software purchase a working information system.",
                 "Your portfolio distinctions are clear." if portfolio == 4 else "Compare the portfolio examples again.",
                 "You distinguished the three IT worlds." if worlds == 3 else "Compare function, network and enterprise IT again.",
                 "Your CCR choices link capabilities, complements and ownership." if ccr == 2 else "Revisit capabilities, complements and managerial responsibility.",
                 "Try another option to explore the implications."]
        debrief = " ".join(parts)
        assert len(debrief.split()) <= 50
        st.markdown(f'<div class="debrief"><strong>Debrief</strong><br>{esc(debrief)}</div>', unsafe_allow_html=True)
    a, b, _ = st.columns([1.3, 1.1, 2])
    with a:
        if st.button("← Review decisions", use_container_width=True):
            go_to(count - 1)
    with b:
        if st.button("Start again", use_container_width=True):
            for i in range(count):
                st.session_state.pop(f"ism_s1_choice_{i}", None)
            go_to(0)
