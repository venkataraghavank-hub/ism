"""Session 2: source-grounded concept revision. Import render_session_02, or run with streamlit run session_02.py. Requires streamlit>=1.32. No external APIs or data files."""
import html
import streamlit as st

SESSION = 2
PREFIX = 'ism_s2'
STAGE_KEY = 'ism_s2_stage'
ANSWER_KEY = 'ism_s2_answers'
TITLE = 'IT strategy: possibilities and choices'
INTRO = ('Apply the Trifecta, strategic positioning and synchronization to varied business situations. '
 'Weigh the alternatives and explain what would make the technology useful.')
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
  'title': 'Three changes, three different benefits',
  'concept': 'Digitization converts a previously physical offering or activity into electronic '
             'form. Infusion embeds software. Ubiquity makes cheap, fast connectivity widely '
             'available.',
  'scene': 'A dairy makes three changes: it replaces paper maintenance logs with searchable '
           'electronic records; installs software inside refrigeration units to adjust temperature '
           'automatically; and uses affordable internet connections to let managers monitor units '
           'at different depots. The manager reports only how many units are connected to the '
           'internet.',
  'prompt': 'Why is the number of connected units insufficient to judge the benefits of all three '
            'changes?',
  'options': ['It shows connectivity, but not whether staff can use the electronic records or '
              'whether automatic temperature control works well.',
              'It is sufficient: once a unit is connected, its electronic records and automatic '
              'temperature control must also be working well.',
              'It is insufficient only because the dairy needs to count the number of electronic '
              'records as well.'],
  'feedback': ['Connectivity supports remote monitoring (ubiquity). Searchable electronic records '
               '(digitization) and software-controlled temperature adjustment (infusion) create '
               'different possibilities. Their usefulness must also be checked; counting '
               'connections alone does not establish it.',
               'An internet connection does not guarantee usable records or effective '
               'temperature-control software. These are distinct changes, even when they work '
               'together.',
               'Counting records adds a measure of volume, but does not show whether the records '
               'help staff or whether embedded software improves temperature control. The manager '
               'needs evidence about each change’s contribution.'],
  'key': 0,
  'source': 'Session 2, slides 6–7, 10–13; Tiwana, Chapter 1: The Trifecta. Applied situation is '
            'illustrative.'},
 {'block': 'The digitization cube',
  'title': 'Online purchase, physical bottleneck',
  'concept': 'The offering, purchase process and delivery are three separate dimensions. Each can '
             'be physical or digital.',
  'scene': 'A furniture seller introduces online ordering. Customers still receive assembled '
           'furniture by truck. Online orders are growing, but transport and handling costs per '
           'delivery remain high.',
  'prompt': 'How does the digitization cube help explain why delivery costs remain high?',
  'options': ['The offering becomes digital when customers order online, so delivery costs should '
              'mainly reflect website operations.',
              'Purchasing is digital, while the offering and delivery remain physical; trucks, '
              'handling and delivery routes still affect costs.',
              'Delivery becomes digital when order confirmations and tracking updates reach '
              'customers electronically.'],
  'feedback': ['Online ordering digitizes the purchase process, not the furniture itself. Website '
               'operations do not replace the physical activities required to deliver it.',
               'The three dimensions can change independently. Online ordering may improve '
               'coordination, but assembled furniture still needs physical handling and transport. '
               'Digitizing purchasing alone does not remove those costs.',
               'Order confirmations and tracking updates are digital information about delivery. '
               'The furniture itself still reaches the customer by truck, so delivery of the '
               'offering remains physical.'],
  'key': 1,
  'source': 'Session 2, slides 8–9; Tiwana, Chapter 1: Digitization. Applied situation is '
            'illustrative.'},
 {'block': 'The digitization cube',
  'title': 'A new delivery route',
  'concept': 'An offering can be digital even when its delivery uses a physical carrier.',
  'scene': 'A training firm sells identical course videos through online payment. It replaces '
           'mailed USB drives with downloads. Management credits the change with digitizing the '
           'course content.',
  'prompt': 'Which interpretation is most precise?',
  'options': ['The offering became digital when the USB drive was removed.',
              'Only purchasing changed, because customers now interact with the website.',
              'The content was already digital; delivery changed from a physical carrier to '
              'network transmission.'],
  'feedback': ['Video files on a USB drive were already digital content. The carrier was physical.',
               'Payment was online in both versions. The changed step is how the content reaches '
               'the customer.',
               'An offering can be digital before its delivery becomes digital. Removing the '
               'physical carrier changes delivery, with possible cost and access implications.'],
  'key': 2,
  'source': 'Session 2, slides 8–9; Tiwana, Chapter 1: Digitization. Applied situation is '
            'illustrative.'},
 {'block': 'The digitization cube',
  'title': 'Low reproduction cost, high investment',
  'concept': 'A digitized offering follows the economics of information: reproduction and '
             'transmission can have near-zero marginal costs.',
  'scene': 'An education firm spends heavily producing an online course. Serving one additional '
           'learner has a low incremental distribution cost, but support, platform operation and '
           'content updates remain costly.',
  'prompt': 'What follows from the economics of a digitized offering?',
  'options': ['Low incremental distribution cost can support scale, but profitability still '
              'depends on recovering other costs and attracting paying learners.',
              'Low distribution cost means the course should be priced close to zero regardless of '
              'development costs.',
              'The high initial investment prevents the firm from benefiting from digital '
              'reproduction.'],
  'feedback': ['Reproducing digital content can be inexpensive without making the entire business '
               'inexpensive. Demand, pricing and other costs still determine viability.',
               'Marginal distribution cost alone does not determine a viable price or eliminate '
               'fixed and ongoing costs.',
               'High initial investment and low reproduction cost can coexist. Scale may help '
               'recover the investment, although it does not guarantee profit.'],
  'key': 0,
  'source': 'Session 2, slides 8–9; Tiwana, Chapter 1: Digitization. Applied situation is '
            'illustrative.'},
 {'block': 'The Trifecta',
  'title': 'Software after the sale',
  'concept': 'Infusion can make products more software-like and enable ongoing services. It does '
             'not force every firm to use a service model.',
  'scene': 'A machine maker can improve energy efficiency through software updates after '
           'installation. It is considering a subscription but has not established whether '
           'customers value ongoing updates.',
  'prompt': 'Which strategic conclusion is justified?',
  'options': ['Introduce a subscription immediately because embedded software makes recurring '
              'revenue the appropriate model.',
              'Infusion enables changing functionality after sale; the firm must still choose a '
              'valuable promise and a workable revenue model.',
              'Treat updates only as internal maintenance because the machine remains a physical '
              'product.'],
  'feedback': ['Infusion creates possibilities, but customer value and service economics must '
               'justify the chosen model.',
               'Software can make a physical offering adaptable after sale. That capability does '
               'not determine what customers will pay for or how the firm should charge.',
               'The physical machine can remain the offering while software changes its customer '
               'benefit. Physical form does not prevent ongoing services.'],
  'key': 1,
  'source': 'Session 2, slides 10–11; Tiwana, Chapter 1: Infusion. Applied situation is '
            'illustrative.'},
 {'block': 'Apply the Trifecta',
  'title': 'One technology, two strategies',
  'concept': 'Technology opens possibilities; strategic choices determine how a firm uses them.',
  'scene': 'A refrigeration company has digital operating records, embedded diagnostics and remote '
           'connectivity. It could improve equipment efficiency or promise fewer disruptions '
           'through ongoing monitoring and intervention.',
  'prompt': 'What should guide the choice between these offers?',
  'options': ['Choose the ongoing service because connected products naturally require '
              'subscription strategies.',
              'Choose equipment improvement because the existing product category fixes the '
              'appropriate strategy.',
              'Compare target customers, the benefits they value and the organization’s ability to '
              'deliver each promise.'],
  'feedback': ['Connectivity enables a service but does not establish that it is the preferred '
               'customer promise.',
               'Existing products influence capabilities, but do not by themselves rule out a '
               'different service promise.',
               'The Trifecta opens both possibilities. Strategic aspiration and coordinated '
               'delivery determine how the technologies should be used.'],
  'key': 2,
  'source': 'Session 2, slides 3, 14; Tiwana, Chapter 1: Confluence of the Trifecta. Applied '
            'situation is illustrative.'},
 {'block': 'Strategic position',
  'title': 'A selected market and a lower-cost offer',
  'concept': 'Strategic aspiration combines target market scope with a basis of competition: lower '
             'cost or differentiation.',
  'scene': 'A travel company offers budget study tours only to college student groups. It uses '
           'fixed itineraries and shared transport to keep its operating costs lower than those of '
           'comparable tour providers. Its aim is to offer economical trips to this selected '
           'customer group.',
  'prompt': 'Which competitive position best describes this company?',
  'options': ['Cost focus: serve a selected customer group through a lower-cost offer.',
              'Broad low cost: serve many different customer groups through a lower-cost offer.',
              'Focused differentiation: serve a selected customer group through distinctive '
              'benefits rather than a lower-cost offer.'],
  'feedback': ['The company focuses on college student groups, rather than the whole travel '
               'market. Its fixed itineraries and shared transport support lower costs. A selected '
               'segment plus a lower-cost basis of competition is cost focus.',
               'The lower-cost part fits, but the broad-market part does not. The company serves '
               'only college student groups; operating in several locations would not by itself '
               'make its customer scope broad.',
               'The selected-segment part fits, but the stated basis of competition is lower cost. '
               'Serving a specific group alone does not establish differentiation; the scenario '
               'emphasizes economical trips, rather than distinctive benefits.'],
  'key': 0,
  'source': 'Session 2, slides 16–17; Tiwana, Chapter 1: Strategic aspiration. Applied situation '
            'is illustrative.'},
 {'block': 'Strategic position',
  'title': 'Position versus implementation',
  'concept': 'Aspiration identifies the position sought. Business choices explain the customer '
             'promise and how the firm competes in that position.',
  'scene': 'A diagnostic service proposes priority appointments for customers who value rapid '
           'results. Its team lists three statements for the strategy discussion.',
  'prompt': 'Which statement most directly expresses strategic aspiration?',
  'options': ['Build an appointment system with priority routing and alerts.',
              'Pursue focused differentiation for customers who value rapid diagnostic results.',
              'Reorganize staff shifts to reserve capacity for urgent appointments.'],
  'feedback': ['This describes an IS choice that could support the position, but does not itself '
               'state whom to serve and how to compete.',
               'This identifies both the target segment and the differentiated benefit sought.',
               'This is an organizational choice to deliver the promise. It follows from, rather '
               'than defines, the position.'],
  'key': 1,
  'source': 'Session 2, slides 17, 21; Tiwana, Chapter 1: Strategic aspiration; Syncing, Not '
            'Alignment. Applied situation is illustrative.'},
 {'block': 'Make the fit',
  'title': 'A premium promise, a volume metric',
  'concept': 'Organizational and IS choices should support the business promise.',
  'scene': 'An appliance manufacturer seeks differentiation through durable products. It collects '
           'field failure data, but engineers are rewarded only for releasing more models each '
           'year.',
  'prompt': 'Which configuration best supports the chosen promise?',
  'options': ['Improve the failure dashboard while retaining release-volume incentives.',
              'Increase release volume and use customer communication to emphasize durability.',
              'Connect field failures to design reviews and evaluate engineering priorities '
              'against durability outcomes.'],
  'feedback': ['Better information may help, but incentives and review routines still pull '
               'decisions away from the promise.',
               'More releases and stronger messaging do not establish that products will last '
               'longer.',
               'IS evidence and organizational priorities must reinforce the same customer '
               'promise. Linking failure learning to design decisions creates that fit.'],
  'key': 2,
  'source': 'Session 2, slides 19–21; Tiwana, Chapter 1: Syncing, Not Alignment. Applied situation '
            'is illustrative.'},
 {'block': 'Make the fit',
  'title': 'Detection without intervention',
  'concept': 'An uptime promise needs a response capability, not just observation.',
  'scene': 'A cold-chain provider promises continuity of refrigeration. Its system detects '
           'temperature risks quickly, but local managers cannot authorize emergency technicians '
           'without next-day approval.',
  'prompt': 'Which response best repairs the mismatch?',
  'options': ['Agree on safe escalation authority and response capacity, and connect alerts to '
              'that process.',
              'Invest in more sensitive sensors so alerts arrive earlier.',
              'Narrow alert thresholds so fewer incidents require managerial action.'],
  'feedback': ['The detected risk needs an authorized response. Decision rights and operational '
               'capacity must support the IS-enabled promise.',
               'Earlier detection may help, but does not remove the approval bottleneck preventing '
               'intervention.',
               'Reducing alerts can hide risks without improving response. Threshold changes need '
               'evidence and do not resolve the stated authority gap.'],
  'key': 0,
  'source': 'Session 2, slides 19–21; Tiwana, Chapter 1: Syncing, Not Alignment. Applied situation '
            'is illustrative.'},
 {'block': 'Make the fit',
  'title': 'Synchronization goes both ways',
  'concept': 'Tiwana describes syncing as an ongoing, two-way relationship between operational and '
             'IT strategy, guided by strategic aspiration.',
  'scene': 'A retailer’s new inventory technology enables frequent small replenishments. Buyers '
           'still place large monthly orders, while customers increasingly expect fresh '
           'assortment. The retailer intends to retain that customer promise.',
  'prompt': 'What best reflects continuous synchronization?',
  'options': ['Finalize the technology and require operations to adapt once at launch.',
              'Review replenishment routines and IS rules together as capabilities and customer '
              'needs evolve.',
              'Preserve buying routines and restrict the system to automating the old ordering '
              'cycle.'],
  'feedback': ['A one-time adjustment may become obsolete. Syncing continues as operational needs '
               'and technology possibilities change.',
               'Syncing is an ongoing, two-way relationship guided by strategic aspiration. Both '
               'operating choices and IS design may need revision.',
               'Automating the existing cycle may preserve a mismatch with the customer promise '
               'and fail to exploit the new capability.'],
  'key': 1,
  'source': 'Session 2, slides 19–21, 24–26; Tiwana, Chapter 1: Syncing, Not Alignment. Applied '
            'situation is illustrative.'},
 {'block': 'Competitive response',
  'title': 'Protect today’s revenue or renew the offer?',
  'concept': 'Rivals can copy visible technology. New offers may also reduce revenue from the '
             'current business.',
  'scene': 'A maintenance firm’s remote prevention service may reduce profitable emergency visits. '
           'Rivals can buy similar monitoring software. Managers disagree about whether to launch '
           'the service.',
  'prompt': 'Which assessment best addresses both competitive pressures?',
  'options': ['Reject the service because any loss of emergency revenue destroys value.',
              'Launch quickly and rely on the monitoring software to prevent imitation.',
              'Evaluate the total customer and revenue effects, delivery capabilities and how the '
              'offer must evolve as rivals respond.'],
  'feedback': ['Lost emergency revenue is relevant, but customers may value prevention and pay '
               'differently. The total economics and future competitive position need assessment.',
               'Readily available software is unlikely to protect the offer by itself. Execution '
               'and continued adaptation matter.',
               'The choice involves cannibalization, imitation and delivery. Neither current '
               'revenue protection nor technology ownership alone resolves these trade-offs.'],
  'key': 2,
  'source': 'Session 2, slides 23–26; Tiwana, Chapter 1: Strategic aspiration; Syncing, Not '
            'Alignment. Applied situation is illustrative.'}]

