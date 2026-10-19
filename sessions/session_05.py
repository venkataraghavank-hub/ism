"""Session 5: application-based concept revision. Standalone or imported; no external APIs or data files."""
import html
import streamlit as st

SESSION = 5

PREFIX = 'ism_s5'

STAGE_KEY = 'ism_s5_stage'

ANSWER_KEY = 'ism_s5_answers'

TITLE = 'Cloud computing'

INTRO = ('Choose service arrangements and apply the seven cloud capabilities to business needs. Test the '
 'link from technical possibility to operating outcomes, costs and managerial responsibility.')

SUMMARY_TITLE = 'Your Cloud Decision Review'

TAKEAWAYS = ['Service and deployment choices answer different questions; governance remains with the firm.',
 'The seven capabilities describe what cloud enables, not automatic business benefits.',
 'Location independence differs from sourcing independence; portability includes meaning as well '
 'as records.',
 'Technical elasticity and commercial flexibility must both be checked.',
 'Evaluate the whole system, full cost, recovery needs and adoption before claiming value.']

GLOSSARY = {'Controlled interface': 'A defined, governed software interface through which services can be '
                         'reused.',
 'Location independence': 'A caller accesses a service without needing its physical location; '
                          'placement constraints still apply.',
 'Sourcing independence': 'The ability to change service sources with usable data, metadata and '
                          'interfaces.',
 'Ubiquitous access': 'Useful service access across devices and locations.',
 'Virtual business environment': 'Integrated applications, tools and process context supporting a '
                                 'business capability.',
 'Addressability and traceability': 'Identifying services and users and recording their usage and '
                                    'history.',
 'Rapid elasticity': 'Rapid expansion and contraction of resource use to match demand.',
 'IaaS / PaaS / SaaS': 'Infrastructure, an application platform or a finished application, with '
                       'different management boundaries.'}

READING = ('Assigned sources: Session 05 deck; Iyer and Henderson (2010), Preparing for the Future: '
 'Understanding the Seven Capabilities of Cloud Computing, MIS Quarterly Executive 9(2), 2010, pp. '
 '117–131. Service/deployment models and the NammaMart exercises follow the teaching deck.')

CONCEPT_MAP = ('\n'
 '| Concept | Application question | Reading trail |\n'
 '|---|---|---|\n'
 '| Foundations | Is capacity actually pooled, accessible and rapidly provisioned? | Session 05, '
 'slides 4–5 |\n'
 '| Service and deployment models | Who manages what, and who uses each infrastructure? | Slides '
 '7–8, 16–17 |\n'
 '| Controlled interface | Can partners rely on defined service interactions and change rules? | '
 'Slide 11; article capability 1 |\n'
 '| Location and sourcing independence | Can a service move physically or between providers '
 'without losing the required business capability? | Slides 11–12; article capabilities 2–3 |\n'
 '| Ubiquitous access and virtual business environments | Can people use services and carry out '
 'integrated work in their actual setting? | Slides 12–13; article capabilities 4–5 |\n'
 '| Addressability and traceability | Can use be identified, attributed and audited? | Slide 13; '
 'article capability 6 |\n'
 '| Rapid elasticity | Do resources and commercial terms match changing demand? | Slides 13–15; '
 'article capability 7 |\n'
 '| Value, adoption and whole-system trade-offs | Does the operating change justify full cost and '
 'meet assurance needs? | Slides 14–15, 18, 20–21; article managerial implications |\n')

