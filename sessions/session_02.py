"""Session 2: source-grounded concept revision. Import render_session_02, or run with streamlit run session_02.py. Requires streamlit>=1.32. No external APIs or data files."""
import html
import streamlit as st

SESSION = 2
PREFIX = 'ism_s2'
STAGE_KEY = 'ism_s2_stage'
ANSWER_KEY = 'ism_s2_answers'
TITLE = 'IT strategy: possibilities and choices'
INTRO = ('Use the Trifecta, strategic positioning and synchronization to review Vandelay’s better-pump and uptime '
 'alternatives.')
SUMMARY_TITLE = 'Your Strategic Configuration'
TAKEAWAYS = ['The Trifecta creates possibilities; managers choose the target customers and promise.',
 'Offering, purchase and delivery can change independently.',
 'Strategic aspiration specifies whom to serve and how to compete.',
 'Organizational and IS choices must jointly support the promise and evolve together.',
 'Imitation and cannibalization require continuing managerial judgment.']
GLOSSARY = {'Digitization': 'Conversion of a previously physical offering or activity into electronic form.',
 'Infusion': 'Software becomes part of a product, service or activity.',
 'Ubiquity': 'Cheap and fast Internet connectivity is widely available.',
 'Strategic aspiration': 'The combination of target scope and basis of competition.',
 'Synchronization': 'Continuous adaptation of operational and IT strategy toward strategic aspiration.',
 'Cannibalization': 'A new offer reduces demand or revenue for an existing offer.'}
READING = ('Primary sources: Session 2 teaching deck and Amrit Tiwana, IT Strategy for Non-IT Managers, Chapter 1. The '
 'deck adds the strategy triangle and competitive response discussion.')
