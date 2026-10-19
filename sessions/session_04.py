"""Session 4: application-based concept revision. Standalone or imported; no external APIs or data files."""
import html
import streamlit as st

SESSION = 4

PREFIX = 'ism_s4'

STAGE_KEY = 'ism_s4_stage'

ANSWER_KEY = 'ism_s4_answers'

TITLE = 'Smart, connected products'

INTRO = ('Advise product and service managers on connected capabilities, technology choices, industry '
 'effects and the changes needed to deliver customer value.')

SUMMARY_TITLE = 'Your Connected-Product Review'

TAKEAWAYS = ['A connection alone does not establish control, optimization or autonomy.',
 'Product hardware, software, cloud layers and business integration solve different problems.',
 'Capability and product-versus-cloud choices follow customer value and operating requirements.',
 'Connected products can strengthen or weaken competitive forces through different mechanisms.',
 'Data rights, ecosystem choices and organizational complements support the chosen business model.']

GLOSSARY = {'Monitoring': 'Observing product condition, environment, operation and use, including alerts.',
 'Control': 'Commands or software change product functions or personalize operation.',
 'Optimization': 'Algorithms use monitoring and control to improve performance or support '
                 'predictive service.',
 'Autonomy': 'Combined capabilities enable operation and adaptation with less direct intervention.',
 'Product cloud': 'Remote data management, development platform, analytics and smart-product '
                  'applications.',
 'System of systems': 'Linked product systems support a broader customer outcome.',
 'Complement': 'A supporting skill, process, role or arrangement needed to realize product value.'}

READING = ('Assigned sources: Session 04 deck; Porter and Heppelmann (2014), How Smart, Connected Products '
 'Are Transforming Competition, Harvard Business Review, November 2014.')

CONCEPT_MAP = ('\n'
 '| Concept | Application question | Reading trail |\n'
 '|---|---|---|\n'
 '| Components and stack | Which layer is missing between observation and useful action? | Session '
 '04, slides 3–6; article technology-stack exhibit |\n'
 '| Four capabilities | What does the product observe, change, improve or do independently? | '
 'Slides 9–15; article capabilities exhibit |\n'
 '| Product versus cloud | Which functions need local response and which benefit from remote '
 'processing? | Slide 18; article strategic choices |\n'
 '| Industry boundaries and Five Forces | Who creates and captures value as the solution broadens? '
 '| Slides 16–17; article industry-structure discussion, pp. 10–12 |\n'
 '| Ecosystem and complements | Which interfaces, skills, partners and decision rights support the '
 'promise? | Slide 19; article strategic choices |\n'
 '| Data, channels and business model | What rights and operating changes are needed to deliver '
 'the chosen service? | Slides 20–22; article strategic choices |\n')

