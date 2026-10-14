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
  'source': 'Updated Session 3 deck, slides 3–4, 23; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
 {'block': 'Industry forces',
  'title': 'More bookings, less profit per booking',
  'concept': 'Stronger forces can lower prices firms receive or raise costs, squeezing industry '
             'margins. Industry growth alone does not establish attractiveness.',
  'scene': 'Hotels in a town are receiving more bookings. Guests use online comparisons to '
           'negotiate lower room rates. At the same time, the two firms that provide most hotels '
           'with laundry services raise their charges. An investor argues that more bookings must '
           'make the hotel industry more attractive.',
  'prompt': 'Why might hotel profit margins still fall even as bookings increase?',
  'options': ['Guests can put downward pressure on room rates, while powerful suppliers raise the '
              'cost of serving each guest.',
              'More bookings will necessarily offset lower room rates and higher laundry charges.',
              'Higher laundry charges matter only for individual hotels, so they should be '
              'excluded from an industry assessment.'],
  'feedback': ['Buyer power can limit the price hotels receive, while supplier power can raise '
               'their costs. More bookings alone do not tell us whether hotels retain more profit '
               'from each booking.',
               'Higher volume may help, but does not guarantee better margins. The effect depends '
               'on prices, costs and the amount of additional business.',
               'When a small number of suppliers serve much of the industry, their bargaining '
               'power can affect many hotels. Supplier costs therefore belong in the industry '
               'assessment.'],
  'key': 0,
  'source': 'Updated Session 3 deck, slides 5–6, 8–9; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
 {'block': 'Industry forces',
  'title': 'An alternative can affect prices before it is used',
  'concept': 'A substitute meets the same need differently. The threat of substitutes or new '
             'entrants can constrain prices before entry or switching occurs.',
  'scene': 'A company is negotiating airfares for employees attending routine meetings. It tells '
           'the airline that some meetings could instead be held by video call. Employees still '
           'take most of their flights, but the company uses this alternative to request lower '
           'fares.',
  'prompt': 'How can video meetings affect the airline even before many flights are cancelled?',
  'options': ['They cannot affect the airline until employees actually stop flying.',
              'They affect the airline only if the video-meeting provider starts operating flights '
              'itself.',
              'They offer another way to meet the business need, which can limit the fare the '
              'company is willing to pay.'],
  'feedback': ['A credible alternative can influence a customer’s willingness to pay before the '
               'customer switches. Actual cancellation is not required for pricing pressure.',
               'A substitute meets the underlying need differently. The provider does not need to '
               'become another airline: video meetings can replace some travel needed for '
               'communication.',
               'For these routine meetings, the need is communication with colleagues, rather than '
               'flying itself. Video calls offer a different way to meet that need and can '
               'constrain acceptable fares.'],
  'key': 2,
  'source': 'Updated Session 3 deck, slides 5, 8–9; Tiwana, Chapter 2. Applied situation is '
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
  'source': 'Updated Session 3 deck, slides 8–9; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
 {'block': 'Industry forces',
  'title': 'Entry without the old infrastructure',
  'concept': 'IT can lower entry barriers by allowing a firm to serve customers without the '
             'physical assets of an established business model. The new offering may also '
             'substitute for an existing one.',
  'scene': 'A new film service delivers movies through streaming. It does not need the shops or '
           'stocks of rental discs used by established video-rental chains. Customers can watch at '
           'home through either service.',
  'prompt': 'How does this digital model change the competitive pressure on video-rental chains?',
  'options': ['It reduces the need for traditional entry assets and offers customers a different '
              'way to obtain home entertainment.',
              'It affects rivalry only after the streaming firm builds a shop network comparable '
              'to the incumbents.',
              'It primarily improves the incumbents’ efficiency because films can now travel over '
              'the internet.'],
  'feedback': ['Streaming avoids some legacy investments needed for store-based rental, lowering '
               'those entry hurdles. It also substitutes for renting physical discs. Other entry '
               'requirements, such as content rights, still matter.',
               'The model’s significance is that it can serve the need without reproducing the old '
               'shop network. Entry pressure does not require identical assets.',
               'Incumbents may also adopt streaming, but the scenario describes an entrant with a '
               'different model. Its lower legacy burden and substitute offering can put '
               'incumbents under pressure.'],
  'key': 0,
  'source': 'Updated Session 3 deck, slides 8–9; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
 {'block': 'Industry forces',
  'title': 'Many accounts or a useful network?',
  'concept': 'Operational efficiency can protect margins. Network effects and deep customization '
             'can erect unconventional competitive barriers.',
  'scene': 'A tutoring marketplace has thousands of registered tutors, but most are inactive. A '
           'smaller rival has active tutors who cover many subjects and respond promptly. Students '
           'find suitable tutors more easily on the smaller platform.',
  'prompt': 'What would best show that a tutoring marketplace’s network makes it difficult for a '
            'new rival to compete?',
  'options': ['It has more registered tutor accounts, whether or not those tutors respond to '
              'students.',
              'It has spent more on its website than other tutoring marketplaces.',
              'More active, relevant tutors improve students’ chances of finding a suitable match, '
              'and a new rival would struggle to assemble an equally useful network.'],
  'feedback': ['Inactive accounts do not necessarily improve matching. A large registration count '
               'alone is not evidence of a useful network effect or an entry barrier.',
               'Website investment may improve the service, but spending alone does not establish '
               'that participants create value for one another.',
               'The network matters when useful participation improves the service for other '
               'users. If a rival cannot readily assemble comparable participation, that network '
               'can make entry harder.'],
  'key': 2,
  'source': 'Updated Session 3 deck, slides 8–9, 28; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
 {'block': 'Value chain',
  'title': 'Lower cost or greater customer value?',
  'concept': 'IT can reduce the cost of performing an activity or increase the value customers '
             'receive. The two effects can occur together, but require different evidence.',
  'scene': 'A service centre introduces diagnostic software that reduces technicians’ time per '
           'repair. It also introduces online appointment selection and progress updates, which '
           'customers say make the service more convenient.',
  'prompt': 'Which interpretation best distinguishes the two contributions?',
  'options': ['Both changes demonstrate differentiation because each uses digital technology.',
              'Faster diagnosis supports cost reduction; appointment choice and useful updates add '
              'customer value. Each claim needs evidence of its effect.',
              'Only faster diagnosis creates value because convenience does not reduce the service '
              'centre’s operating cost.'],
  'feedback': ['Digital technology alone does not establish differentiation. One change primarily '
               'reduces the resources used in a repair, while the other improves the customer '
               'experience.',
               'Repair time provides evidence for an efficiency contribution. Customer convenience '
               'provides evidence for added value. These routes can overlap, but buying either '
               'system does not by itself prove the result.',
               'Value-chain analysis considers both lower cost and benefits customers value. '
               'Convenience can add value even without a direct operating-cost reduction.'],
  'key': 1,
  'source': 'Updated Session 3 deck, slides 11–15; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
 {'block': 'Value chain',
  'title': 'Connecting steps or removing a layer?',
  'concept': 'Coordination uses information to connect activities within or across firms. '
             'Disintermediation changes the value-stream structure by bypassing an intermediary.',
  'scene': 'A supermarket shares store inventory with its existing suppliers so they can replenish '
           'shelves promptly. Separately, a manufacturer starts accepting customer orders directly '
           'online and bypasses its distributor.',
  'prompt': 'What is the most precise distinction between these changes?',
  'options': ['Inventory sharing improves coordination between existing participants; direct '
              'ordering changes the structure by bypassing an intermediary.',
              'Both are disintermediation because information now travels directly between firms.',
              'Both are coordination because the distributor’s activities disappear when customers '
              'order online.'],
  'feedback': ['The first connects existing activities more effectively. The second removes a '
               'participant from the route to the customer, although necessary activities may '
               'transfer to the manufacturer or another provider.',
               'A direct information link need not remove a participant. The supermarket retains '
               'its suppliers and improves replenishment coordination.',
               'Bypassing a distributor changes which firms perform activities. Its necessary work '
               'may remain, but the structural change goes beyond coordination.'],
  'key': 0,
  'source': 'Updated Session 3 deck, slides 12, 21; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
 {'block': 'Value chain',
  'title': 'Customer insight changes an activity',
  'concept': 'Applications combined with proprietary customer data can change decisions within a '
             'value-chain activity, reducing wasted effort or increasing customer value.',
  'scene': 'A hotel chain discovers that frequent local visitors, rather than its highest-spending '
           'occasional guests, produce more reliable profit. It changes its loyalty offers to '
           'reflect visit patterns and customer preferences instead of sending the same discount '
           'to everyone.',
  'prompt': 'What best explains the contribution of information systems to its marketing activity?',
  'options': ['The loyalty application creates the advantage because competitors cannot use '
              'similar software.',
              'Accumulating more guest records establishes an advantage even if the offers remain '
              'unchanged.',
              'Customer insight changes targeting and offers, potentially reducing wasted '
              'promotions and making relevant offers more valuable.'],
  'feedback': ['Competitors may obtain similar applications. The contribution comes from combining '
               'the application with customer knowledge and changed decisions.',
               'Records have potential value, but the scenario’s benefit comes from their use. '
               'Data volume alone does not establish better decisions or defensibility.',
               'This applies the logic of Tiwana’s casino example. Marketing decisions change in '
               'response to evidence, creating possible cost and value benefits that still need '
               'evaluation.'],
  'key': 2,
  'source': 'Updated Session 3 deck, slides 14–16; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
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
  'source': 'Updated Session 3 deck, slides 17–19, 21; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
 {'block': 'Value chain',
  'title': 'Music downloads and the changing distribution chain',
  'concept': 'Digitizing the offering enables digital delivery and can permit further changes in '
             'the value stream.',
  'scene': 'An independent musician replaces CDs sold through distributors and shops with music '
           'files sold through a download platform. The platform delivers the files online. The '
           'musician still pays a specialist agency to promote the music and help listeners '
           'discover it.',
  'prompt': 'What does this example show about digitization and intermediaries?',
  'options': ['Digital music delivery can remove physical distribution stages, while promotion '
              'intermediaries may remain if they add value.',
              'The download platform changes only the purchase process; the music still needs the '
              'same physical distribution stages as a CD.',
              'Once delivery is digital, retaining any promotion intermediary means the '
              'distribution model has failed.'],
  'feedback': ['Digitizing the offering allows delivery without manufacturing and moving CDs. It '
               'does not eliminate the need to reach listeners; an agency may still create value '
               'through promotion and discovery.',
               'In this scenario, both the offering and its delivery are digital. CD '
               'manufacturing, transport and shop handling are no longer required for these '
               'downloads.',
               'Digital delivery removes certain physical activities, not every activity in the '
               'value chain. An intermediary can still be worthwhile if its contribution justifies '
               'its cost.'],
  'key': 0,
  'source': 'Updated Session 3 deck, slides 20–21; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
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
  'source': 'Updated Session 3 deck, slides 23, 26; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
 {'block': 'Resource advantage',
  'title': 'The same application, different data',
  'concept': 'Useful networks and proprietary observations can strengthen applications, but value, '
             'rarity, imitation and equivalent alternatives still need assessment.',
  'scene': 'Two streaming services buy comparable recommendation software. One has years of '
           'detailed viewing histories and expertise in using them. A rival uses customer '
           'interviews and experiments to produce recommendations that customers find equally '
           'useful.',
  'prompt': 'What is the strongest assessment of the first service’s application–data combination?',
  'options': ['The viewing histories guarantee sustained advantage because competitors cannot buy '
              'identical records.',
              'The combination may improve decisions, but an equally effective alternative can '
              'challenge its ability to sustain advantage.',
              'Comparable software means the proprietary histories cannot contribute any business '
              'value.'],
  'feedback': ['Hard-to-copy data are relevant, but sustained advantage also depends on whether '
               'rivals can achieve equivalent value through other resources or capabilities.',
               'The application and data can be valuable together. However, the rival’s different '
               'route to equivalent customer benefit raises a substitution challenge under the '
               'litmus test.',
               'Common applications can create different results when combined with distinctive '
               'data and expertise. The issue is defensibility, rather than whether the data can '
               'have value.'],
  'key': 1,
  'source': 'Updated Session 3 deck, slides 23, 28; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'},
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
  'source': 'Updated Session 3 deck, slides 24, 27, 29; Tiwana, Chapter 2. Applied situation is '
            'illustrative.'}]

RETRY_HINTS = ['Separate the industry question, the activity question and the resource question.',
 'Consider both sides of each booking: what the hotel receives from the guest and what it pays to '
 'provide the stay.',
 'Ask what the company needs the trip to accomplish, and whether it can accomplish that purpose '
 'another way.',
 'Consider whose alternatives improve under each platform feature.',
 'Ask which assets the entrant can avoid, and whether customers can meet the same need in another '
 'way.',
 'Focus on the value active tutors create for students, and what a new rival would need to '
 'reproduce that value.',
 'Separate the resources needed to perform the activity from the benefit experienced by the '
 'customer.',
 'Check whether the same participants remain connected more effectively, or whether an '
 'intermediary is bypassed.',
 'Trace how the insight changes the marketing decision, rather than focusing only on the software '
 'or record count.',
 'Ask which activities disappear and which must still be performed by someone.',
 'Separate the work of physically moving CDs from the work of helping listeners discover the '
 'music.',
 'Distinguish business value, competitive parity and sustained advantage.',
 'Distinguish copying the same records from creating an equivalent customer benefit by another '
 'method.',
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



