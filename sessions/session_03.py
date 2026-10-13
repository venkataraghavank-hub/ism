"""Session 3: source-grounded concept revision. Import render_session_03, or run with streamlit run session_03.py. Requires streamlit>=1.32. No external APIs or data files."""
import html
import streamlit as st

SESSION = 3
PREFIX = 'ism_s3'
STAGE_KEY = 'ism_s3_stage'
ANSWER_KEY = 'ism_s3_answers'
TITLE = 'Information systems as a strategic tool'
INTRO = ('Apply the three strategic lenses to varied business situations. Trace competitive mechanisms, '
 'activity linkages and the conditions for sustained advantage.')
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
  'title': 'Which question needs which lens?',
  'concept': 'Five Forces examines the industry; the value chain examines firm activities relative '
             'to rivals; the litmus test examines an individual IT asset.',
  'scene': 'A retailer faces sector-wide price pressure, slow replenishment and a proprietary '
           'demand dataset. Its CEO proposes using one framework to decide whether the dataset can '
           'sustain an advantage.',
  'prompt': 'Which approach best matches the distinct questions?',
  'options': ['Use Five Forces to establish that any proprietary dataset is defensible in a '
              'difficult industry.',
              'Use the litmus test for the dataset’s defensibility, the value chain for '
              'replenishment and Five Forces for industry pressure.',
              'Use the value chain to determine whether the entire industry has attractive '
              'margins.'],
  'feedback': ['Industry pressure does not establish whether this particular resource is valuable, '
               'rare or hard to imitate or substitute.',
               'The lenses examine different levels: industry conditions, activities and linkages, '
               'and individual resources. They complement one another.',
               'The value chain helps analyze activities within and across firms. Industry '
               'attractiveness requires examining industry forces.'],
  'key': 1,
  'source': 'Session 3, slides 3–4, 19–20; Tiwana, Chapter 2: The Three Lenses. Applied situation '
            'is illustrative.'},
 {'block': 'Industry forces',
  'title': 'Growing market, thinner margins',
  'concept': 'Stronger forces can lower prices firms receive or raise costs, squeezing industry '
             'margins. Industry growth alone does not establish attractiveness.',
  'scene': 'An online services industry gains customers quickly. Price comparison makes buyers '
           'more demanding, while a few essential suppliers increase fees. Analysts call the '
           'industry attractive because demand is growing.',
  'prompt': 'Which assessment best applies Five Forces?',
  'options': ['Growth can coexist with margin pressure if buyers constrain prices and suppliers '
              'raise costs.',
              'Growth reduces the importance of buyer and supplier power because revenue will '
              'rise.',
              'Supplier fee increases affect individual firms, so they are outside industry '
              'analysis.'],
  'feedback': ['Industry attractiveness depends on the ability to retain value, not demand growth '
               'alone. Buyer and supplier power can squeeze the gap between revenue and cost.',
               'More customers do not ensure profitable customers. Strong forces can limit margins '
               'even in a growing market.',
               'If essential suppliers have bargaining power over industry participants, their '
               'fees are directly relevant to industry margins.'],
  'key': 0,
  'source': 'Session 3, slides 5–9; Tiwana, Chapter 2: Four Nuances; Five Forces and Margins. '
            'Applied situation is illustrative.'},
 {'block': 'Industry forces',
  'title': 'A threat before customers switch',
  'concept': 'A substitute meets the same need differently. The threat of substitutes or new '
             'entrants can constrain prices before entry or switching occurs.',
  'scene': 'Corporate clients tell a conference organizer that virtual events are an acceptable '
           'alternative for some meetings. Few have switched yet, but clients use the option when '
           'negotiating prices.',
  'prompt': 'What is the strongest interpretation?',
  'options': ['There is no substitute pressure until clients actually choose virtual events.',
              'Virtual events are new entrants to the same physical conference business because '
              'both serve corporate clients.',
              'An alternative way of meeting the need can constrain prices before switching '
              'occurs.'],
  'feedback': ['A credible alternative can affect bargaining and willingness to pay before it '
               'captures many sales.',
               'Serving the same need does not make the operating model identical. The scenario '
               'describes a different way to fulfill the meeting need.',
               'The threat of substitution can cap prices even while most customers remain. Actual '
               'switching is not necessary for pressure to arise.'],
  'key': 2,
  'source': 'Session 3, slides 5, 8–9; Tiwana, Chapter 2: Four Nuances. Applied situation is '
            'illustrative.'},
 {'block': 'Industry forces',
  'title': 'Supplier power can move both ways',
  'concept': 'Transparency can improve comparison of suppliers; wider access to buyers can '
             'increase suppliers’ options. Effects depend on the mechanism.',
  'scene': 'A procurement platform makes suppliers’ prices easy to compare. It also gives those '
           'suppliers access to buyers beyond their previous local customers.',
  'prompt': 'What should the purchasing manager conclude?',
  'options': ['The platform necessarily weakens suppliers because buyers can compare quotes.',
              'Comparison may weaken supplier power, while wider access to buyers may strengthen '
              'it; assess both mechanisms.',
              'The platform necessarily strengthens suppliers because their potential market '
              'grows.'],
  'feedback': ['Comparison supports buyers, but suppliers’ additional alternatives can offset that '
               'effect.',
               'Transparency and wider market access pull in different directions. Their net '
               'effect depends on alternatives, differentiation and the actual trading situation.',
               'More alternatives can strengthen suppliers, but improved buyer comparison also '
               'matters. Market growth alone does not settle bargaining power.'],
  'key': 1,
  'source': 'Session 3, slides 8–9; Tiwana, Chapter 2: How IT Alters the Five Forces. Applied '
            'situation is illustrative.'},
 {'block': 'Industry forces',
  'title': 'A better customer offer, a harder industry',
  'concept': 'IT can increase price transparency and let entrants rent capacity instead of owning '
             'traditional infrastructure.',
  'scene': 'An industry adopts price-comparison tools and inexpensive rented computing. Customers '
           'compare offers more easily, and new firms need less upfront IT investment.',
  'prompt': 'Which interpretation best distinguishes the two effects?',
  'options': ['Buyer power can increase while IT-related entry barriers fall, without eliminating '
              'other entry requirements.',
              'Comparison primarily changes supplier power, while rented computing makes buyers '
              'less price-sensitive.',
              'Both changes mainly improve incumbent efficiency, so they necessarily increase '
              'industry margins.'],
  'feedback': ['Transparency improves buyer choice; rented capacity can reduce one entry hurdle. '
               'Regulation, expertise and other barriers may still remain.',
               'The described comparisons concern customers choosing providers. Rented computing '
               'concerns entrants’ capacity costs, not buyer price sensitivity.',
               'Incumbents can benefit too, but greater buyer power and easier entry can intensify '
               'pressure on margins.'],
  'key': 0,
  'source': 'Session 3, slides 8–9; Tiwana, Chapter 2: How IT Alters the Five Forces. Applied '
            'situation is illustrative.'},
 {'block': 'Industry forces',
  'title': 'Size is not enough for a network barrier',
  'concept': 'Operational efficiency can protect margins. Network effects and deep customization '
             'can erect unconventional competitive barriers.',
  'scene': 'A professional marketplace has many registered accounts but little useful interaction. '
           'A smaller rival has fewer accounts and more active matching between buyers and '
           'experts.',
  'prompt': 'What evidence best tests whether the larger marketplace has an unconventional '
            'barrier?',
  'options': ['The total number of accounts exceeds the rival’s, demonstrating stronger network '
              'effects.',
              'It has invested more in servers, demonstrating that matching will become valuable.',
              'Useful participation increases member value and is difficult for a rival to '
              'recreate or replace.'],
  'feedback': ['Registered accounts need not create useful connections. Network effects depend on '
               'the value participation adds, not headcount alone.',
               'Infrastructure spending can support operations but does not establish useful '
               'participation or a competitive barrier.',
               'A network barrier comes from the value of interaction and the difficulty of '
               'assembling or replacing that useful network. Scale without activity is '
               'insufficient.'],
  'key': 2,
  'source': 'Session 3, slides 8–9, 25; Tiwana, Chapter 2: IT Antidotes. Applied situation is '
            'illustrative.'},
 {'block': 'Value chain',
  'title': 'Local savings, system cost',
  'concept': 'A value chain explains how activities turn inputs into outputs worth more to '
             'customers. Activities may cut across departments and contain physical and '
             'informational components.',
  'scene': 'A manufacturer automates packing and lowers warehouse labor costs. Packages now arrive '
           'in larger batches, increasing delivery delays and retailers’ stockouts.',
  'prompt': 'How should a value-chain analysis evaluate the change?',
  'options': ['Approve it on the warehouse savings because each activity should optimize its own '
              'cost.',
              'Assess costs and customer value across packing, delivery and replenishment linkages '
              'before judging the gain.',
              'Treat downstream delays only as the transport department’s performance problem.'],
  'feedback': ['A local gain can create larger costs or value losses elsewhere. Activity '
               'optimization does not automatically optimize the chain.',
               'The value chain connects activities. The relevant result includes downstream '
               'coordination and the value customers receive.',
               'The packing change alters downstream work. Department boundaries should not hide '
               'those linkages.'],
  'key': 1,
  'source': 'Session 3, slides 10–13; Tiwana, Chapter 2: Lens 2: Value Chains. Applied situation '
            'is illustrative.'},
 {'block': 'Value chain',
  'title': 'A faster step or a better linkage?',
  'concept': 'IT can improve one activity or change coordination and structure between activities, '
             'including across firms.',
  'scene': 'A retailer considers two changes: faster item picking within its warehouse and sharing '
           'store demand signals with suppliers to schedule replenishment.',
  'prompt': 'Which comparison best identifies the source of improvement?',
  'options': ['Faster picking improves an activity; shared demand signals improve coordination '
              'between activities and firms.',
              'Both are activity-level improvements because each uses warehouse data.',
              'Shared signals change only the purchasing activity because the retailer sends the '
              'message.'],
  'feedback': ['One changes performance inside a step; the other changes how activities connect. '
               'Both may affect cost and service.',
               'Using the same data does not make the mechanism the same. Shared signals can '
               'change coordination across organizational boundaries.',
               'The message affects supplier planning and replenishment as well as purchasing. Its '
               'value lies partly in those linkages.'],
  'key': 0,
  'source': 'Session 3, slides 11–13; Tiwana, Chapter 2: Transforming Value Chains with IT. '
            'Applied situation is illustrative.'},
 {'block': 'Value chain',
  'title': 'A loyalty database that changes nothing',
  'concept': 'Commodity technology can create value when combined with proprietary customer '
             'knowledge and changed decisions.',
  'scene': 'A hotel chain builds rich guest histories. Marketing still sends the same discount to '
           'every guest. Management claims it has reproduced the strategic logic of Tiwana’s '
           'casino example.',
  'prompt': 'What is missing from that claim?',
  'options': ['A larger database is needed before customer knowledge can affect decisions.',
              'A distinctive loyalty card design is needed to turn the common system into '
              'strategic IT.',
              'Customer insights must change targeting and incentives in ways that improve value, '
              'rather than merely accumulate records.'],
  'feedback': ['More records may help, but the stated gap is that decisions do not use the '
               'insights already available.',
               'Card design does not establish the decision changes responsible for the example’s '
               'value.',
               'In the casino example, insights challenged assumptions about valuable customers '
               'and changed marketing choices. Capturing history alone does not reproduce that '
               'logic.'],
  'key': 2,
  'source': 'Session 3, slides 14; Tiwana, Chapter 2: Value-Adding Applications: Casino Example. '
            'Applied situation is illustrative.'},
 {'block': 'Value chain',
  'title': 'An intermediary disappears; its work remains',
  'concept': 'Digital purchasing can reconfigure intermediary linkages while the offering and '
             'delivery remain physical.',
  'scene': 'A printed-book seller moves online and removes a wholesaler from its distribution '
           'route. It still needs storage, order fulfillment and returns handling.',
  'prompt': 'Which assessment best applies value-chain reconfiguration?',
  'options': ['Removing the wholesaler means its former share of revenue becomes the seller’s '
              'profit.',
              'An intermediary layer can disappear while its necessary activities move elsewhere, '
              'so net value depends on the new costs and linkages.',
              'Digital purchasing means the printed book no longer requires a physical supply '
              'chain.'],
  'feedback': ['The seller or another party may now perform costly activities previously handled '
               'by the wholesaler. Removed revenue shares are not automatically profit.',
               'Disintermediation changes who performs activities and how they connect. Physical '
               'fulfillment and transferred responsibilities still need evaluation.',
               'The buying process is digital, but the printed offering and delivery remain '
               'physical. Online ordering does not eliminate logistics.'],
  'key': 1,
  'source': 'Session 3, slides 15–17; Tiwana, Chapter 2: Value Chain Reconfiguration. Applied '
            'situation is illustrative.'},
 {'block': 'Value chain',
  'title': 'Digital delivery, optional intermediaries',
  'concept': 'Digitizing the offering enables digital delivery and can permit further changes in '
             'the value stream.',
  'scene': 'An author can sell an e-book directly through a platform. A publisher offers editing, '
           'promotion and rights management. Managers argue that digital delivery makes every '
           'publisher unnecessary.',
  'prompt': 'Which conclusion is supported?',
  'options': ['Digital offerings can enable fewer intermediary layers, but an intermediary may '
              'remain if its activities add value.',
              'Publishers must remain because the activities in a traditional printed-book chain '
              'cannot change.',
              'Publishers must disappear because eliminating physical delivery eliminates all '
              'their activities.'],
  'feedback': ['Digitization enables reconfiguration without predetermining one universal chain. '
               'Editing, discovery and other services may still justify an intermediary.',
               'Digital creation and delivery can change which layers are needed and how '
               'activities are organized. Tradition alone does not justify the existing chain.',
               'Physical distribution is only one possible activity. Nonphysical services can '
               'still add value.'],
  'key': 0,
  'source': 'Session 3, slides 18; Tiwana, Chapter 2: Value Chain Reconfiguration. Applied '
            'situation is illustrative.'},
 {'block': 'Resource advantage',
  'title': 'Necessary and valuable, but common',
  'concept': 'Valuable and rare assets may create advantage. Costly imitation and lack of '
             'equivalent substitutes help sustain it. Valuable common assets can support parity.',
  'scene': 'A bank’s standard transaction platform improves reliability. All major rivals can '
           'purchase comparable systems. The CFO says it either creates sustained advantage or '
           'should be removed.',
  'prompt': 'Which response best applies the competitive litmus test?',
  'options': ['Keep it because any costly, reliable system establishes a sustained advantage.',
              'Remove it because a resource that rivals can buy cannot create business value.',
              'It may be essential for parity and operations, while its availability to rivals '
              'means the evidence does not establish rarity.'],
  'feedback': ['Cost and reliability can establish usefulness, but do not establish rarity, costly '
               'imitation or lack of substitutes.',
               'Common resources can create operational value and be necessary to compete. Absence '
               'of advantage does not mean absence of value.',
               'The resource can be valuable without being rare. Sustained advantage requires '
               'further conditions beyond usefulness.'],
  'key': 2,
  'source': 'Session 3, slides 20, 23; Tiwana, Chapter 2: Lens 3: Competitive Litmus Test. Applied '
            'situation is illustrative.'},
 {'block': 'Resource advantage',
  'title': 'Different resource, equivalent result',
  'concept': 'Custom construction alone does not satisfy the litmus test. Proprietary data and '
             'useful networks may be harder to reproduce, but must still be assessed.',
  'scene': 'A streaming firm’s proprietary viewing histories are valuable, rare and difficult to '
           'copy. A rival’s interviews and experiments nevertheless produce equally effective '
           'recommendations for its customers.',
  'prompt': 'What does this challenge in the litmus test?',
  'options': ['Rarity, because equivalent recommendations mean the rival owns the same viewing '
              'histories.',
              'Nonsubstitutability, because a different resource may deliver equivalent customer '
              'value.',
              'Value, because the original histories become useless whenever an alternative '
              'approach exists.'],
  'feedback': ['The rival does not need the same histories to reach a similar result. Rarity '
               'concerns access to the resource itself.',
               'Costly copying does not rule out achieving the same ends differently. An effective '
               'alternative challenges sustainability through substitution.',
               'The histories may remain useful. The issue is whether their value can sustain a '
               'unique advantage when customers can obtain an equivalent result elsewhere.'],
  'key': 1,
  'source': 'Session 3, slides 20, 23, 25; Tiwana, Chapter 2: Competitive Litmus Test; '
            'Applications and Data. Applied situation is illustrative.'},
 {'block': 'Resource advantage',
  'title': 'Resources that never become a capability',
  'concept': 'Skills, processes and decision rights connect resources to capabilities and customer '
             'value. VRIO makes organization explicit; Tiwana’s litmus test uses VRIN.',
  'scene': 'A grocery service owns demand data, automation and specialist expertise. Inventory '
           'planners and delivery managers work to conflicting priorities, causing late deliveries '
           'and spoilage.',
  'prompt': 'What best explains why the resources have not produced the intended customer value?',
  'options': ['The resources need coordinated processes and decision rights to become a reliable '
              'logistics capability; VRIO makes organization explicit.',
              'The resources must be valueless because customer outcomes have not improved.',
              'The missing condition is VRIN’s nonsubstitutability, which is identical to VRIO’s '
              'organization criterion.'],
  'feedback': ['Resources must be organized into effective work. Coordination can turn them into '
               'capabilities; organization and nonsubstitutability are different criteria.',
               'Poor use does not prove a resource has no potential value. Conflicting priorities '
               'identify a barrier between resources and realised outcomes.',
               'Nonsubstitutability tests equivalent alternatives; organization tests whether the '
               'firm can use resources effectively. They are not interchangeable.'],
  'key': 0,
  'source': 'Session 3, slides 21, 24, 26; Tiwana, Chapter 2: Competitive Litmus Test; deck’s VRIO '
            'extension. Applied situation is illustrative.'}]

