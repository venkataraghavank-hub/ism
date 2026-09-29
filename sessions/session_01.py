"""Session 1: an interactive management tutorial based on the assigned readings."""
from __future__ import annotations

import html
import streamlit as st

STAGES = [
    "The Red Queen", "What is the system?", "See the portfolio",
    "Choose a capability", "Make it work", "Advise Chris", "Your configuration",
]

DECISIONS = [
    {
        "scene": "Vandelay has invested in ERP, field service tools and sensors. Rivals quickly buy similar products. Chris Burns asks why the spending never seems to end.",
        "prompt": "What question should Chris settle before approving another technology purchase?",
        "options": [
            "Which vendor offers the newest features?",
            "Which business result must improve, and what would make the technology produce it?",
            "How much are our rivals spending?",
        ],
        "feedback": [
            "A feature lead can disappear when rivals buy the same product. Ask how this feature changes Vandelay’s work and produces value.",
            "Start with a business result. The Red Queen explains the pressure to keep investing; ISM asks how investments become a capability that rivals cannot simply purchase.",
            "Rival spending explains the race, but it does not tell Chris which activity to improve or how to capture value.",
        ],
        "lens": "Tiwana · Red Queen and the business value anchor",
    },
    {
        "scene": "A vendor says its ERP licence will solve inaccurate inventory and late fulfilment. The rollout team has not agreed on item codes, approvals or who owns stock records.",
        "prompt": "What would you ask the rollout team to do first?",
        "options": [
            "Install the software and let each department retain its own data definitions.",
            "Agree on process steps, common data formats, roles and decision rights before rollout.",
            "Add more dashboard views for Chris.",
        ],
        "feedback": [
            "A licence is only one component. Incompatible item codes and approvals would keep the information system from working across departments.",
            "An ERP becomes an information system through coordinated technology, data, people and processes. Its value depends on the redesigned workflow being used.",
            "Dashboards expose discrepancies but cannot reconcile definitions or assign responsibility for the transactions underneath.",
        ],
        "lens": "Information system · technology, data, people and process",
    },
    {
        "scene": "Chris shows you four requests: reliable cloud and identity services; a standard order-processing application; a proprietary customer-service offer; and a cleaned product/customer database.",
        "prompt": "How would you organise these requests for a portfolio discussion?",
        "options": [
            "Rank all four by purchase price alone.",
            "Separate infrastructure, operational applications, strategic applications and data assets.",
            "Put them in one digital-transformation budget.",
        ],
        "feedback": [
            "Price alone misses differences in shared foundation, operational reliability, strategic distinctiveness and data quality.",
            "This first lens makes the varied assets visible. Each has a different value logic and therefore a different managerial priority.",
            "One budget can fund them, but it hides why a shared platform, a routine transaction system, a distinctive offer and data need different attention.",
        ],
        "lens": "Tiwana · infrastructure, operational applications, strategic applications, data",
    },
    {
        "scene": "Three proposals now compete for attention: an engineer’s simulator, a technician knowledge network, and an ERP purchasing workflow.",
        "prompt": "Chris wants experimentation and more precise engineering decisions. Which proposal would you pilot first?",
        "options": [
            "Engineer’s simulator · function IT",
            "Technician knowledge network · network IT",
            "ERP purchasing workflow · enterprise IT",
        ],
        "feedback": [
            "The simulator is function IT: it helps an individual try alternatives and make a more precise task decision. It still needs the right skills and task design.",
            "The knowledge network is network IT: it lets technicians find one another and share emerging solutions. That is useful, but it addresses a different capability.",
            "The ERP workflow is enterprise IT: it standardises and coordinates purchasing across roles. That is useful, but it is not the most direct experiment for engineering precision.",
        ],
        "lens": "McAfee · function, network and enterprise IT are different capabilities",
    },
    {
        "scene": "Chris likes all three proposals. The simulator has few trained users; technicians do not share lessons; ERP teams use conflicting product codes and bypass approvals.",
        "prompt": "Which implementation instruction would you give Chris?",
        "options": [
            "Provide the tools and let use emerge on its own.",
            "Match each tool to its complement: skill and task design; participation norms; redesigned process, data and decision rights.",
            "Mandate identical usage targets for all three tools.",
        ],
        "feedback": [
            "Access does not automatically create capability. Each technology encounters a different obstacle to productive use.",
            "Function IT needs proficient users and a suitable task; network IT needs voluntary contribution and trust; enterprise IT needs coordinated workflow, common data and accountable authority.",
            "A single mandate misses the difference between experimentation, shared knowledge and cross-functional standardisation.",
        ],
        "lens": "McAfee · complements determine whether capability becomes organisational value",
    },
    {
        "scene": "Chris asks for your recommendation. The budget will not support everything at once, and an approved purchase is only the beginning.",
        "prompt": "Which management brief would you take to the investment meeting?",
        "options": [
            "Approve the largest package, announce a launch date and expect returns.",
            "Choose the business capability, build its complements, assign responsibility for adoption and value, then review outcomes.",
            "Wait until a rival demonstrates a proven product and copy its configuration.",
        ],
        "feedback": [
            "A purchase and a launch date do not show that work changed or that the expected value was realised.",
            "Use Capability–Complements–Responsibility (CCR): choose what the system should enable, change what surrounds it, and own the results through selection, adoption and exploitation.",
            "Imitation may reduce technical uncertainty, but copying a product cannot copy another firm’s routines, data, relationships or execution.",
        ],
        "lens": "CCR · capability, complements, responsibility",
    },
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def select_stage(stage: int) -> None:
    st.session_state.ism_stage = stage
    st.rerun()


def render_session_01() -> None:
    st.session_state.setdefault("ism_stage", 0)
    stage = st.session_state.ism_stage
    st.markdown('<div class="hero"><div class="eyebrow">SESSION 01 · INTERACTIVE TUTORIAL</div><h1>Vandelay: manage the IT race</h1><p>Take the role of a manager advising Chris Burns. Make six decisions, inspect their implications, and revise your choices.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="notice">The scenario brings the 2004 and 2026 Vandelay conversations together. The management problem spans ERP, infrastructure, data, field work and newer tools.</div>', unsafe_allow_html=True)
    st.progress(stage / 6, text=f"{STAGES[stage]} · {stage + 1} of 7")

    if stage < 6:
        item = DECISIONS[stage]
        with st.container(border=True):
            st.markdown(f'<div class="stage">Decision {stage+1:02d} / 06 · {esc(item["lens"])}</div><div class="prompt">{esc(item["prompt"])}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="case">{esc(item["scene"])}</div>', unsafe_allow_html=True)
            selection = st.radio("Your call", item["options"], index=None, key=f"ism_choice_{stage}")
            if selection is not None:
                index = item["options"].index(selection)
                st.markdown(f'<div class="debrief"><strong>What this choice sets in motion</strong><br>{esc(item["feedback"][index])}</div>', unsafe_allow_html=True)
                st.caption("Select another option to compare its implications.")
        prev, spacer, nxt = st.columns([1, 3, 1])
        with prev:
            if stage and st.button("← Previous", use_container_width=True):
                select_stage(stage - 1)
        with nxt:
            if st.button("Continue →" if stage < 5 else "Your configuration →", type="primary", disabled=selection is None, use_container_width=True):
                select_stage(stage + 1)
    else:
        render_configuration()

    with st.expander("Concept map and reading trail"):
        st.markdown("""
| Lens | Management question | Reading |
|---|---|---|
| Red Queen | Why can IT investment fail to create lasting advantage? | Amrit Tiwana, *IT Strategy for Non-IT Managers*, introductory chapter |
| Information system | What must connect for a purchase to change performance? | Session 1 course deck; *A Conversation About Information Technology* (2004 and 2026 edition) |
| Portfolio | Which assets and managerial imperatives differ? | Tiwana, introductory chapter |
| Three worlds | What capability does the technology create, and which complements make it work? | Andrew McAfee, *Mastering the Three Worlds of Information Technology* |
| CCR | Who selects, adopts and exploits a business capability? | Session 1 course framework |
""")
        st.caption("This tutorial paraphrases the assigned readings. Consult the course copies for the full arguments and examples.")


def render_configuration() -> None:
    if any(st.session_state.get(f"ism_choice_{i}") is None for i in range(6)):
        select_stage(0)
    with st.container(border=True):
        st.markdown('<div class="stage">Management debrief</div><div class="prompt">Your Configuration</div>', unsafe_allow_html=True)
        for i, item in enumerate(DECISIONS):
            choice = st.session_state[f"ism_choice_{i}"]
            idx = item["options"].index(choice)
            st.markdown(f"**{i+1}. {STAGES[i]}**  ")
            st.write(choice)
            st.caption(item["feedback"][idx])
        portfolio = st.session_state.ism_choice_2
        capability = st.session_state.ism_choice_3
        complements = st.session_state.ism_choice_4
        synthesis = st.session_state.ism_choice_5
        sentences = [
            "You prioritised engineering experimentation through function IT." if capability.startswith("Engineer") else
            "You prioritised shared field knowledge through network IT." if capability.startswith("Technician") else
            "You prioritised coordinated purchasing through enterprise IT."
        ]
        sentences.append("Your portfolio view distinguishes assets by their management needs." if portfolio.startswith("Separate") else "Revisit how infrastructure, applications and data demand different management decisions.")
        sentences.append("Your implementation plan matches complements to each technology." if complements.startswith("Match") else "Revisit the skills, participation norms and process changes each tool needs.")
        sentences.append("Your brief assigns responsibility for realised value." if synthesis.startswith("Choose") else "Revisit who owns adoption and realised value after purchase.")
        sentences.append("Try another option and compare the implications.")
        debrief = " ".join(sentences)
        assert len(debrief.split()) <= 50
        st.markdown(f'<div class="debrief"><strong>Debrief</strong><br>{esc(debrief)}</div>', unsafe_allow_html=True)
    a, b, c = st.columns([1.2, 1.2, 2])
    with a:
        if st.button("← Revise a decision", use_container_width=True):
            select_stage(5)
    with b:
        if st.button("Start again", use_container_width=True):
            for i in range(6):
                st.session_state.pop(f"ism_choice_{i}", None)
            select_stage(0)
