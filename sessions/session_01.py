"""Session 1: applied concept revision across varied business contexts."""
from __future__ import annotations

import html
import streamlit as st

# Each decision asks students to apply a distinction across varied business contexts.
DECISIONS = [
    {
        "block": "The management problem",
        "title": "Parity without advantage",
        "concept": "The Red Queen race distinguishes investment needed to keep pace from investment that creates a distinctive business benefit.",
        "scene": "A retailer introduces next-day delivery. Its sales stay flat, but competitors also introduce next-day delivery and customers stop accepting slower service.",
        "prompt": "What is the most defensible interpretation of the retailer’s investment?",
        "options": [
            "It may have protected competitive parity, even though it did not increase sales.",
            "Flat sales show that the investment created no business value.",
            "Because competitors copied it, withdrawing the service would improve its competitive position."
        ],
        "feedback": [
            "Customers’ expectations changed. Maintaining sales may reflect avoided losses; this does not prove a lasting advantage, and the investment’s costs still need assessment.",
            "Flat sales alone cannot reveal what would have happened without the service. Avoiding customer losses can be valuable even when sales do not grow.",
            "Imitation removes distinctiveness, but can make the service a competitive necessity. Withdrawal could leave the retailer behind."
        ],
        "key": 0
    },
    {
        "block": "The management problem",
        "title": "Accurate information, unchanged outcome",
        "concept": "An information system produces outcomes through technology, data, people and processes working together.",
        "scene": "A hospital’s dashboard correctly identifies discharge-ready patients. Beds remain occupied because only one senior doctor can approve discharge and approvals happen once each evening.",
        "prompt": "Which intervention best addresses the reason the dashboard has not freed beds sooner?",
        "options": [
            "Increase the frequency of dashboard updates so staff see readiness sooner.",
            "Agree on safe approval roles and timings, and connect dashboard alerts to that workflow.",
            "Measure dashboard viewing rates and ask every ward to achieve full usage."
        ],
        "feedback": [
            "The information is already accurate. Faster updates do not remove the approval bottleneck.",
            "The bottleneck lies in how information leads to action. Appropriate approval arrangements connect the dashboard’s information to timely discharge.",
            "Viewing rates measure use, but staff can view the dashboard without being able to act. Adoption measures must connect to the workflow and outcome."
        ],
        "key": 1
    },
    {
        "block": "Criterion 1 · the IT portfolio",
        "title": "A database is not the customer data",
        "concept": "Infrastructure includes shared storage and data-management services; data are the business records managed through them.",
        "scene": "A bank proposes a shared database service for several applications and a separate project to reconcile conflicting customer records.",
        "prompt": "Which classification best identifies the different management needs?",
        "options": [
            "Both are data investments because both involve a database.",
            "The database service is an application; reconciling records is infrastructure maintenance.",
            "The shared database service is infrastructure; reconciling customer records improves the data asset."
        ],
        "feedback": [
            "The shared technical service and the meaning of the records are different assets. Their proximity does not make them the same category.",
            "A common database service supports applications. Reconciling customer identities addresses record quality rather than the technical foundation.",
            "The service needs reliability and support; customer records need consistent definitions, quality and ownership. These require coordinated but different decisions."
        ],
        "key": 2
    },
    {
        "block": "Criterion 1 · the IT portfolio",
        "title": "When is an application strategic?",
        "concept": "An application’s strategic role depends on the distinctive value it supports, rather than whether it faces customers or uses new technology.",
        "scene": "Two logistics firms buy the same tracking software. One provides standard parcel updates; the other combines it with proprietary delivery history and coordinated recovery routines to serve customers with costly delivery failures.",
        "prompt": "What is the strongest basis for treating the second use as potentially strategic?",
        "options": [
            "It supports a distinctive customer benefit through data and coordinated work, although rivals may imitate it.",
            "It is customer-facing, so it must be strategic while internal systems must be operational.",
            "Its software licence is identical to the rival’s, so neither use can contribute to differentiation."
        ],
        "feedback": [
            "The differentiated use comes from how the application, data and routines deliver value together. The advantage still needs continued improvement.",
            "Customer-facing applications can support routine transactions and competitive parity. Being external does not establish differentiation.",
            "Common software does not require identical business use. Firms can combine it with different data, routines and customer promises."
        ],
        "key": 0
    },
    {
        "block": "Criterion 1 · the IT portfolio",
        "title": "More records, less trust",
        "concept": "A data asset becomes useful through shared meaning, quality, ownership and its contribution to a business decision.",
        "scene": "A retailer has years of purchase records, but its website and stores assign different IDs to the same customers. Managers want to identify customers whose purchases are declining.",
        "prompt": "Which action most directly improves the basis for that decision?",
        "options": [
            "Add more years of records before resolving customer identity.",
            "Agree on customer identity rules and ownership, reconcile records, and check whether the combined history supports the decision.",
            "Create separate store and website dashboards so each team can use its own definition."
        ],
        "feedback": [
            "More records can magnify inconsistent identities. Volume does not repair the meaning of the data.",
            "Reliable customer histories require knowing which records belong together. Ownership and a decision-focused check help make the combined data usable.",
            "Separate dashboards may be useful locally, but preserve the inconsistency that prevents a reliable cross-channel customer view."
        ],
        "key": 1
    },
    {
        "block": "Criterion 1 · the IT portfolio",
        "title": "One budget, different imperatives",
        "concept": "Portfolio categories need different managerial priorities: shared reliability, dependable operations, differentiated value and trusted data.",
        "scene": "A manufacturer reviews network recovery, payroll automation, a distinctive maintenance service and inconsistent equipment records. The CFO proposes one success measure: the percentage of employees using each investment.",
        "prompt": "What is the strongest objection to this measure?",
        "options": [
            "Usage should be replaced by the purchase price of each investment.",
            "Only the maintenance service needs evaluation because the other assets cannot create value.",
            "Usage alone misses the different results and standards each asset must deliver."
        ],
        "feedback": [
            "Purchase price is a cost, not evidence of results. Neither price nor usage alone evaluates the portfolio.",
            "Infrastructure, routine applications and data can enable essential value. They require evaluation even when their role is not differentiation.",
            "The network needs recovery standards, payroll needs reliable transactions, the service needs customer value, and records need quality. One usage measure misses these differences."
        ],
        "key": 2
    },
    {
        "block": "Criterion 2 · three worlds",
        "title": "Classify the use, not the label",
        "concept": "Function IT supports a discrete task; classification depends on how technology changes work, not on its product name.",
        "scene": "An analyst uses an AI assistant to compare demand scenarios and draft a recommendation. The analyst checks the output; no other team’s workflow or approvals change.",
        "prompt": "Which classification and management response best fit this use?",
        "options": [
            "Function IT: develop the analyst’s skill in checking assumptions and using the output.",
            "Enterprise IT: impose a company-wide process because the assistant uses advanced AI.",
            "Network IT: encourage contributions because the assistant interacts conversationally."
        ],
        "feedback": [
            "The assistant supports an individual analytical task. Skill and appropriate use of its output are the relevant complements.",
            "Advanced technology does not automatically define an enterprise process. The described use does not coordinate a prescribed cross-team workflow.",
            "A conversational interface does not itself connect people to exchange knowledge. The work described is an individual task."
        ],
        "key": 0
    },
    {
        "block": "Criterion 2 · three worlds",
        "title": "Participation or prescription?",
        "concept": "Network IT enables flexible knowledge exchange; useful contributions, participation and shared norms help realise its value.",
        "scene": "A consulting firm launches a community for unusual client problems. Consultants read posts but rarely share solutions. A manager proposes requiring every question to follow the same approval chain as an expense claim.",
        "prompt": "Which response best fits the intended capability?",
        "options": [
            "Require the approval chain so all knowledge exchange becomes a standard transaction.",
            "Encourage useful contributions, recognition and sharing norms while preserving flexible discussion.",
            "Give every consultant a personal analysis tool so community participation becomes unnecessary."
        ],
        "feedback": [
            "Controls may be appropriate for sensitive information, but an expense-style approval chain can obstruct the flexible exchange the community is intended to enable.",
            "The gap is participation and useful exchange. Norms and recognition support network capability without prescribing every interaction.",
            "Individual tools can support personal work, but do not address how colleagues discover and reuse each other’s knowledge."
        ],
        "key": 1
    },
    {
        "block": "Criterion 2 · three worlds",
        "title": "The same assistant, a different world",
        "concept": "Enterprise IT defines and coordinates a process across teams or partners; roles, data and decision rights must fit that process.",
        "scene": "A service assistant previously drafted repair notes for technicians. It will now check inventory, authorize parts purchases and schedule supplier deliveries automatically.",
        "prompt": "What is the most consequential change in its management requirements?",
        "options": [
            "The main requirement remains better drafting skills because the software is still called an assistant.",
            "Participation norms become sufficient because several parties are now involved.",
            "The use now coordinates an enterprise workflow, requiring agreed permissions, approvals, data and accountability."
        ],
        "feedback": [
            "The assistant now acts across a transaction process. Drafting skills alone do not determine who may commit money or schedule suppliers.",
            "Involving several parties does not automatically make the use network IT. These actions follow a prescribed workflow and require decision rights.",
            "The changed use moves beyond an individual task to coordinated business actions. Managers must define authority, exceptions and responsibility across the workflow."
        ],
        "key": 2
    },
    {
        "block": "CCR · making value real",
        "title": "Capability without its complement",
        "concept": "Capability is what technology enables; complements are changes in skills and work arrangements that help turn it into performance.",
        "scene": "A design simulator accurately compares alternatives. Engineers know how to run it, but design approvals still depend on the first prototype and reviewers never consider simulation results.",
        "prompt": "Which diagnosis and response best apply the capability–complement distinction?",
        "options": [
            "Testing alternatives is the capability; changing review routines to evaluate that evidence is the missing complement.",
            "The simulator lacks capability because its results have not changed design decisions; buy a more accurate version.",
            "Training is always the complement, so repeat software training even though engineers can already operate it."
        ],
        "feedback": [
            "The technical capability exists. Review routines must make its evidence usable in decisions, alongside engineering judgement and appropriate checks.",
            "Lack of realised benefit does not establish lack of technical capability. The scenario identifies a disconnect between results and approval routines.",
            "Training can be a complement, but the stated gap is how reviewers use evidence. Complements should address the actual barrier."
        ],
        "key": 0
    },
    {
        "block": "CCR · making value real",
        "title": "Adoption is not the final result",
        "concept": "Managerial responsibility covers selection, adoption and exploitation: using and improving the system to realise business value.",
        "scene": "A CRM is live and every salesperson uses it. Customer retention has not improved because follow-up tasks are recorded but responsibility for resolving complaints remains unclear.",
        "prompt": "What should the business manager do next?",
        "options": [
            "Declare the initiative complete because installation and full usage demonstrate realised value.",
            "Clarify complaint ownership, connect CRM tasks to resolution, and monitor retention and service outcomes.",
            "Ask IT to improve system availability before changing the sales and service process."
        ],
        "feedback": [
            "Installation and usage are milestones. They do not demonstrate that the intended customer outcome has improved.",
            "Responsibility continues into exploitation. The manager must connect use to effective action, measure results and improve the arrangements.",
            "Availability matters, but no availability failure is described. The identified gap concerns ownership and follow-through in the business process."
        ],
        "key": 1
    }
]