DECISIONS = [{'block': 'The Trifecta',
  'title': 'Three drivers',
  'concept': 'Digitization converts a previously physical offering or activity into electronic form. '
             'Infusion embeds software. Ubiquity makes cheap, fast connectivity widely available.',
  'scene': 'A pump has electronic service records, embedded diagnostics and a remote connection.',
  'prompt': 'Which mapping separates the drivers correctly?',
  'options': ['Records: digitization; diagnostics: infusion; connection: ubiquity',
              'All three mean digitization',
              'Records: ubiquity; connection: infusion'],
  'feedback': ['Each driver has a distinct role, although they often work together.',
               'Electronic records, embedded behavior and connectivity are related but distinct.',
               'Ubiquity concerns connectivity; infusion concerns software embedded in an offering or '
               'activity.'],
  'key': 0,
  'source': 'Session 2, slides 6–7, 10–13; Tiwana, Chapter 1: The Trifecta.'},
 {'block': 'The digitization cube',
  'title': 'Printed book bought online',
  'concept': 'The offering, purchase process and delivery are three separate dimensions. Each can be '
             'physical or digital.',
  'scene': 'A reader orders a printed book online and receives it by courier.',
  'prompt': 'What is digital here?',
  'options': ['The offering and delivery', 'The purchase process only', 'Every dimension'],
  'feedback': ['The book and courier delivery remain physical.',
               'Online purchase changes one dimension; the printed book and its delivery remain physical.',
               'An online transaction does not digitize the physical book or courier delivery.'],
  'key': 1,
  'source': 'Session 2, slides 8–9; Tiwana, Chapter 1: Digitization.'},
 {'block': 'The digitization cube',
  'title': 'Software and movies',
  'concept': 'An offering can be digital even when its delivery uses a physical carrier.',
  'scene': 'Software once arrived on a disc; the same kind of software can now be downloaded.',
  'prompt': 'Which dimension changes in this comparison?',
  'options': ['The offering changes from physical to digital',
              'Only the target market changes',
              'Delivery changes from physical to digital'],
  'feedback': ['The software content was already digital on the disc.',
               'The described change concerns delivery, regardless of the target market.',
               'Digital content moves from a physical carrier to transmission over a network.'],
  'key': 2,
  'source': 'Session 2, slides 8–9; Tiwana, Chapter 1: Digitization.'},
 {'block': 'The digitization cube',
  'title': 'Streaming a movie',
  'concept': 'A digitized offering follows the economics of information: reproduction and transmission can '
             'have near-zero marginal costs.',
  'scene': 'A customer purchases access online and streams a movie.',
  'prompt': 'How would you classify the three dimensions?',
  'options': ['Digital offering, digital purchase, digital delivery',
              'Physical offering, digital purchase, physical delivery',
              'Digital delivery means the entire business has zero costs'],
  'feedback': ['The content, transaction and transmission are digital in this example.',
               'That describes a physical item ordered online, not streamed content.',
               'Near-zero reproduction costs do not eliminate content creation, infrastructure or other '
               'business costs.'],
  'key': 0,
  'source': 'Session 2, slides 8–9; Tiwana, Chapter 1: Digitization.'},
 {'block': 'The Trifecta',
  'title': 'Infusion and services',
  'concept': 'Infusion can make products more software-like and enable ongoing services. It does not force '
             'every firm to use a service model.',
  'scene': 'The deck discusses Tesla updates and Rolls-Royce engine services.',
  'prompt': 'What is the shared managerial implication?',
  'options': ['Software always removes the physical product',
              'Software can change functions after sale and support an ongoing service promise',
              'Connectivity alone guarantees recurring revenue'],
  'feedback': ['Cars and engines remain physical; software changes their behavior and use.',
               'Updates and ongoing service are possibilities enabled by software infusion. The business '
               'still needs a valuable customer promise.',
               'Recurring revenue requires an offer customers value and the ability to deliver it.'],
  'key': 1,
  'source': 'Session 2, slides 10–11; Tiwana, Chapter 1: Infusion.'},
 {'block': 'Apply the Trifecta',
  'title': 'Two Vandelay offers',
  'concept': 'Technology opens possibilities; strategic choices determine how a firm uses them.',
  'scene': 'Both better pumps and an uptime promise can use records, diagnostics and remote connectivity.',
  'prompt': 'Which conclusion follows?',
  'options': ['Sensors prove uptime is always the best strategy',
              'Better pumps cannot use the Trifecta',
              'Either offer can use the Trifecta, with different purposes'],
  'feedback': ['Sensors make monitoring possible but do not decide whom to serve or what promise to make.',
               'Field records, software controls and connectivity can improve pump performance too.',
               'For better pumps the emphasis is product improvement; for uptime it is early warning and '
               'coordinated intervention.'],
  'key': 2,
  'source': 'Session 2, slides 3, 14; Tiwana, Chapter 1: Confluence of the Trifecta.'},
 {'block': 'Strategic position',
  'title': 'Whom and how',
  'concept': 'Strategic aspiration combines target market scope with a basis of competition: lower cost or '
             'differentiation.',
  'scene': 'The deck places DMart, Asian Paints, OYO budget stays and Fabindia craft range in four teaching '
           'positions.',
  'prompt': 'Which mapping matches the deck?',
  'options': ['DMart: broad low cost; Asian Paints: broad differentiation; OYO budget stays: cost focus; '
              'Fabindia craft range: focused differentiation',
              'Every firm follows differentiation focus',
              'A website makes every firm a broad low-cost competitor'],
  'feedback': ['These are the positions used in the session illustrations, not claims about every business '
               'line.',
               'The examples deliberately distinguish scope and basis of competition.',
               'Digital access does not determine either strategic dimension.'],
  'key': 0,
  'source': 'Session 2, slides 16–17; Tiwana, Chapter 1: Strategic aspiration.'},
 {'block': 'Strategic position',
  'title': 'Aspiration and execution',
  'concept': 'Aspiration identifies the position sought. Business choices explain the customer promise and '
             'how the firm competes in that position.',
  'scene': 'Vandelay considers high availability for plants where downtime is costly.',
  'prompt': 'Which statement describes the position rather than its execution?',
  'options': ['Install telemetry and maintain technician response commitments',
              'Pursue focused differentiation for plants that value high availability',
              'Buy the newest diagnostic package'],
  'feedback': ['These are operational and IS choices needed to deliver the promise.',
               'This specifies the target segment and differentiated value.',
               'A technology purchase alone does not identify the strategic position.'],
  'key': 1,
  'source': 'Session 2, slides 17, 21; Tiwana, Chapter 1: Strategic aspiration; Syncing, Not Alignment.'},
 {'block': 'Make the fit',
  'title': 'Better pump configuration',
  'concept': 'Organizational and IS choices should support the business promise.',
  'scene': 'Vandelay chooses broad differentiation through efficient, longer-lasting pumps.',
  'prompt': 'Which configuration fits the deck?',
  'options': ['Alerts alone, with no engineering feedback',
              'A booking platform for budget rooms',
              'Engineers prioritize performance; design and test data connect to field failures'],
  'feedback': ['Alerts may help, but this configuration omits the product improvement process.',
               'That supports a different business and customer promise.',
               'Engineering priorities and linked evidence support better pump design.'],
  'key': 2,
  'source': 'Session 2, slides 19–21; Tiwana, Chapter 1: Syncing, Not Alignment.'},
 {'block': 'Make the fit',
  'title': 'Uptime configuration',
  'concept': 'An uptime promise needs a response capability, not just observation.',
  'scene': 'Vandelay detects faults remotely, but parts and technicians are unavailable.',
  'prompt': 'What is the main gap?',
  'options': ['Organizational arrangements do not support the IS-enabled promise',
              'It must stop collecting data',
              'Having sensors already completes the strategy'],
  'feedback': ['Monitoring must connect to early intervention, available parts and clear response '
               'responsibilities.',
               'Data remain useful; the response arrangements need attention.',
               'Sensors detect conditions but cannot themselves fulfill service commitments.'],
  'key': 0,
  'source': 'Session 2, slides 19–21; Tiwana, Chapter 1: Syncing, Not Alignment.'},
 {'block': 'Make the fit',
  'title': 'Continuous synchronization',
  'concept': 'Tiwana describes syncing as an ongoing, two-way relationship between operational and IT '
             'strategy, guided by strategic aspiration.',
  'scene': 'Customer requirements change after an uptime service launches.',
  'prompt': 'What should managers do?',
  'options': ['Freeze the original processes and system design',
              'Adapt service processes and IT together as the promise evolves',
              'Let the vendor decide the target customer segment'],
  'feedback': ['A one-time fit can deteriorate as conditions change.',
               'Both strategies evolve; managers continuously repair mismatches while pursuing the chosen '
               'position.',
               'Managers must own the competitive choices, even when vendors support implementation.'],
  'key': 1,
  'source': 'Session 2, slides 19–21, 24–26; Tiwana, Chapter 1: Syncing, Not Alignment.'},
 {'block': 'Competitive response',
  'title': 'Imitation and cannibalization',
  'concept': 'Rivals can copy visible technology. New offers may also reduce revenue from the current '
             'business.',
  'scene': 'Rivals add sensors and contracts; Vandelay’s uptime service may reduce repair jobs.',
  'prompt': 'Which response best follows the session?',
  'options': ['Assume the technology protects the position forever',
              'Judge the service only by lost repair revenue',
              'Review customer value, coordinated delivery and the revenue trade-off'],
  'feedback': ['Imitation can erode advantage; buying sensors provides no permanent protection.',
               'Lost repair revenue is relevant, but so are the ongoing service promise and its economics.',
               'The deck asks managers to consider imitation, execution and cannibalization together, '
               'without assuming one offer must win.'],
  'key': 2,
  'source': 'Session 2, slides 23–26; Tiwana, Chapter 1: Strategic aspiration; Syncing, Not Alignment.'}]