RETRY_HINTS = ['Separate the industry question, the activity question and the resource question.',
 'Examine what firms can charge and what they must pay, rather than market size alone.',
 'Ask whether the alternative meets the underlying need differently and how its availability '
 'affects negotiations.',
 'Consider whose alternatives improve under each platform feature.',
 'Identify who gains negotiating alternatives and which investment a new entrant can avoid.',
 'Look for value gained from other participants and whether an alternative network can offer '
 'equivalent value.',
 'Follow the effect of one activity’s change on later activities and the customer outcome.',
 'Distinguish doing one step better from changing how several steps are coordinated.',
 'Trace how information changes whom marketing serves and what it offers them.',
 'Ask which activities disappear and which must still be performed by someone.',
 'Separate physical distribution from the other functions an intermediary may perform.',
 'Distinguish business value, competitive parity and sustained advantage.',
 'Separate reproducing the same asset from achieving the same outcome by another route.',
 'Trace the chain from resources through coordinated work to the customer result, and distinguish '
 'VRIN from VRIO.']

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
        st.caption("These illustrative revision situations apply concepts from the assigned readings; consult the course copies for the full arguments.")

def render_session_03():
    _render()

if __name__ == "__main__":
    st.set_page_config(page_title="ISM LAB · Session 3", page_icon="📘", layout="wide")
    render_session_03()