# Concept-specific nudges support another attempt.
RETRY_HINTS = [
    "Separate growth from avoiding a loss of competitiveness; ask what might have happened without the investment.",
    "Trace the path from information to action and identify where that path stops.",
    "Distinguish the shared technical service from the business meaning and quality of its contents.",
    "Ask where the distinctive customer benefit comes from, beyond the software licence.",
    "Consider whether records can be combined into a reliable history of the same customer.",
    "Match each portfolio asset to the result it enables and the standard it must meet.",
    "Look at the task and workflow being changed, rather than the sophistication of the technology.",
    "Ask whether the intended work is flexible knowledge exchange or a prescribed transaction.",
    "Follow the assistant’s new actions and ask who can authorize them across organizations.",
    "Separate what the simulator can do from whether the approval process uses its evidence.",
    "Distinguish installation, use and the business outcome; identify the barrier after adoption."
]

STYLE = """
<style>
.hero {background:#eef5ff;border-left:5px solid #1761aa;padding:18px 22px;border-radius:8px;margin-bottom:18px;color:#143a60}
.hero h1 {font-size:1.9rem;margin:4px 0 8px;color:#143a60}
.eyebrow {font-weight:700;font-size:.82rem;letter-spacing:.06em;color:#1761aa}
.case {background:#eef5ff;color:#143a60;padding:14px;border-radius:8px;margin:12px 0}
.debrief {background:#f0f7ff;color:#143a60;padding:14px;border-left:4px solid #1761aa;border-radius:6px;margin-top:14px}
</style>
"""


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def go_to(stage: int) -> None:
    st.session_state.ism_stage = stage
    st.rerun()