STYLE = """
<style>
.hero {background:#eef5ff;border-left:5px solid #1761aa;padding:18px 22px;border-radius:8px;margin-bottom:18px;color:#143a60}
.hero h1 {font-size:1.9rem;margin:4px 0 8px;color:#143a60}
.eyebrow {font-weight:700;font-size:.82rem;letter-spacing:.06em;color:#1761aa}
.case {background:#eef5ff;color:#143a60;padding:14px;border-radius:8px;margin:12px 0}
.debrief {background:#f0f7ff;color:#143a60;padding:14px;border-left:4px solid #1761aa;border-radius:6px;margin-top:14px}
</style>
"""

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
        st.warning("Some decisions are unfinished. Complete them to view your review.")
        if st.button("Return to first unfinished decision", key=f"{PREFIX}_unfinished"):
            _go(missing[0])
        return
    st.markdown(f"### {SUMMARY_TITLE}")
    st.write("Review the concepts and compare your decisions with the reasoning from the session.")
    revisit = []
    for block in dict.fromkeys(item['block'] for item in DECISIONS):
        with st.expander(block, expanded=False):
            for i, item in enumerate(DECISIONS):
                if item['block'] != block:
                    continue
                idx = item['options'].index(answers[i])
                st.markdown(f"**{item['title']}**")
                st.write(f"Your choice: {answers[i]}")
                st.info(item['feedback'][idx])
                if idx != item['key']:
                    revisit.append(item['title'])
                if st.button("Revisit this decision", key=f"{PREFIX}_review_{i}"):
                    _go(i)
    note = ("Revisit: " + "; ".join(revisit) + ". Compare another option to clarify these distinctions.") if revisit else "Your choices reflect the key distinctions in this session. Review another option to compare its reasoning and reinforce the concepts."
    st.markdown(f'<div class="debrief"><strong>Your revision note</strong><br>{esc(note)}</div>', unsafe_allow_html=True)
    st.markdown("### Concepts to retain")
    for takeaway in TAKEAWAYS:
        st.markdown(f"- {takeaway}")
    left, right = st.columns(2)
    with left:
        if st.button("Review decisions", key=f"{PREFIX}_review_all", use_container_width=True):
            _go(len(DECISIONS)-1)
    with right:
        if st.button("Start again", key=f"{PREFIX}_restart", use_container_width=True):
            _reset()