DECISIONS = [{'block': 'Cloud foundations',
  'title': 'Renting a server is not the whole story',
  'concept': 'Cloud combines network access, pooled resources and rapid provisioning or release. '
             'Measured usage supports management, but the contract determines charges.',
  'scene': 'A retailer moves a server to an outside provider. Capacity changes still need a '
           'six-week purchase order, and the retailer pays for a fixed peak allocation all year. '
           'Its CEO expects immediate elasticity savings merely because the server is off site.',
  'prompt': 'Which question should the team investigate first?',
  'options': ['Whether employees can see the provider’s physical server building.',
              'Whether the supplier uses the word cloud in its contract.',
              'Whether resources and charges can actually adjust when workload changes.'],
  'feedback': ['Knowing the physical building is not the mechanism behind matching capacity to '
               'demand.',
               'A label does not establish provisioning behavior or economic flexibility.',
               'The expected benefit depends on the operating capability and commercial terms. '
               'Off-site hosting alone does not establish rapid elasticity or pay-for-use '
               'savings.'],
  'key': 2,
  'source': 'Session 05 deck, slides 4–5, 10, 15; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Rapid Elasticity. '
            'The business situation and any numbers are illustrative.'},
 {'block': 'Cloud foundations',
  'title': 'Separate environments on shared hardware',
  'concept': 'Virtualization separates computing environments; multitenancy shares resources among '
             'tenants. These mechanisms need isolation and management.',
  'scene': 'A provider runs several customers’ separate virtual machines on shared physical hosts. '
           'A buyer concludes that because each customer has its own virtual machine, no physical '
           'resources are shared and access controls are unnecessary.',
  'prompt': 'Which response best diagnoses the misconception?',
  'options': ['Separate virtual environments can share physical resources; isolation and access '
              'controls still matter.',
              'A virtual machine always means one physical host is reserved for one customer.',
              'Sharing hardware means every customer must be allowed to read every other '
              'customer’s files.'],
  'feedback': ['Virtual separation and physical pooling can coexist. The arrangement does not '
               'remove the need to enforce tenant boundaries.',
               'A virtual environment is not proof of a dedicated physical host. That would depend '
               'on a specific hosting arrangement.',
               'Resource pooling is compatible with enforced separation. Sharing infrastructure is '
               'not the same as sharing access to data.'],
  'key': 0,
  'source': 'Session 05 deck, slides 4–5; Iyer and Henderson (2010), Preparing for the Future: '
            'Understanding the Seven Capabilities of Cloud Computing, cloud foundations; the '
            'deck’s enabling-technology discussion. The business situation and any numbers are '
            'illustrative.'},
 {'block': 'Service and deployment choices',
  'title': 'Choosing which tasks to hand over',
  'concept': 'IaaS, PaaS and SaaS allocate different operating tasks to the provider. The firm '
             'still decides how the service supports work and who can use it.',
  'scene': 'A small team wants to deploy its own application code but avoid administering '
           'virtual-machine operating systems. It does not want to replace the application with a '
           'finished third-party product.',
  'prompt': 'Which choice most closely matches that division of work?',
  'options': ['A finished online application that replaces the team’s code.',
              'A virtual machine on which the team administers the operating system.',
              'A managed application platform that runs the team’s code and manages the underlying '
              'runtime and infrastructure.'],
  'feedback': ['That may fit another need, but it does not meet the stated desire to deploy the '
               'team’s own application.',
               'That offers infrastructure, but leaves the operating-system task the team wants to '
               'hand over.',
               'This is the PaaS pattern. The team still owns its code, application behavior and '
               'appropriate access configuration.'],
  'key': 2,
  'source': 'Session 05 deck, slides 7, 16–17; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, cloud service '
            'context; the deck’s service-model demonstrations. The business situation and any '
            'numbers are illustrative.'},
 {'block': 'Service and deployment choices',
  'title': 'A finished service still has a customer owner',
  'concept': 'Using a finished application transfers many operating tasks, but does not transfer '
             'the customer’s governance and adoption decisions.',
  'scene': 'A firm subscribes to a ready-to-use expense system. An employee leaves, but no one '
           'removes their access. The manager says account ownership belongs entirely to the '
           'software supplier because this is SaaS.',
  'prompt': 'Who should address the failure described?',
  'options': ['The supplier alone, because it must know every staffing change at the customer.',
              'No one needs to act if the provider maintains its servers correctly.',
              'The firm must assign responsibility for account access and coordinate provisioning '
              'or removal through the service.'],
  'feedback': ['The customer must communicate and govern its personnel and permissions. Supplier '
               'infrastructure management does not establish awareness of staffing changes.',
               'A well-maintained server does not make an inappropriate user permission '
               'appropriate.',
               'The provider may offer controls or integration, but the firm must ensure that '
               'access reflects business roles. SaaS does not remove governance responsibility.'],
  'key': 2,
  'source': 'Session 05 deck, slides 7, 15, 17; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, managerial '
            'implications; service responsibilities in the deck. The business situation and any '
            'numbers are illustrative.'},
 {'block': 'Service and deployment choices',
  'title': 'Exclusive use need not mean on premises',
  'concept': 'Deployment models describe the user community and the arrangement of cloud '
             'infrastructures, rather than simply whether equipment is inside a company building.',
  'scene': 'A provider operates a cloud environment exclusively for one manufacturer at the '
           'provider’s facility. The manufacturer’s team labels it public cloud solely because it '
           'is outside its own premises.',
  'prompt': 'Which classification best follows the stated arrangement?',
  'options': ['Private cloud, because use is exclusive to that organization, even though a '
              'provider operates it off site.',
              'Community cloud, because the provider employs people outside the manufacturer.',
              'Public cloud, because any externally operated infrastructure is public.'],
  'feedback': ['Exclusive organizational use is the relevant distinction. Physical location alone '
               'does not determine the deployment model.',
               'A community arrangement serves organizations with shared requirements. A '
               'supplier’s staff do not by themselves create that community.',
               'Public use and external operation are different concepts. The stated environment '
               'is not open to the general public.'],
  'key': 0,
  'source': 'Session 05 deck, slides 8; Iyer and Henderson (2010), Preparing for the Future: '
            'Understanding the Seven Capabilities of Cloud Computing, deployment context; the '
            'deck’s deployment-model definitions. The business situation and any numbers are '
            'illustrative.'},
 {'block': 'Service and deployment choices',
  'title': 'Two subscriptions or an integrated hybrid?',
  'concept': 'Hybrid deployment connects distinct cloud infrastructures for portability or '
             'coordinated use. Multiple contracts alone do not establish that integration.',
  'scene': 'A firm uses one public cloud and an exclusive private cloud. Their data and workloads '
           'cannot move between them and no coordinated process connects the environments. A '
           'director calls this proof of a working hybrid design.',
  'prompt': 'What evidence is missing from that claim?',
  'options': ['Both providers’ logos appearing on the same procurement presentation.',
              'A defined connection that enables the intended portability or coordinated use '
              'across the distinct clouds.',
              'A guarantee that the firm owns every physical server in both environments.'],
  'feedback': ['Purchasing services does not demonstrate operational integration.',
               'The deck’s hybrid definition involves distinct infrastructures connected for a '
               'purpose. The design needs evidence that the required interaction works.',
               'Physical ownership is not the defining requirement for hybrid deployment.'],
  'key': 1,
  'source': 'Session 05 deck, slides 8, 15; Iyer and Henderson (2010), Preparing for the Future: '
            'Understanding the Seven Capabilities of Cloud Computing, deployment context; the '
            'deck’s hybrid definition. The business situation and any numbers are illustrative.'},
 {'block': 'Seven cloud capabilities',
  'title': 'An interface that partners can depend on',
  'concept': 'Controlled interfaces define reusable interactions and how third parties may use '
             'them. API governance includes permissions and change management.',
  'scene': 'An order service exposes a documented API to partners. A new release unexpectedly '
           'changes the meaning of a field. Partners can still connect but now book deliveries '
           'incorrectly.',
  'prompt': 'Which action best strengthens the controlled-interface capability?',
  'options': ['Define interface versions, permitted use and a managed change process with affected '
              'partners.',
              'Allow each partner to edit the provider’s production database directly.',
              'Replace the API address with the underlying server’s physical location.'],
  'feedback': ['A useful interface needs stable expectations and governance, not merely '
               'connectivity. Managed evolution protects reuse and coordination.',
               'Bypassing the interface removes an important boundary and does not resolve shared '
               'expectations safely.',
               'Physical location does not resolve the broken service contract or field meaning.'],
  'key': 0,
  'source': 'Session 05 deck, slides 10–11, 18; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Controlled '
            'Interface. The business situation and any numbers are illustrative.'},
 {'block': 'Seven cloud capabilities',
  'title': 'Same service address, a different physical region',
  'concept': 'Location independence hides physical placement from callers. It does not remove '
             'requirements governing where data resides or who can access it.',
  'scene': 'A provider moves a data service to a different region while keeping its address '
           'unchanged. The application works without modification. The firm’s contract requires '
           'processing in a designated region.',
  'prompt': 'What should the manager conclude?',
  'options': ['The application demonstrates location independence, but the placement still needs '
              'to satisfy the agreed requirement.',
              'The move demonstrates sourcing independence because the physical location changed.',
              'A stable service address proves that regional obligations have been met.'],
  'feedback': ['Technical decoupling from location does not waive a contractual or governance '
               'constraint. Both functional continuity and permitted placement matter.',
               'The provider has not changed. Sourcing independence concerns the ability to switch '
               'sources, a different question.',
               'The address tells the application how to reach the service, not whether its '
               'underlying location meets the agreement.'],
  'key': 0,
  'source': 'Session 05 deck, slides 10–11, 15; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Location '
            'Independence. The business situation and any numbers are illustrative.'},
 {'block': 'Seven cloud capabilities',
  'title': 'A CSV export that loses the relationships',
  'concept': 'Sourcing independence requires usable portability, including data, metadata and '
             'relevant interfaces or procedures. An export button alone is insufficient.',
  'scene': 'A CRM vendor offers an export of customer names and phone numbers. It excludes '
           'interaction histories, field definitions and links between customer and service '
           'records. A new vendor needs those relationships to run the same workflow.',
  'prompt': 'Which exit test provides the strongest evidence of sourcing independence?',
  'options': ['Confirm that the old supplier allows files to be downloaded.',
              'Compare only the two vendors’ monthly subscription prices.',
              'Import representative data and metadata into the alternative and verify that the '
              'required workflow still works.'],
  'feedback': ['Download permission matters, but does not establish that the exported material is '
               'sufficient for the business use.',
               'Price comparisons miss migration effort, missing meaning and workflow disruption.',
               'A working migration test examines whether the business capability can move. '
               'Metadata and relationships are part of usable portability.'],
  'key': 2,
  'source': 'Session 05 deck, slides 10, 12, 15; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Sourcing '
            'Independence. The business situation and any numbers are illustrative.'},
 {'block': 'Seven cloud capabilities',
  'title': 'Accessible on a phone, unusable in the field',
  'concept': 'Ubiquitous access concerns useful access across devices and locations. Device '
             'compatibility and connectivity performance affect its realization.',
  'scene': 'A field team can sign into a cloud application from its phones, but each screen '
           'downloads large files. At remote sites the connection is slow, so staff cannot '
           'complete visits on time.',
  'prompt': 'What is the most relevant improvement?',
  'options': ['Treat successful sign-in as sufficient evidence that the intended access capability '
              'works.',
              'Adapt the interface and data transfer for field devices and assess suitable caching '
              'and connectivity.',
              'Buy a larger office monitor for each field employee.'],
  'feedback': ['Sign-in is only one part of access. The team must complete its work under the '
               'actual operating conditions.',
               'The article identifies performance and caching as practical concerns. The business '
               'outcome requires usable access, not just authentication.',
               'Office equipment does not address the field-device and network constraint.'],
  'key': 1,
  'source': 'Session 05 deck, slides 10, 12, 14; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Ubiquitous Access. '
            'The business situation and any numbers are illustrative.'},
 {'block': 'Seven cloud capabilities',
  'title': 'A folder is not an integrated business environment',
  'concept': 'A virtual business environment integrates applications, tools and process context '
             'around a business capability. It involves how work is organized.',
  'scene': 'A project team puts documents, chat and dashboards in separate cloud tools. Staff '
           'still re-enter data and cannot identify the next task or the approved project version. '
           'The sponsor calls the collection an integrated environment.',
  'prompt': 'Which change most directly delivers the missing capability?',
  'options': ['Put every document in one larger folder while leaving approvals and tasks '
              'disconnected.',
              'Link the tools through shared project context, a defined workflow and appropriate '
              'roles.',
              'Add more cloud subscriptions without changing the process.'],
  'feedback': ['A common storage location may help, but does not by itself integrate workflow, '
               'decisions or approvals.',
               'Integrated access and process guidance support coordinated decisions and '
               'execution. Tool count alone does not establish a virtual business environment.',
               'More separate tools can preserve the same fragmentation. The issue is their '
               'relationship to the work.'],
  'key': 1,
  'source': 'Session 05 deck, slides 10, 13–14; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Virtual Business '
            'Environments. The business situation and any numbers are illustrative.'},
 {'block': 'Seven cloud capabilities',
  'title': 'An invoice without a trail',
  'concept': 'Addressability identifies services or users; traceability records their use. '
             'Together they support audit, attribution and usage-based charging.',
  'scene': 'A cloud API bill rises sharply. All teams use one shared identifier and the provider '
           'retains only an organization-wide monthly total. Managers cannot connect usage to a '
           'project or investigate individual requests.',
  'prompt': 'What would most directly improve the ability to investigate the bill?',
  'options': ['Use attributable service or project identifiers and retain suitable request and '
              'usage records.',
              'Increase the monthly budget without changing identification or records.',
              'Choose another server region while keeping the same usage records.'],
  'feedback': ['Identifiable use plus a recorded history supports investigation and attribution. '
               'Access to the records and appropriate retention still need governance.',
               'A larger budget does not explain the increase or provide accountability.',
               'A location change does not establish who used which service and when.'],
  'key': 0,
  'source': 'Session 05 deck, slides 10, 13, 15; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Addressability and '
            'Traceability. The business situation and any numbers are illustrative.'},
 {'block': 'Seven cloud capabilities',
  'title': 'Elastic servers, a fixed bill',
  'concept': 'Rapid elasticity matches resources to workload. Pricing and commitments must also '
             'allow the firm to capture the economic benefit.',
  'scene': 'A cloud service adds capacity during peaks and releases it afterwards. The contract '
           'nevertheless charges a non-refundable annual minimum equal to the peak allocation. '
           'Finance forecasts lower costs in every quiet month.',
  'prompt': 'Which assessment best separates capability from benefit?',
  'options': ['The resource behavior is elastic, but the minimum commitment may prevent the '
              'forecast savings.',
              'A fixed minimum means the service cannot scale technically.',
              'Automatic scaling means the invoice must fall whenever workload falls.'],
  'feedback': ['Technical elasticity and economic flexibility need separate verification. This '
               'parallels the article’s warning about long-term commitments.',
               'Technical scaling and the payment structure are distinct. One can be flexible '
               'while the other is fixed.',
               'The resource mechanism does not determine every commercial term. The commitment '
               'can keep costs high despite resource release.'],
  'key': 0,
  'source': 'Session 05 deck, slides 10, 13–15; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Rapid Elasticity, '
            'including the Pulte Homes example. The business situation and any numbers are '
            'illustrative.'},
 {'block': 'Value and workload fit',
  'title': 'Expected cost rather than the largest possible saving',
  'concept': 'Economic evaluation should use the workload, relevant costs and commercial terms. '
             'Elastic provision is not automatically the cheapest option.',
  'scene': 'For one comparable service period, a fixed plan costs ₹12,000. An elastic plan costs '
           '₹4,000 in a quiet period and ₹20,000 in a busy period. Each outcome has probability '
           '0.5. Both plans meet the stated demand and service requirements; other costs are '
           'equal.',
  'prompt': 'Which conclusion follows from these assumptions?',
  'options': ['Fixed saves ₹8,000 because the elastic plan can cost ₹20,000.',
              'Both have an expected cost of ₹12,000; choose using other relevant trade-offs '
              'rather than claiming an expected-cost saving.',
              'Elastic saves ₹8,000 because its quiet-period cost is below the fixed plan.'],
  'feedback': ['This uses only the busy outcome. Expected cost must weight both stated outcomes.',
               'The elastic expectation is 0.5 × ₹4,000 + 0.5 × ₹20,000 = ₹12,000. The scenario '
               'does not establish a cost advantage; flexibility or risk may still influence the '
               'decision.',
               'This uses only the quiet outcome and ignores the equally likely busy cost.'],
  'key': 1,
  'source': 'Session 05 deck, slides 14–15, 20–21; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Rapid Elasticity and '
            'managerial value implications; deck decision exercises. The business situation and '
            'any numbers are illustrative.'},
 {'block': 'Value and workload fit',
  'title': 'More servers, unchanged completed orders',
  'concept': 'A capability creates value through the operating outcome. Scaling one resource '
             'cannot remove a bottleneck in another required part of the system.',
  'scene': 'A promotion’s application tier can process 700 orders per hour, but the database can '
           'complete only 300. The manager proposes increasing application capacity to 1,000 while '
           'leaving the database unchanged.',
  'prompt': 'Assuming no other bottlenecks change, what is the strongest assessment?',
  'options': ['Database capacity is irrelevant once the application tier uses cloud services.',
              'The 300-order database limit still constrains completed orders; evaluate the whole '
              'path before spending.',
              'Completed orders must rise to 1,000 because application capacity has risen.'],
  'feedback': ['Cloud provisioning does not eliminate application dependencies or resource limits.',
               'The expected operating benefit depends on the whole system. The scenario applies '
               'the deck’s app-tier and database-tier decision exercise.',
               'End-to-end completion requires both tiers. Increasing the nonbinding capacity does '
               'not remove the binding limit.'],
  'key': 1,
  'source': 'Session 05 deck, slides 14–15, 20–21; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, capability-to-value '
            'reasoning; deck’s whole-system scaling exercise. The business situation and any '
            'numbers are illustrative.'},
 {'block': 'Value and workload fit',
  'title': 'A backup is not uninterrupted trading',
  'concept': 'Service assurance requires explicit availability and recovery needs. Backup, '
             'restoration and failover address different operating consequences.',
  'scene': 'An online seller requires restoration within 15 minutes after a server failure. Its '
           'proposal provides nightly backup, but a recovery test takes four hours. Another '
           'proposal includes a redundant deployment and tested failover.',
  'prompt': 'Which evaluation best fits the stated requirement?',
  'options': ['Choose the cheapest plan because provider uptime removes the need for recovery '
              'testing.',
              'Approve nightly backup because any recoverable copy guarantees a 15-minute '
              'restoration.',
              'Compare tested recovery and failover times against 15 minutes, along with cost and '
              'other requirements.'],
  'feedback': ['A service label or uptime claim does not establish the recovery performance of '
               'this application.',
               'Recoverable data is important, but the observed restoration time does not meet the '
               'stated requirement.',
               'The decision needs evidence that the proposed arrangement meets the recovery '
               'requirement. Redundancy alone is also not proof unless failover works as needed.'],
  'key': 2,
  'source': 'Session 05 deck, slides 15, 20–21; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, adoption and '
            'assurance implications; deck’s service-reliability exercise. The business situation '
            'and any numbers are illustrative.'},
 {'block': 'Web services and managerial responsibility',
  'title': 'A web service can provision a resource',
  'concept': 'A web service exposes a software function to another application. It can return '
             'information, perform an action or provision a computing resource.',
  'scene': 'An application calls one API to store an invoice object and another to create a '
           'virtual server. A colleague says these cannot be web services because they do not '
           'return a weather forecast or exchange rate.',
  'prompt': 'Which explanation best resolves the confusion?',
  'options': ['Launching a server means the API has also deployed, secured and maintained the '
              'customer’s application.',
              'An API becomes a web service only if a human reads a text response in a browser.',
              'The API exposes a function: storing an object and creating a server are service '
              'actions, just as retrieving data is.'],
  'feedback': ['Provisioning infrastructure does not automatically perform all application and '
               'governance tasks. The service boundary still matters.',
               'Applications can consume service functions directly. A human-facing page is not '
               'required for the described interaction.',
               'The category is broader than information lookup. The deck distinguishes '
               'provisioning a resource from subsequently running and managing software on it.'],
  'key': 2,
  'source': 'Session 05 deck, slides 11, 16–18; Iyer and Henderson (2010), Preparing for the '
            'Future: Understanding the Seven Capabilities of Cloud Computing, Controlled '
            'Interface; deck’s web-service and cloud-resource examples. The business situation and '
            'any numbers are illustrative.'},
 {'block': 'Web services and managerial responsibility',
  'title': 'Capability, operating change and benefit',
  'concept': 'Cloud capability, operating outcome and business benefit are different links. '
             'Realized value needs the service design, adoption and managerial complements.',
  'scene': 'A sales team buys a cloud dashboard available across devices. Managers predict faster '
           'responses, but the staff still wait for a weekly approval meeting and few use the '
           'mobile view.',
  'prompt': 'What evidence and action would best support the promised benefit?',
  'options': ['Count purchased licenses as proof that response times have fallen.',
              'Check actual use and response times, and adapt approval roles and work practices to '
              'exploit access when needed.',
              'Treat the dashboard’s provider as solely responsible for changing the firm’s '
              'approval process.'],
  'feedback': ['Licenses establish access to a resource, not a change in operating performance.',
               'Ubiquitous access creates a possibility. Adoption and a compatible decision '
               'process are needed to realize the faster response, which must be measured.',
               'The firm retains responsibility for its work practices, incentives and decision '
               'rights.'],
  'key': 1,
  'source': 'Session 05 deck, slides 14–15; Iyer and Henderson (2010), Preparing for the Future: '
            'Understanding the Seven Capabilities of Cloud Computing, managerial implications and '
            'capability-based assessment. The business situation and any numbers are '
            'illustrative.'}]