def render_session_01() -> None:
    st.markdown(STYLE, unsafe_allow_html=True)
    count = len(DECISIONS)
    st.session_state.setdefault("ism_stage", 0)
    # Widget keys for off-screen questions are pruned by Streamlit. Keep the
    # student's selections in a separate, non-widget session-state dictionary.
    st.session_state.setdefault("ism_s1_answers", {})
    stage = min(st.session_state.ism_stage, count)
    st.markdown('<div class="hero"><div class="eyebrow">SESSION 01 · CONCEPT REVISION</div><h1>Information systems: concepts in practice</h1><p>Apply the portfolio, three worlds and CCR lenses to management situations. Consider what changes in the work, why an answer fits and what each alternative misses.</p></div>', unsafe_allow_html=True)
    if stage < count:
        item = DECISIONS[stage]
        st.progress(stage / count, text=f"Decision {stage + 1} of {count} · {item['block']}")
        with st.container(border=True):
            st.markdown(f'<div class="stage">{esc(item["block"])} · {esc(item["title"])}</div><div class="case"><strong>Before you decide</strong><br>{esc(item["concept"])}</div><div class="compact">MANAGEMENT SITUATION</div><p>{esc(item["scene"])}</p><div class="prompt">{esc(item["prompt"])}</div>', unsafe_allow_html=True)
            widget_key = f"ism_s1_choice_{stage}"
            if widget_key not in st.session_state and stage in st.session_state["ism_s1_answers"]:
                st.session_state[widget_key] = st.session_state["ism_s1_answers"][stage]
            selection = st.radio("Your call", item["options"], index=None, key=widget_key)
            is_correct = False
            if selection is not None:
                idx = item["options"].index(selection)
                is_correct = idx == item["key"]
                if is_correct:
                    st.session_state["ism_s1_answers"][stage] = selection
                    st.success("Correct — " + item["feedback"][idx])
                    st.caption("You can now continue. There are no marks.")
                else:
                    st.session_state["ism_s1_answers"].pop(stage, None)
                    st.warning("Not quite — " + item["feedback"][idx])
                    st.info("Hint: " + RETRY_HINTS[stage])
                    st.caption("Try again: select another answer above.")
        left, _, right = st.columns([1.2, 3, 1.5])
        with left:
            if stage and st.button("← Previous", use_container_width=True):
                go_to(stage - 1)
        with right:
            label = "View summary →" if stage == count - 1 else "Continue →"
            if st.button(label, type="primary", disabled=not is_correct, use_container_width=True):
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
        st.caption("The revision questions paraphrase the assigned readings; consult the course copies for the full arguments.")


def render_summary() -> None:
    count = len(DECISIONS)
    answers = st.session_state.get("ism_s1_answers", {})
    unfinished = [i for i, item in enumerate(DECISIONS)
                  if answers.get(i) != item["options"][item["key"]]]
    if unfinished:
        st.warning("Some decisions are unfinished. Return to them before viewing your configuration.")
        if st.button("Return to first unfinished decision"):
            go_to(unfinished[0])
        return
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
        picks = [DECISIONS[i]["options"].index(answers[i]) for i in range(count)]
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
        parts = ["You distinguished competitive parity from lasting advantage." if picks[0] == DECISIONS[0]["key"] else "Revisit competitive parity and the value of keeping pace.",
                 "You connected technology with people, process and data." if picks[1] == DECISIONS[1]["key"] else "Revisit what makes a software purchase a working information system.",
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
            st.session_state["ism_s1_answers"] = {}
            for i in range(count):
                st.session_state.pop(f"ism_s1_choice_{i}", None)
            go_to(0)