def _render():
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
        st.progress(stage/count, text=f"Decision {stage+1} of {count} · {item['block']}")
        with st.container(border=True):
            st.markdown(f"### {item['title']}")
            st.markdown(f'<div class="case"><strong>Before you decide</strong><br>{esc(item["concept"])}</div>', unsafe_allow_html=True)
            st.write(item['scene'])
            st.markdown(f"**{item['prompt']}**")
            widget_key = f"{PREFIX}_choice_{stage}"
            stored = st.session_state[ANSWER_KEY].get(stage)
            if widget_key not in st.session_state and stored is not None:
                st.session_state[widget_key] = stored
            choice = st.radio("Your call", item['options'], index=None, key=widget_key)
            if choice is not None:
                st.session_state[ANSWER_KEY][stage] = choice
                idx = item['options'].index(choice)
                st.markdown(f'<div class="debrief"><strong>What your choice means</strong><br>{esc(item["feedback"][idx])}</div>', unsafe_allow_html=True)
                st.caption("There are no marks. Choose another option to compare the reasoning.")
        left, right = st.columns(2)
        with left:
            if st.button("Previous", disabled=stage==0, key=f"{PREFIX}_previous", use_container_width=True):
                _go(stage-1)
        with right:
            if st.button("View summary" if stage==count-1 else "Continue", disabled=choice is None, key=f"{PREFIX}_next", type="primary", use_container_width=True):
                _go(stage+1)
    with st.expander("Concept map and reading trail"):
        st.markdown("""\n| Lens | Question | Course reading |
|---|---|---|
| Trifecta | How do digitization, infusion and ubiquity change business possibilities? | Tiwana, Chapter 1; Session 2 deck |
| Digitization cube | What changes in the offering, purchase process and delivery? | Tiwana, Chapter 1, Digitization; Session 2 deck |
| Strategic aspiration | Whom will the firm serve, and how will it compete? | Tiwana, Chapter 1, Strategic Aspiration; Session 2 deck |
| Strategy triangle and synchronization | Do organizational and IS choices support the customer promise as conditions change? | Session 2 strategy triangle; Tiwana, Chapter 1, Syncing, Not Alignment |
| Competitive response | How might imitation and self-disruption affect the chosen position? | Session 2 competitive response discussion; Tiwana, Chapter 1 |\n""")
        st.markdown("**Concept reminders**")
        for term, definition in GLOSSARY.items():
            st.markdown(f"**{term}:** {definition}")
        st.caption("The tutorial paraphrases the assigned readings; consult the course copies for the full arguments.")

def render_session_02():
    _render()

if __name__ == "__main__":
    st.set_page_config(page_title="ISM LAB · Session 2", page_icon="📘", layout="wide")
    render_session_02()