DECISIONS = [{'block': 'Product and technology stack',
  'title': 'Connected, but unable to act',
  'concept': 'Physical components perform the function, smart components process information, and '
             'connectivity exchanges it. A connection alone does not create every capability.',
  'scene': 'A cold-store operator connects temperature sensors to a dashboard. Managers receive '
           'alerts, but the refrigeration unit cannot accept commands from the dashboard. The '
           'supplier describes this as remote temperature control.',
  'prompt': 'What additional evidence would support the supplier’s control claim?',
  'options': ['An authenticated command path that makes the unit change its operation.',
              'More frequent alerts delivered to the manager’s phone.',
              'A longer history of temperature readings stored on the dashboard.'],
  'feedback': ['Control requires software or commands to alter product functions. Sensors and a '
               'dashboard establish monitoring, while a functioning command path would support '
               'control.',
               'Faster notification improves monitoring. A notification still requires someone or '
               'something to change the product.',
               'History improves visibility and analysis, but does not make the unit act.'],
  'key': 0,
  'source': 'Session 04 deck, slides 3–4, 9–11; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, What Are Smart, Connected Products? and What '
            'Can Smart, Connected Products Do?. The business situation is illustrative.'},
 {'block': 'Product and technology stack',
  'title': 'A cloud dashboard that cannot find history',
  'concept': 'The product database aggregates and manages observations; analytics interprets them; '
             'applications deliver the service. Different layers solve different problems.',
  'scene': 'A pump maker has working sensors, communication and an app. Each reading overwrites '
           'the previous one. Managers want to compare operating patterns before past failures, '
           'and propose adding a more attractive dashboard.',
  'prompt': 'Which change addresses the immediate obstacle to that comparison?',
  'options': ['Retain and organize time-stamped product histories before developing the '
              'comparison.',
              'Increase the number of user accounts without changing how readings are stored.',
              'Redesign the app’s charts while continuing to overwrite old observations.'],
  'feedback': ['The proposed comparison needs historical observations. The product data layer must '
               'retain and organize them; analytics and the application can then use those '
               'records.',
               'Account access does not create historical evidence. It addresses a different part '
               'of the stack.',
               'A clearer interface cannot recover observations that were discarded. Storage and '
               'data management are the immediate gap.'],
  'key': 0,
  'source': 'Session 04 deck, slides 4–6; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, The New Technology Stack. The business '
            'situation is illustrative.'},
 {'block': 'Product and technology stack',
  'title': 'Useful alerts, missed repairs',
  'concept': 'Product data creates value when insight changes work. Integration connects product '
             'information with business processes, while roles determine who acts.',
  'scene': 'A connected compressor predicts service needs accurately. Alerts remain in the product '
           'app, while the service team schedules visits in a separate system. No one owns the '
           'handover and customers still suffer avoidable downtime.',
  'prompt': 'Which response most directly connects the prediction to business value?',
  'options': ['Connect alerts to service work orders and assign responsibility for responding.',
              'Add more sensors so the same alert can include more measurements.',
              'Set a more ambitious uptime target without changing the handover.'],
  'feedback': ['Integration and clear responsibility turn an insight into a service action. '
               'Predictive accuracy alone does not establish reduced downtime.',
               'More measurements may improve predictions, but the stated failure is acting on an '
               'already useful alert.',
               'A target alone does not change the workflow or decision rights that currently '
               'leave alerts unattended.'],
  'key': 0,
  'source': 'Session 04 deck, slides 5–6, 19; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, The New Technology Stack and strategy '
            'implications. The business situation is illustrative.'},
 {'block': 'Capabilities',
  'title': 'A recommendation is not autonomous operation',
  'concept': 'Monitoring observes, control changes functions, optimization improves performance, '
             'and autonomy combines capabilities to operate with less direct intervention.',
  'scene': 'A vacuum maps each room and recommends an efficient cleaning route. It starts only '
           'after the owner approves that route. The product team claims that an efficient '
           'recommendation proves fully autonomous cleaning.',
  'prompt': 'Which assessment is best supported by the described behavior?',
  'options': ['Because the owner approves the route, the product can only monitor its '
              'surroundings.',
              'Any use of a route algorithm establishes autonomous operation.',
              'The route recommendation demonstrates optimization; it does not by itself establish '
              'independent operation.'],
  'feedback': ['Human approval does not erase optimization. These capabilities can coexist with '
               'different degrees of human involvement.',
               'An algorithm can recommend an improvement without independently operating the '
               'product. Examine the actual decision and action.',
               'The algorithm improves the proposed operation, while the owner retains the '
               'initiation decision. Further evidence is needed for the broader autonomy claim.'],
  'key': 2,
  'source': 'Session 04 deck, slides 12–15; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, What Can Smart, Connected Products Do?. The '
            'business situation is illustrative.'},
 {'block': 'Product and technology choices',
  'title': 'A safety function during a network failure',
  'concept': 'Placing functionality in the product or cloud involves response time, reliability, '
             'upgrade needs and the operating setting.',
  'scene': 'A factory valve must close immediately if pressure becomes unsafe. Internet service is '
           'intermittent. Weekly performance analysis benefits from comparing data across many '
           'sites.',
  'prompt': 'Which division of functions best fits these requirements?',
  'options': ['Run both functions only in the cloud to keep all decision logic in one place.',
              'Keep every function local, including all cross-site comparisons, because the '
              'connection sometimes fails.',
              'Keep the immediate safety response local and use the cloud for cross-site '
              'analysis.'],
  'feedback': ['A central location for logic does not meet the stated requirement during an '
               'outage. Network dependence matters for the safety function.',
               'The safety constraint does not rule out cloud value for a different, less '
               'time-sensitive task. Allocate each function according to its requirements.',
               'The safety action needs a dependable local response. Aggregated cloud analysis can '
               'improve longer-term decisions without making the immediate action depend on '
               'connectivity.'],
  'key': 2,
  'source': 'Session 04 deck, slides 4–5, 18; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, How much functionality should be embedded in '
            'the product versus the cloud?. The business situation is illustrative.'},
 {'block': 'Product and technology choices',
  'title': 'A feature that customers will not fund',
  'concept': 'A firm selects connected capabilities according to customer value relative to cost '
             'and competitive positioning, rather than maximizing the feature count.',
  'scene': 'A maker of basic water pumps can add an expensive autonomous scheduling feature. Small '
           'shops value simple fault alerts, while large plants need scheduling. The supplier '
           'suggests adding the full feature bundle to every pump.',
  'prompt': 'Which product policy best applies the article’s strategic choice?',
  'options': ['Add the full bundle to every model because autonomy is the highest capability.',
              'Offer fault alerts broadly and assess a priced scheduling option for the segment '
              'that values it.',
              'Remove all connected features until every customer wants the same bundle.'],
  'feedback': ['More capability can raise cost without creating enough value for the target '
               'customer. Autonomy is an option, not a universal objective.',
               'This matches capability and cost to customer needs. The scheduling option still '
               'needs evidence of willingness to pay and feasible delivery.',
               'Different needs support segmentation. They do not imply that the simpler useful '
               'capability should be withheld.'],
  'key': 1,
  'source': 'Session 04 deck, slides 15, 18, 22; Porter and Heppelmann (2014), How Smart, '
            'Connected Products Are Transforming Competition, Which smart, connected product '
            'capabilities and features should the company pursue?. The business situation is '
            'illustrative.'},
 {'block': 'Industry structure',
  'title': 'Selling a tractor or managing the farm?',
  'concept': 'Related connected products can form a product system; linking equipment with '
             'weather, irrigation and seed systems broadens the basis of competition further.',
  'scene': 'A tractor manufacturer first coordinates its tractors and harvesters. A new platform '
           'then combines multiple equipment brands with weather forecasts, irrigation and seed '
           'decisions. Farmers compare the resulting farm productivity.',
  'prompt': 'What is the most useful strategic interpretation?',
  'options': ['Connecting more systems necessarily makes every equipment maker’s margins higher.',
              'The platform is simply a more advanced tractor and the relevant competitors remain '
              'unchanged.',
              'Competition is expanding toward a system of systems, so equipment makers must '
              'reassess partners, rivals and the value proposition.'],
  'feedback': ['Broader value creation does not determine who captures the value. Rivalry, '
               'bargaining power and coordination costs still matter.',
               'The customer now evaluates coordinated farm outcomes across several domains, '
               'rather than only the tractor’s features.',
               'The scope of the customer solution and the participants changes. A tractor maker '
               'may face a platform competitor or need to cooperate with it.'],
  'key': 2,
  'source': 'Session 04 deck, slides 16; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, Redefining Industry Boundaries. The business '
            'situation is illustrative.'},
 {'block': 'Industry structure',
  'title': 'Higher barriers, but an unexpected entrant',
  'concept': 'Connected products can raise entry barriers through fixed costs and accumulated '
             'data, while a different business model can bypass incumbent assets.',
  'scene': 'An equipment maker has years of machine data and a large installed base. A software '
           'firm proposes a decision service using customers’ existing equipment across several '
           'brands, without manufacturing machines itself.',
  'prompt': 'How should the incumbent assess entry pressure?',
  'options': ['Its data may deter a similar manufacturer, but a cross-brand service can bypass '
              'part of the old asset requirement.',
              'Its installed base means the software firm cannot become a relevant competitor.',
              'The software firm’s entry means accumulated data never creates entry barriers.'],
  'feedback': ['Different entry models face different hurdles. Incumbent data can protect one '
               'position while a service entrant competes on a broader solution.',
               'Protection against replicating a machine business does not guarantee protection '
               'against a different way to serve the customer.',
               'Two mechanisms can operate together. A bypass does not prove that data is '
               'worthless to every entrant or incumbent.'],
  'key': 0,
  'source': 'Session 04 deck, slides 17; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, Threat of new entrants. The business situation '
            'is illustrative.'},
 {'block': 'Industry structure',
  'title': 'Customer data can change power in either direction',
  'concept': 'Personalization and accumulated history can raise switching costs; performance '
             'transparency and some service models can increase buyer power.',
  'scene': 'A machine service learns each factory’s settings over time. Separately, the buyer '
           'obtains comparable performance reports and can move between suppliers through a '
           'short-term usage contract.',
  'prompt': 'Which conclusion is most defensible?',
  'options': ['History can make switching costly, while comparability and flexible contracting '
              'improve the buyer’s alternatives.',
              'Both changes necessarily reduce buyer power because they use connected-product '
              'data.',
              'Shorter contracts eliminate all value from personalization and operating history.'],
  'feedback': ['Assess both mechanisms and their strength in the actual relationship. Do not '
               'equate more customer data with a guaranteed fall in buyer power.',
               'Data can create differentiation but also make comparison easier. A single '
               'direction does not follow from connectivity.',
               'Personalization may still be valuable. Better alternatives can offset its '
               'bargaining effect without removing its operating benefit.'],
  'key': 0,
  'source': 'Session 04 deck, slides 17; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, Bargaining power of buyers. The business '
            'situation is illustrative.'},
 {'block': 'Industry structure',
  'title': 'Fewer physical parts, more technology dependence',
  'concept': 'Connected products can weaken traditional component suppliers while introducing '
             'powerful suppliers of the technology stack.',
  'scene': 'A manufacturer replaces several specialized mechanical controls with software. It then '
           'depends on a proprietary operating platform supplied by one technology vendor, which '
           'raises license charges.',
  'prompt': 'What changed in supplier power?',
  'options': ['The license increase proves that connected products cannot create value for '
              'customers.',
              'Some mechanical suppliers lost leverage, but a new technology supplier may capture '
              'more value.',
              'Supplier power disappeared because software replaced physical components.'],
  'feedback': ['A supplier’s ability to capture value is distinct from whether the product creates '
               'value. Examine both.',
               'The relevant suppliers now include software and platform providers. Customer value '
               'may grow even while the manufacturer captures a smaller share.',
               'Changing the input mix can redistribute bargaining power rather than eliminate '
               'dependence on suppliers.'],
  'key': 1,
  'source': 'Session 04 deck, slides 17; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, Bargaining power of suppliers. The business '
            'situation is illustrative.'},
 {'block': 'Industry structure',
  'title': 'Two threats to the profit forecast',
  'concept': 'Differentiation can move rivalry away from price. High fixed costs, feature races '
             'and substitutes can still pressure profitability.',
  'scene': 'Connected machines command a premium, but rival firms keep adding costly features. At '
           'the same time, a shared-usage service allows customers to use fewer machines more '
           'intensively. A director predicts that connectivity guarantees higher industry profits.',
  'prompt': 'Which challenge best addresses that prediction?',
  'options': ['Feature spending may erode margins, and shared usage may substitute for ownership '
              'even if customers value the connected features.',
              'The premium is sufficient evidence that higher profits will continue regardless of '
              'costs and ownership patterns.',
              'Shared usage only affects buyers’ convenience, so it has no bearing on equipment '
              'demand.'],
  'feedback': ['The scenario combines rivalry through a feature race with substitution for '
               'ownership. Added value and higher unit prices do not establish higher industry '
               'profit.',
               'A price premium must be weighed against development costs and changes in demand. '
               'It is not a profit guarantee.',
               'Higher utilization can change the number of machines customers need to own. That '
               'is relevant to the underlying business.'],
  'key': 0,
  'source': 'Session 04 deck, slides 17, 21–22; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, Rivalry among competitors and Threat of '
            'substitutes. The business situation is illustrative.'},
 {'block': 'Ecosystem and organization',
  'title': 'Interoperability without unrestricted access',
  'concept': 'Open versus closed systems involves interoperability, adoption and control. Opening '
             'selected interfaces does not require giving every partner unrestricted access.',
  'scene': 'A smart-building supplier wants its equipment to work with other brands. Its service '
           'team worries that publishing any interface means outsiders must be allowed to alter '
           'every control setting.',
  'prompt': 'Which approach best addresses both concerns?',
  'options': ['Allow all partners to change all settings so adoption can grow quickly.',
              'Expose selected documented interfaces with authentication, permissions and clear '
              'operating rules.',
              'Keep every interface closed, since interoperability requires abandoning control.'],
  'feedback': ['Adoption does not justify removing control over sensitive functions. Define the '
               'permitted interactions.',
               'Selective interoperability can support a wider ecosystem while retaining explicit '
               'control over access and operation. The appropriate boundary depends on strategy.',
               'A firm can design a degree of openness. The choice is not limited to total closure '
               'or unrestricted access.'],
  'key': 1,
  'source': 'Session 04 deck, slides 19–20; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, Should the company pursue an open or closed '
            'system?. The business situation is illustrative.'},
 {'block': 'Ecosystem and organization',
  'title': 'Buying the cloud without outsourcing the advantage',
  'concept': 'Build-versus-outsource choices balance speed and expertise against control and '
             'learning in activities that differentiate the firm.',
  'scene': 'A pump company can buy standard hosting quickly. Its distinctive promise is diagnosing '
           'local operating failures accurately. An outsourcing proposal would transfer both '
           'hosting and all diagnostic expertise to one vendor.',
  'prompt': 'Which alternative best protects the distinctive promise while using specialist '
            'suppliers?',
  'options': ['Outsource diagnosis solely because it is technically difficult, without considering '
              'its strategic importance.',
              'Consider specialist hosting while retaining the diagnostic knowledge and '
              'capabilities central to the promise.',
              'Build every technology layer internally before launching any service.'],
  'feedback': ['Difficulty is relevant to feasibility, but cannot alone settle the strategic '
               'boundary. Outsourcing the differentiator can weaken the promised advantage.',
               'The firm can source standard layers while preserving control and learning where '
               'they create distinctive customer value. Governance of the supplier relationship '
               'still matters.',
               'Internal development of every layer can delay the service and duplicate standard '
               'capabilities. Differentiation does not require owning the full stack.'],
  'key': 1,
  'source': 'Session 04 deck, slides 19; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, Should the company develop the full set of '
            'capabilities internally or outsource?. The business situation is illustrative.'},
 {'block': 'Data and business model',
  'title': 'Collecting everything before deciding why',
  'concept': 'Data selection follows the intended customer benefit, collection cost and risks. '
             'Data ownership, access and permitted use require explicit choices.',
  'scene': 'A connected fitness-equipment maker needs usage and fault data for preventive service. '
           'It also proposes collecting unrelated personal information for possible future sale, '
           'although customer permissions and commercial value are unclear.',
  'prompt': 'Which policy best fits the article’s data choices?',
  'options': ['Treat ownership of the equipment’s software as automatic entitlement to every '
              'customer observation.',
              'Collect all available data now because storage is inexpensive and later uses may '
              'emerge.',
              'Specify the service purpose and necessary data, clarify rights and access, and '
              'evaluate external monetization separately.'],
  'feedback': ['Software ownership does not by itself resolve customer data rights. Those '
               'arrangements need clarification.',
               'Storage is only one cost. Relevance, security, privacy and the customer '
               'relationship can constrain value.',
               'Useful data, costs, rights and trust must be considered together. A possible '
               'future sale does not settle permission or justify collecting unrelated '
               'information.'],
  'key': 2,
  'source': 'Session 04 deck, slides 20; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, What data must the company capture? Who should '
            'own the data? Should the company monetize data externally?. The business situation is '
            'illustrative.'},
 {'block': 'Data and business model',
  'title': 'A direct relationship still needs a repair network',
  'concept': 'Connected service can change channel roles. Bypassing an intermediary does not '
             'remove every activity that customers need.',
  'scene': 'A manufacturer can diagnose faults and update software remotely. It plans to remove '
           'local service partners, although a quarter of faults require a physical part '
           'replacement and customers need rapid repair.',
  'prompt': 'Which channel decision best follows from these facts?',
  'options': ['Remove the local partners because a direct data connection replaces every service '
              'activity.',
              'Redesign partner roles around physical repairs while using direct connections for '
              'remote service and insight.',
              'Keep the existing channel entirely unchanged because any direct interaction harms '
              'partners.'],
  'feedback': ['Diagnosis and software updates do not physically replace parts. Required '
               'activities must still have an owner.',
               'This allocates work according to what connectivity changes and what still requires '
               'proximity. It also requires managing incentives and the partner relationship.',
               'The channel can evolve rather than remain fixed. Direct services and local repair '
               'can complement one another.'],
  'key': 1,
  'source': 'Session 04 deck, slides 21; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, Should the company disintermediate '
            'distribution channels or service networks?. The business situation is illustrative.'},
 {'block': 'Data and business model',
  'title': 'Selling uptime changes the work',
  'concept': 'A service or usage model changes incentives and responsibilities. Organizational '
             'complements connect monitoring and control to the promised customer outcome.',
  'scene': 'A compressor maker moves from selling equipment to charging for guaranteed '
           'availability. It has remote alerts, but rewards service managers only for minimizing '
           'visits. Repeated warnings go unaddressed until breakdowns occur.',
  'prompt': 'What is the strongest managerial response?',
  'options': ['Rename equipment sales as a subscription without changing service priorities.',
              'Sell the alert data to another firm before addressing the service failures.',
              'Align service incentives, response processes and decision rights with the '
              'availability promise.'],
  'feedback': ['Recurring billing alone does not deliver availability. The operating model must '
               'support the promise.',
               'External monetization does not fix the failure to meet the core customer promise.',
               'The business model shifts the provider’s incentive toward sustained performance. '
               'Roles and processes must turn alerts into timely preventive action.'],
  'key': 2,
  'source': 'Session 04 deck, slides 19, 21–22; Porter and Heppelmann (2014), How Smart, Connected '
            'Products Are Transforming Competition, Should the company change its business model? '
            'and strategy implications. The business situation is illustrative.'}]

