"""Session 06: Big Data Analytics concept revision, applied to business decisions."""
from __future__ import annotations

import html
import streamlit as st

SESSION = 6
PREFIX = "ism_s6"
STAGE_KEY = "ism_s6_stage"
ANSWER_KEY = "ism_s6_answers"
TITLE = "Big Data Analytics"
INTRO = "Apply Big Data concepts to MetroTrans and other business decisions. Focus on the problem, relevant capabilities, action and value."
READING = "Assigned sources: Session 06 Big Data deck; Hugh J. Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications, Communications of the Association for Information Systems, 34, Article 65."
DECISIONS = [
  {
    "block": "The managerial problem",
    "title": "Lots of data, too little action",
    "concept": "Big Data matters when data volume, velocity or variety obstruct useful decisions.",
    "scene": "MetroTrans receives readings from 12,000 trucks. Maintenance teams still learn about overheating after a breakdown. Its director wants to buy more storage.",
    "prompt": "Which question should guide the investment?",
    "options": [
      "How much storage could a vendor supply?",
      "Which decision must happen sooner, and what information would make it possible?",
      "How many dashboards can the IT team build?"
    ],
    "key": 1,
    "feedback": [
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "Start with the decision and the cost of delay; storage is only one potential enabler.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "The 3Vs",
    "title": "When tomorrow is too late",
    "concept": "Volume is how much data exists; velocity concerns how quickly it arrives and needs attention; variety concerns differences in data forms.",
    "scene": "An engine sends readings every few seconds. A dangerous temperature spike should be detected before the truck fails.",
    "prompt": "Which challenge makes a daily report inadequate?",
    "options": [
      "Velocity and the need for a timely response.",
      "Variety, because trucks have different colours.",
      "Volume alone, because many records use space."
    ],
    "key": 0,
    "feedback": [
      "Speed of arrival and urgency of action are the crucial constraints.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "The 3Vs",
    "title": "Records that do not agree",
    "concept": "Combining different data sources requires shared identifiers, definitions and time references.",
    "scene": "MetroTrans has GPS histories, repair notes and fuel-card purchases. Each system uses a different truck identifier.",
    "prompt": "What should the managers fix first?",
    "options": [
      "Discard the repair notes because they are text.",
      "Link the sources to a trusted truck identity and common event times.",
      "Purchase additional processors before matching records."
    ],
    "key": 1,
    "feedback": [
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "The different sources cannot inform one truck's situation reliably until they are integrated.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Data to business value",
    "title": "An accurate alert with no owner",
    "concept": "Collection, integration, analysis, visualisation and managerial action are distinct stages.",
    "scene": "An analytics dashboard identifies trucks at risk of breakdown, but no person is responsible for arranging an inspection.",
    "prompt": "Which change most directly creates value?",
    "options": [
      "Add more charts.",
      "Collect readings twice as often.",
      "Assign an owner and workflow to act on high-risk alerts."
    ],
    "key": 2,
    "feedback": [
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "Insights need a responsible team and a process that turns them into preventive maintenance."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Distributed processing",
    "title": "Divide, work, combine",
    "concept": "Independent tasks can run in parallel, and their partial results can then be combined—the basic intuition behind MapReduce.",
    "scene": "Five teams each total ten numbers from a list of 50. The class then combines the five subtotals.",
    "prompt": "What does this exercise demonstrate?",
    "options": [
      "Dividing work, computing partial results and combining them.",
      "Duplicating all calculations five times.",
      "Ensuring data is correct merely by adding more people."
    ],
    "key": 0,
    "feedback": [
      "Parallel processing can reduce processing time, but dividing and merging the work also takes effort.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Distributed processing",
    "title": "More workers but slower reports",
    "concept": "Scaling out has coordination costs; performance depends on work divided and results merged.",
    "scene": "MetroTrans increases its processing workers from 8 to 30. Reports become slower because data transfer and merging take longer.",
    "prompt": "How should the manager respond?",
    "options": [
      "Keep increasing worker count because more is always faster.",
      "Evaluate total completion time and find an appropriate number of workers.",
      "Conclude that distributed computing never works."
    ],
    "key": 1,
    "feedback": [
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "Coordination overhead may exceed the time saved by parallel work.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Distributed storage",
    "title": "A computer fails",
    "concept": "Distributing records and maintaining usable copies can protect service continuity when a machine fails.",
    "scene": "One computer storing truck service histories stops working. Equivalent copies are accessible on other computers.",
    "prompt": "What business outcome do the copies support?",
    "options": [
      "Repairs can continue with less disruption.",
      "The company no longer needs backups or access controls.",
      "Data quality automatically improves."
    ],
    "key": 0,
    "feedback": [
      "Copies improve availability, but they do not remove the need for governance and recovery planning.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Technology choices",
    "title": "The vendor's shopping list",
    "concept": "Hadoop, distributed file systems, Spark, Kafka, cloud storage and dashboards play different roles; the business requirement comes first.",
    "scene": "A vendor recommends installing Hadoop, Spark and Kafka for every logistics firm, including a small operator with only monthly reports.",
    "prompt": "What is the strongest managerial response?",
    "options": [
      "The same stack is mandatory whenever data is digital.",
      "Identify the workload, response needs, simpler alternatives and full cost first.",
      "Choose the tool with the most technical features."
    ],
    "key": 1,
    "feedback": [
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "Select needed capabilities rather than adopting a fashionable technology stack.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Batch versus streaming",
    "title": "Fuel trends and overheating",
    "concept": "Batch processing fits scheduled analysis; streaming fits decisions that lose value when delayed.",
    "scene": "MetroTrans reviews fleet fuel efficiency every week but must alert a driver immediately when engine temperature becomes dangerous.",
    "prompt": "Which approach fits best?",
    "options": [
      "Batch for the weekly report; timely streaming for the overheating alert.",
      "Stream everything because scheduled reporting is obsolete.",
      "Process both only at the end of the week."
    ],
    "key": 0,
    "feedback": [
      "Processing frequency should reflect business urgency and the cost of delay.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Analytics and visualisation",
    "title": "Predictions nobody can use",
    "concept": "Analysis finds patterns or predicts outcomes; visualisation helps decision-makers understand priorities.",
    "scene": "A model predicts which trucks may fail. The manager receives 12,000 unranked risk scores without routes, locations or recommended action.",
    "prompt": "What is the most useful next step?",
    "options": [
      "Store the same predictions in more places.",
      "Present a prioritised view of high-risk trucks with context and follow-up actions.",
      "Remove managers from the process entirely."
    ],
    "key": 1,
    "feedback": [
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "Translate model outputs into a useful view and actionable priorities.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Business outcomes",
    "title": "A dashboard is not the benefit",
    "concept": "Value must be established through improved decisions and measured operating outcomes.",
    "scene": "MetroTrans celebrates its new data platform and rising dashboard visits, but cannot say whether breakdowns or late deliveries declined.",
    "prompt": "Which evidence should it collect?",
    "options": [
      "Only number of dashboards viewed.",
      "Only the volume of data processed.",
      "Baseline and follow-up breakdowns, repair costs, on-time deliveries and actions taken."
    ],
    "key": 2,
    "feedback": [
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "Technology activity is not the same as business impact."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Investment decision",
    "title": "When not to use Big Data",
    "concept": "Choose the simplest feasible approach whose incremental benefits justify investment, risks and change effort.",
    "scene": "A smaller operator manages 40 trucks. Its current database handles all records and reporting needs without delay.",
    "prompt": "What should the manager recommend?",
    "options": [
      "Pilot a simple approach and invest further only if business needs justify it.",
      "Copy MetroTrans's full architecture immediately.",
      "Adopt a streaming platform to demonstrate innovation."
    ],
    "key": 0,
    "feedback": [
      "Big Data architecture is a means, not an obligation. Compare it with less complex alternatives.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  },
  {
    "block": "Responsible use",
    "title": "Driver monitoring has consequences",
    "concept": "Combining large datasets raises concerns about privacy, access, fairness and purpose.",
    "scene": "MetroTrans plans to link every driver's personal movements to fuel use, repair records and employee rankings.",
    "prompt": "What is the appropriate first step?",
    "options": [
      "Make all individual profiles public.",
      "Set a legitimate purpose, limited data use, access controls and safeguards.",
      "Collect every personal detail because it may be useful later."
    ],
    "key": 1,
    "feedback": [
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome.",
      "A business case does not remove duties to protect people and govern sensitive information.",
      "This does not directly resolve the business problem. Consider the distinction in the concept above and what changes the decision or outcome."
    ],
    "source": "Watson (2014), Tutorial: Big Data Analytics: Concepts, Technologies, and Applications; Session 06 lecture. Scenarios are illustrative."
  }
]
RETRY_HINTS = [
  "Consider the managerial purpose: Big Data matters when data volume, velocity or variety obstruct useful decisions.",
  "Consider the managerial purpose: Volume is how much data exists; velocity concerns how quickly it arrives and needs attention; variety concerns differences in data forms.",
  "Consider the managerial purpose: Combining different data sources requires shared identifiers, definitions and time references.",
  "Consider the managerial purpose: Collection, integration, analysis, visualisation and managerial action are distinct stages.",
  "Consider the managerial purpose: Independent tasks can run in parallel, and their partial results can then be combined—the basic intuition behind MapReduce.",
  "Consider the managerial purpose: Scaling out has coordination costs; performance depends on work divided and results merged.",
  "Consider the managerial purpose: Distributing records and maintaining usable copies can protect service continuity when a machine fails.",
  "Consider the managerial purpose: Hadoop, distributed file systems, Spark, Kafka, cloud storage and dashboards play different roles; the business requirement comes first.",
  "Consider the managerial purpose: Batch processing fits scheduled analysis; streaming fits decisions that lose value when delayed.",
  "Consider the managerial purpose: Analysis finds patterns or predicts outcomes; visualisation helps decision-makers understand priorities.",
  "Consider the managerial purpose: Value must be established through improved decisions and measured operating outcomes.",
  "Consider the managerial purpose: Choose the simplest feasible approach whose incremental benefits justify investment, risks and change effort.",
  "Consider the managerial purpose: Combining large datasets raises concerns about privacy, access, fairness and purpose."
]
TAKEAWAYS = [
    "Begin with the decision and business problem, not the technology.",
    "Volume, velocity and variety present different managerial challenges.",
    "Combine data sources reliably before expecting useful analytics.",
    "Distributed processing shares work; replication supports continuity, with costs and limitations.",
    "Match batch or streaming to when the business needs an answer.",
    "Data collection, integration, analysis and visualisation create value through operating action.",
    "Compare realised benefits, full cost, privacy risks and simpler alternatives.",
]
GLOSSARY = {
    "Volume": "The amount of data produced or held.",
    "Velocity": "The speed at which data arrives and may need to be processed.",
    "Variety": "Different formats and sources of data.",
    "Data integration": "Connecting sources so records describe the same truck, customer or event.",
    "Distributed processing": "Sharing separate parts of work and combining their results.",
    "Replication": "Keeping usable copies to improve continuity if a machine fails.",
    "Batch": "Processing collected data at an agreed time.",
    "Streaming": "Processing incoming events continuously when delay matters.",
    "Analysis": "Finding patterns, estimates and evidence in data.",
    "Visualisation": "Presenting results so people can understand and act.",
}
CONCEPT_MAP = """
| Concept | Application question | Reading trail |
|---|---|---|
| Big Data and 3Vs | What makes current information processing inadequate? | Watson (2014), sections II–III |
| Analytics and value | Does information produce an effective decision? | Sections IV–VI |
| Distributed computing and storage | What can be split, combined and protected? | Section VII, Hadoop/MapReduce |
| Batch and streaming | How soon does an answer need to arrive? | Section VII, Streaming and CEP |
| Platform selection | Which solution fits the need at reasonable cost? | Section VII, Which Platform Is Best |
| People, governance and privacy | Who acts, and what risks must be governed? | Sections VII–VIII |
"""
STYLE = """<style>
.hero{background:#eef5ff;border-left:5px solid #1761aa;padding:18px 22px;border-radius:8px;margin-bottom:18px;color:#143a60}
.hero h1{font-size:1.9rem;margin:4px 0 8px;color:#143a60}
.eyebrow{font-weight:700;font-size:.82rem;letter-spacing:.06em;color:#1761aa}
.case{background:#eef5ff;color:#143a60;padding:14px;border-radius:8px;margin:12px 0}
.debrief{background:#f0f7ff;color:#143a60;padding:14px;border-left:4px solid #1761aa;border-radius:6px;margin-top:14px}
</style>"""

def esc(value):
    return html.escape(str(value), quote=True)

def _go(stage):
    st.session_state[STAGE_KEY] = stage
    st.rerun()

def _reset():
    st.session_state[ANSWER_KEY] = {}
    for i in range(len(DECISIONS)):
        st.session_state.pop(f"{PREFIX}_choice_{i}", None)
    _go(0)

def render_summary():
    answers = st.session_state[ANSWER_KEY]
    missing = [i for i in range(len(DECISIONS)) if i not in answers]
    if missing:
        st.warning("Some decisions are unfinished. Complete them to view the review.")
        if st.button("Return to first unfinished decision", key=f"{PREFIX}_unfinished"):
            _go(missing[0])
        return
    st.markdown("### Your Big Data Decision Review")
    st.write("Review how your decisions connect to the concepts and reasoning.")
    for block in dict.fromkeys(item["block"] for item in DECISIONS):
        with st.expander(block, expanded=False):
            for i, item in enumerate(DECISIONS):
                if item["block"] != block:
                    continue
                answer = answers[i]
                idx = item["options"].index(answer)
                st.markdown(f"**{item['title']}**")
                st.write("Your choice: " + answer)
                st.info(item["feedback"][idx])
                if st.button("Revisit this decision", key=f"{PREFIX}_revisit_{i}"):
                    _go(i)
    st.markdown('<div class="debrief"><strong>Your revision note</strong><br>Big Data adds value when the organization can combine, understand and act on information at the right time, with measurable results.</div>', unsafe_allow_html=True)
    st.markdown("### Concepts to retain")
    for takeaway in TAKEAWAYS:
        st.markdown("- " + takeaway)
    left, right = st.columns(2)
    with left:
        if st.button("Review decisions", key=f"{PREFIX}_review_all", use_container_width=True):
            _go(len(DECISIONS) - 1)
    with right:
        if st.button("Start again", key=f"{PREFIX}_restart", use_container_width=True):
            _reset()

def render_session_06():
    st.markdown(STYLE, unsafe_allow_html=True)
    st.session_state.setdefault(STAGE_KEY, 0)
    st.session_state.setdefault(ANSWER_KEY, {})
    count = len(DECISIONS)
    stage = max(0, min(int(st.session_state[STAGE_KEY]), count))
    st.markdown(f'<div class="hero"><div class="eyebrow">SESSION {SESSION:02d} · CONCEPT REVISION</div><h1>{esc(TITLE)}</h1><p>{esc(INTRO)}</p></div>', unsafe_allow_html=True)
    if stage == count:
        st.progress(1.0, text=f"{count} of {count} decisions complete · Summary")
        render_summary()
    else:
        item = DECISIONS[stage]
        st.progress(stage / count, text=f"Decision {stage+1} of {count} · {item['block']}")
        with st.container(border=True):
            st.markdown(f"### {item['title']}")
            st.markdown(f'<div class="case"><strong>Before you decide</strong><br>{esc(item["concept"])}</div>', unsafe_allow_html=True)
            st.write(item["scene"])
            st.markdown(f"**{item['prompt']}**")
            widget_key = f"{PREFIX}_choice_{stage}"
            saved = st.session_state[ANSWER_KEY].get(stage)
            if widget_key not in st.session_state and saved is not None:
                st.session_state[widget_key] = saved
            choice = st.radio("Your call", item["options"], index=None, key=widget_key)
            is_correct = False
            if choice is not None:
                idx = item["options"].index(choice)
                is_correct = idx == item["key"]
                if is_correct:
                    st.session_state[ANSWER_KEY][stage] = choice
                    st.success("Correct — " + item["feedback"][idx])
                    st.caption("You can now continue. There are no marks.")
                else:
                    st.session_state[ANSWER_KEY].pop(stage, None)
                    st.warning("Not quite — " + item["feedback"][idx])
                    st.info("Hint: " + RETRY_HINTS[stage])
                    st.caption("Try again: select another answer above.")
        left, right = st.columns(2)
        with left:
            if st.button("Previous", disabled=stage == 0, key=f"{PREFIX}_previous", use_container_width=True):
                _go(stage - 1)
        with right:
            if st.button("View summary" if stage == count - 1 else "Continue", disabled=not is_correct, key=f"{PREFIX}_next", type="primary", use_container_width=True):
                _go(stage + 1)
    with st.expander("Concept map and reading trail"):
        st.caption(READING)
        st.markdown(CONCEPT_MAP)
        if stage < count:
            st.caption("Reading trail: " + DECISIONS[stage]["source"])
        st.markdown("**Concept reminders**")
        for term, definition in GLOSSARY.items():
            st.markdown(f"**{term}:** {definition}")
        st.caption("The business situations are illustrative applications of the assigned concepts.")

if __name__ == "__main__":
    st.set_page_config(page_title="ISM LAB · Session 06", page_icon="📘", layout="wide")
    render_session_06()
