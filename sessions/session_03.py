"""Session 3: source-grounded concept revision. Import render_session_03, or run with streamlit run session_03.py. Requires streamlit>=1.32. No external APIs or data files."""
import html
import streamlit as st

SESSION = 3
PREFIX = 'ism_s3'
STAGE_KEY = 'ism_s3_stage'
ANSWER_KEY = 'ism_s3_answers'
TITLE = 'Information systems as a strategic tool'
INTRO = ('Examine industry forces, changes in value-chain activities, and the defensibility of IT resources using '
 'the session’s examples.')
SUMMARY_TITLE = 'Your Three-Lens Review'
TAKEAWAYS = ['The three lenses address industry, firm activities and individual IT assets.',
 'Industry forces affect margins; IT can strengthen or weaken forces through different mechanisms.',
 'IT can reduce cost or add value within an activity and transform linkages between activities.',
 'Valuable common resources can support parity; value and rarity alone do not establish sustainability.',
 'Resources require complementary skills and organization to become capabilities that create customer value.']
GLOSSARY = {'Five Forces': 'Industry rivalry, buyer power, supplier power, threat of entry and threat of substitutes.',
 'Substitute': 'A different way of satisfying the same customer need.',
 'Value chain': 'Activities and linkages through which the firm creates and delivers value.',
 'Disintermediation': 'Removal or bypassing of intermediary layers.',
 'VRIN': 'Valuable, rare, costly to imitate and non-substitutable.',
 'VRIO': 'Value, rarity, costly imitation and organization to exploit the resource.',
 'Network effects': 'Useful participation increases the value of a network.',
 'Capability': 'What a firm can do by coordinating resources with complementary skills and processes.'}
READING = ('Primary sources: Session 3 teaching deck and Amrit Tiwana, IT Strategy for Non-IT Managers, Chapter 2. The '
 'deck adds VRIO and the illustrative Amazon book and Amazon Fresh exercises.')