RETRY_HINTS = ['Distinguish information about the unit from a change in what the unit does.',
 'Ask whether the evidence needed for the analysis still exists.',
 'Trace the alert from detection to an actual maintenance visit.',
 'Identify which decision the algorithm makes and which decision still belongs to the owner.',
 'Separate the time-critical action from the analysis that can wait for a connection.',
 'Compare the benefit and cost for each customer segment.',
 'Ask what outcome the customer now buys and which systems contribute to it.',
 'Would the entrant need to reproduce the incumbent’s factory and installed base?',
 'Separate what makes the relationship valuable from what makes alternatives easier to compare or '
 'choose.',
 'Track which inputs remain replaceable and which vendor has become difficult to substitute.',
 'Examine development costs and the number of units customers need, as well as selling price.',
 'Distinguish allowing a defined interaction from surrendering all control.',
 'Identify the work that is standard and the work that makes the offer distinctive.',
 'Ask what decision the data supports and what rights allow that use.',
 'Distinguish removing a participant from ensuring its necessary activities still happen.',
 'Compare the stated uptime promise with the behavior encouraged by current incentives.']

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
        st.caption(READING)
        st.markdown(CONCEPT_MAP)
        if stage < count:
            st.caption("Reading trail for this decision: " + DECISIONS[stage]['source'])
        st.markdown("**Concept reminders**")
        for term, definition in GLOSSARY.items():
            st.markdown(f"**{term}:** {definition}")
        st.caption("These illustrative revision situations apply concepts from the assigned readings; consult the course copies for the full arguments.")

def render_session_04():
    _render()

if __name__ == "__main__":
    st.set_page_config(page_title="ISM LAB · Session 4", page_icon="📘", layout="wide")
    render_session_04()