RETRY_HINTS = ['Trace what would change in provisioned capacity and the bill after demand falls.',
 'Separate the physical host from the environments presented to its users.',
 'Locate the boundary between the application the team builds and the platform it wants managed.',
 'Identify who knows the employee’s current business role.',
 'Ask who the infrastructure is for, rather than where its machines sit.',
 'Distinguish buying two services from making the two environments work together.',
 'Ask what partners must be able to rely on when they call the service.',
 'Separate what the caller needs to know from what the organization must govern.',
 'Check whether the new service can interpret and use what has been exported.',
 'Measure whether employees can carry out the task on their actual device and connection.',
 'Ask whether the environment helps the team execute a business process, not only store its files.',
 'Ask what links a billed unit of usage to a service, user or project.',
 'Examine both the capacity released and the payment the contract still requires.',
 'Weight each outcome by its probability before comparing the plans.',
 'Trace an order through both tiers and find the lower capacity.',
 'Compare elapsed recovery time with the specific business tolerance.',
 'Identify the function requested and distinguish its completion from all the work that follows.',
 'Follow the chain from available access to changed work and then to the promised result.']

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

def render_session_05():
    _render()

if __name__ == "__main__":
    st.set_page_config(page_title="ISM LAB · Session 5", page_icon="📘", layout="wide")
    render_session_05()