DECISIONS = [{'block': 'Three lenses',
  'title': 'Choose the level',
  'concept': 'Five Forces examines the industry; the value chain examines firm activities relative to '
             'rivals; the litmus test examines an individual IT asset.',
  'scene': 'You want to know whether proprietary customer data can sustain an advantage.',
  'prompt': 'Which lens directly addresses this question?',
  'options': ['Five Forces alone', 'The competitive litmus test', 'The value chain alone'],
  'feedback': ['Five Forces explains industry pressures, not the defensibility of this particular asset.',
               'The litmus test examines value, rarity, imitation and substitutes for the asset.',
               'The value chain locates value creation, but does not by itself test sustainability.'],
  'key': 1,
  'source': 'Session 3, slides 3–4, 19–20; Tiwana, Chapter 2: The Three Lenses.'},
 {'block': 'Industry forces',
  'title': 'Forces and margins',
  'concept': 'Stronger forces can lower prices firms receive or raise costs, squeezing industry margins. '
             'Industry growth alone does not establish attractiveness.',
  'scene': 'Customers gain negotiating clout while suppliers raise input prices.',
  'prompt': 'What is the likely pressure?',
  'options': ['Industry margins are squeezed',
              'Margins must rise because transactions are digital',
              'Only one firm is affected by industry forces'],
  'feedback': ['Buyer and supplier power can both erode the margins of firms in an industry.',
               'Digital transactions do not remove bargaining power.',
               'Five Forces concerns industry conditions, though firms can respond differently.'],
  'key': 0,
  'source': 'Session 3, slides 5–9; Tiwana, Chapter 2: Four Nuances; Five Forces and Margins.'},
 {'block': 'Industry forces',
  'title': 'Substitutes and entry threats',
  'concept': 'A substitute meets the same need differently. The threat of substitutes or new entrants can '
             'constrain prices before entry or switching occurs.',
  'scene': 'The deck uses Zoom as an alternative to some business travel.',
  'prompt': 'Why can this matter to travel providers?',
  'options': ['Only an actual airline entrant matters',
              'Zoom is an airline rival using the same activity system',
              'An alternative way to meet the need can cap prices'],
  'feedback': ['Substitutes can affect profitability without entering as another airline.',
               'The mechanism is a different way to meet some communication needs.',
               'The substitute threat can constrain what travel providers charge, even before every buyer '
               'switches.'],
  'key': 2,
  'source': 'Session 3, slides 5, 8–9; Tiwana, Chapter 2: Four Nuances.'},
 {'block': 'Industry forces',
  'title': 'Supplier power: two mechanisms',
  'concept': 'Transparency can improve comparison of suppliers; wider access to buyers can increase '
             'suppliers’ options. Effects depend on the mechanism.',
  'scene': 'An online procurement market displays offers and connects suppliers to more buyers.',
  'prompt': 'Which interpretation matches the book and deck?',
  'options': ['IT always weakens supplier power',
              'Comparison can weaken supplier power; wider buyer access can strengthen it',
              'Only customer power can change'],
  'feedback': ['The same technology can create opposing mechanisms.',
               'Comparison increases buyer leverage, while access to more buyers can improve supplier '
               'alternatives.',
               'Both supplier and customer bargaining power can change.'],
  'key': 1,
  'source': 'Session 3, slides 8–9; Tiwana, Chapter 2: How IT Alters the Five Forces.'},
 {'block': 'Industry forces',
  'title': 'Buyer power and entry',
  'concept': 'IT can increase price transparency and let entrants rent capacity instead of owning '
             'traditional infrastructure.',
  'scene': 'The deck uses Google Flights for comparisons and AWS for rented IT capacity.',
  'prompt': 'Which pair of effects fits these illustrations?',
  'options': ['More buyer power; lower IT entry hurdles',
              'Less buyer power; entrants must own every server',
              'Both automatically create durable advantage for incumbents'],
  'feedback': ['Comparison expands buyer choice; rented capacity reduces an entrant’s initial IT '
               'requirements.',
               'These mechanisms move in the opposite directions in the illustrations.',
               'These can increase competitive pressure rather than protect existing firms.'],
  'key': 0,
  'source': 'Session 3, slides 8–9; Tiwana, Chapter 2: How IT Alters the Five Forces.'},
 {'block': 'Industry forces',
  'title': 'IT antidotes',
  'concept': 'Operational efficiency can protect margins. Network effects and deep customization can erect '
             'unconventional competitive barriers.',
  'scene': 'A platform grows more useful through participation; a business system becomes deeply tailored to '
           'customer work.',
  'prompt': 'What should a manager examine?',
  'options': ['Whether buying identical software guarantees the same barrier',
              'Whether every customer is permanently locked in',
              'How useful participation or customization makes entry or switching harder'],
  'feedback': ['The barrier depends on the network or customization, not simply the purchased software.',
               'These effects can be overcome; permanence should not be assumed.',
               'These are the mechanisms behind the network-effect and customization examples.'],
  'key': 2,
  'source': 'Session 3, slides 8–9, 25; Tiwana, Chapter 2: IT Antidotes.'},
 {'block': 'Value chain',
  'title': 'Activities and value',
  'concept': 'A value chain explains how activities turn inputs into outputs worth more to customers. '
             'Activities may cut across departments and contain physical and informational components.',
  'scene': 'Vandelay considers changes to operations and after-sales service.',
  'prompt': 'How should managers evaluate a proposed IT change?',
  'options': ['Only by which department owns the software',
              'By how it lowers cost or increases customer value in activities and linkages',
              'Only by the number of automated tasks'],
  'feedback': ['Department ownership does not establish value creation.',
               'This connects the proposal to the firm’s activities and customer promise.',
               'Automation matters when it changes cost or value; a task count alone is insufficient.'],
  'key': 1,
  'source': 'Session 3, slides 10–13; Tiwana, Chapter 2: Lens 2: Value Chains.'},
 {'block': 'Value chain',
  'title': 'Steps versus linkages',
  'concept': 'IT can improve one activity or change coordination and structure between activities, including '
             'across firms.',
  'scene': 'Compare faster processing within a warehouse with sharing demand data between retail and '
           'production.',
  'prompt': 'Which distinction is appropriate?',
  'options': ['First improves a step; second improves a linkage',
              'Both are only changes in marketing',
              'Neither can affect costs'],
  'feedback': ['One improves work inside an activity; the other connects activities so decisions can be '
               'coordinated.',
               'Warehouse processing and demand-production coordination span different activities.',
               'Both can affect cost and value through different mechanisms.'],
  'key': 0,
  'source': 'Session 3, slides 11–13; Tiwana, Chapter 2: Transforming Value Chains with IT.'},
 {'block': 'Value chain',
  'title': 'Harrah’s customer insight',
  'concept': 'Commodity technology can create value when combined with proprietary customer knowledge and '
             'changed decisions.',
  'scene': 'In Tiwana’s casino example, loyalty information challenged the focus on wealthy gamblers and '
           'informed customized incentives.',
  'prompt': 'What explains the strategic value?',
  'options': ['The loyalty card alone guarantees an advantage',
              'Every casino must target wealthy gamblers',
              'Customer insight changed whom marketing served and how incentives were allocated'],
  'feedback': ['The card collected observations; analytical insight and changed decisions made them useful.',
               'The example challenges that industry assumption using customer evidence.',
               'The contribution was the combination of data, analysis and marketing decisions.'],
  'key': 2,
  'source': 'Session 3, slides 14; Tiwana, Chapter 2: Value-Adding Applications: Casino Example.'},
 {'block': 'Value chain',
  'title': 'Amazon: printed books',
  'concept': 'Digital purchasing can reconfigure intermediary linkages while the offering and delivery '
             'remain physical.',
  'scene': 'The deck compares the traditional chain with an illustrative author–publisher–Amazon–consumer '
           'chain.',
  'prompt': 'What does this show?',
  'options': ['Printed books can always be delivered as bits',
              'Intermediary layers can change while physical fulfillment remains',
              'The slide allocations prove actual Amazon profit margins'],
  'feedback': ['A printed book still requires physical delivery.',
               'This illustrates structural reconfiguration and disintermediation in the distribution chain.',
               'The dollar allocations are teaching illustrations, not actual Amazon economics.'],
  'key': 1,
  'source': 'Session 3, slides 15–17; Tiwana, Chapter 2: Value Chain Reconfiguration.'},
 {'block': 'Value chain',
  'title': 'Amazon: e-books',
  'concept': 'Digitizing the offering enables digital delivery and can permit further changes in the value '
             'stream.',
  'scene': 'The deck then shows an illustrative author–Amazon–consumer e-book chain.',
  'prompt': 'Which conclusion is supported?',
  'options': ['Product digitization can enable further disintermediation',
              'Publishers must disappear from every e-book business',
              'An e-book always has the exact price shown in the slide'],
  'feedback': ['The example illustrates a possible reconfiguration, not a universal industry arrangement.',
               'The teaching scenario does not show that every publisher becomes unnecessary.',
               'The prices and allocations are illustrative.'],
  'key': 0,
  'source': 'Session 3, slides 18; Tiwana, Chapter 2: Value Chain Reconfiguration.'},
 {'block': 'Resource advantage',
  'title': 'The competitive litmus test',
  'concept': 'Valuable and rare assets may create advantage. Costly imitation and lack of equivalent '
             'substitutes help sustain it. Valuable common assets can support parity.',
  'scene': 'A reliable standard application is available to all major rivals.',
  'prompt': 'How should it be described?',
  'options': ['Useless because competitors can buy it',
              'Sustainable advantage solely because it is expensive',
              'Potentially valuable for operations, but not rare on this evidence'],
  'feedback': ['Competitive necessities can have substantial operational value.',
               'Purchase cost does not establish rarity, imitation barriers or non-substitutability.',
               'Value does not by itself demonstrate a competitive advantage over rivals.'],
  'key': 2,
  'source': 'Session 3, slides 20, 23; Tiwana, Chapter 2: Lens 3: Competitive Litmus Test.'},
 {'block': 'Resource advantage',
  'title': 'Custom apps, data and networks',
  'concept': 'Custom construction alone does not satisfy the litmus test. Proprietary data and useful '
             'networks may be harder to reproduce, but must still be assessed.',
  'scene': 'Compare a copyable custom feature with Netflix viewing insights and LinkedIn’s useful '
           'participation.',
  'prompt': 'Which question is most useful?',
  'options': ['Was the application written from scratch?',
              'Can rivals reproduce the useful data or network, or achieve equivalent value another way?',
              'Does the database contain a large number of rows?'],
  'feedback': ['Custom development is a construction choice, not proof of sustainable advantage.',
               'This tests imitation and strategic substitutes for the value-producing resource and '
               'capability.',
               'Volume alone does not establish valuable, rare or defensible insight.'],
  'key': 1,
  'source': 'Session 3, slides 20, 23, 25; Tiwana, Chapter 2: Competitive Litmus Test; Applications and '
            'Data.'},
 {'block': 'Resource advantage',
  'title': 'Resources become capabilities',
  'concept': 'Skills, processes and decision rights connect resources to capabilities and customer value. '
             'VRIO makes organization explicit; Tiwana’s litmus test uses VRIN.',
  'scene': 'The Amazon Fresh illustration links data, automation and expertise to logistics and cold-chain '
           'capabilities.',
  'prompt': 'Which account completes the chain?',
  'options': ['Organized resources enable coordinated logistics and cold-chain work, creating convenient '
              'delivery and fresh groceries',
              'Owning automation alone proves customer value',
              'VRIO and VRIN have exactly the same final criterion'],
  'feedback': ['The value comes through what the firm can do with its resources and the benefit customers '
               'receive.',
               'Ownership alone does not show effective use or delivery of the promise.',
               'VRIN highlights non-substitutability; VRIO explicitly asks whether the organization can '
               'exploit the resource.'],
  'key': 0,
  'source': 'Session 3, slides 21, 24, 26; Tiwana, Chapter 2: Competitive Litmus Test; deck’s VRIO '
            'extension.'}]

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
        st.markdown("""
| Lens | Question | Course reading |
|---|---|---|
| Five Forces | How does IT change industry competition and margins? | Tiwana, Chapter 2, Lens 1; Session 3 deck |
| IT antidotes | How can efficiency, network effects and customization respond to competitive pressure? | Tiwana, Chapter 2; Session 3 deck |
| Value chain | Where can IT reduce cost, add value or change activities and linkages? | Tiwana, Chapter 2, Lens 2; Session 3 deck |
| Competitive litmus test (VRIN) | Can an IT asset create and sustain an advantage over rivals? | Tiwana, Chapter 2, Lens 3; Session 3 deck |
| Organization (VRIO) | Is the firm organized to exploit the resource? | Session 3 deck's VRIO extension |
| Resources and capabilities | How do resources and complementary arrangements create customer value? | Session 3 deck; Tiwana, Chapter 2 |
""")
        st.markdown("**Concept reminders**")
        for term, definition in GLOSSARY.items():
            st.markdown(f"**{term}:** {definition}")
        st.caption("The tutorial paraphrases the assigned readings; consult the course copies for the full arguments.")

def render_session_03():
    _render()

if __name__ == "__main__":
    st.set_page_config(page_title="ISM LAB · Session 3", page_icon="📘", layout="wide")
    render_session_03()