RETRY_HINTS = ['Ask what each change lets people or equipment do. Which of those benefits does a connection '
 'count actually show?',
 'Trace what is bought, how it is purchased and how the item itself reaches the customer.',
 'Separate the content from its carrier and compare only the dimensions that changed.',
 'Distinguish the cost of one additional copy from the costs of creating and operating the '
 'offering.',
 'Separate the technology’s possibility from the business model chosen to use it.',
 'Ask whom the firm intends to serve and what it can credibly promise them.',
 'Make two separate choices: whom does the company serve, and does it compete mainly through lower '
 'cost or distinctive benefits?',
 'Look for both a selected customer group and a basis of competition, rather than a delivery '
 'mechanism.',
 'Trace whether the information, work routines and incentives all support durability.',
 'Follow what must happen after an alert for the promised continuity to be delivered.',
 'Consider how changes in technology and business needs can each trigger changes in the other.',
 'Consider the whole offer’s economics and the ability to keep creating value when competitors '
 'respond.']

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
            is_correct = False
            if choice is not None:
                idx = item['options'].index(choice)
                is_correct = idx == item['key']
                if is_correct:
                    st.session_state[ANSWER_KEY][stage] = choice
                    st.success("Correct — " + item['feedback'][idx])
                    st.caption("You can now continue. There are no marks.")
                else:
                    st.session_state[ANSWER_KEY].pop(stage, None)
                    st.warning("Not quite — " + item['feedback'][idx])
                    st.info("Hint: " + RETRY_HINTS[stage])
                    st.caption("Try again: select another answer above.")
        left, right = st.columns(2)
        with left:
            if st.button("Previous", disabled=stage==0, key=f"{PREFIX}_previous", use_container_width=True):
                _go(stage-1)
        with right:
            if st.button("View summary" if stage==count-1 else "Continue", disabled=not is_correct, key=f"{PREFIX}_next", type="primary", use_container_width=True):
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
        st.caption("These illustrative revision situations apply concepts from the assigned readings; consult the course copies for the full arguments.")

def render_session_02():
    _render()

if __name__ == "__main__":
    st.set_page_config(page_title="ISM LAB · Session 2", page_icon="📘", layout="wide")
    render_session_02()



