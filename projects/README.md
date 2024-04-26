# Project Lifecycle Process

## Introduction

This governance policy describes how an open source project can formally join the CHIPS Alliance. The process is the same for existing projects which seek to move into CHIPS Alliance and new projects being formed within CHIPS Alliance.

There are three project categories:

* [Sandbox](#sandbox): Optional pre-membership stage to help a project prepare for the TSC's consideration.
* [Graduated](#graduated): A project which has met the graduation requirements and demonstrated sustainable momentum.
* [Archived](#archived): A former Graduated project which has been archived for strategic or practical reasons.

## Project Proposal Process

The acceptance process is a three-stage process: a technical review with the Technical Advisory Committee (TAC), legal submission to LF, and a vote by the Governing Board.

```mermaid
flowchart TD
    A(Technical Review) --> 
    C{TAC Vote}
    C -->|Approved| D[Project is\n'Sandbox']
    C -->|Declined| A
    D --> E(Complete Legal Review)
    D --> F(Complete Onboarding Checklist)
    E --> G
    F --> G{Board Vote} 
    G -->|Approved| H[Project is\n 'Graduated']
 ```

### Project Acceptance Process

#### Technical Review

Projects are required to present their proposal at a TAC meeting. This proposal should cover all the items in the [Project Application Template](./templates/project-application-template.yml).

The TAC may ask for changes to bring the project into better alignment with the CHIPS Alliance (adding a governance document to a repository or adopting a Code of Conduct, for example). The project will need to make these changes in order to progress further.

Projects are accepted or progress from category to category via a two-thirds majority vote of TAC representatives.

The TAC will determine the appropriate initial stage for the project. The project can apply for a different stage via the review process.

Once a project passes Technical Review, the TAC will inform the Governing Board of the submission proposal.

#### Legal Submission

After a successful TAC vote, the project is ready for a legal review. The legal review is initiated by the project filling out [this form](https://docs.google.com/forms/d/e/1FAIpQLSeO1bDGHUP-ZpCo1uynm94YOxZlek6RhCH7o3FnX1lZSXXfSQ/viewform?fbzx=4351560609072672295) and working with the CHIPS operations team. The LF project onboarding team will create a draft Technical Charter, a draft Project Contribution Agreement (if needed), and a draft Series Agreement.

As noted in clause 10 of the CHIPS Alliance Charter,  CHIPS requires that any trademarks be transferred to, or be available for use by, LF Projects, LLC. Even if no trademarks exist, the current CP policy is that projects be submitted to LF Projects, LLC.

#### Governing Board Vote

Once the Technical Review and Legal Submission steps are complete, the Governing Board will review the project proposal and the proposed Technical Charter. If there are legal questions raised, the Governing Board may refer the matter to the Legal Committee for review. This review may occur in parallel with Technical Review in some cases.

Once any such legal questions have been addressed, the Governing Board will vote at its next available meeting.

Upon acceptance by the board, the project's approved Technical Charter must be included in the project's main repository. This document can be in whatever format is most appropriate for the project, as long as the content is the same.


## Project Category Definitions & Expectations

### Sandbox

Sandbox projects are projects which plan to join the CHIPS Alliance, but have not yet met the prerequisites to formally join.

#### Benefits of becoming a Sandbox project:

* The TAC will prioritize requests for help meeting the requirements of Graduated projects.
* The TAC will monitor the project to ensure progress is being made.


#### Expectations of Sandbox projects:

* Because Sandbox projects are not yet a part of CHIPS Alliance, it is their responsibility to manage the Graduation application process.
* Projects may remain in the Sandbox stage so long as they are making reasonable progress toward applying for Graduated status.
* Projects which cease to make progress or are on a trajectory which would lead to rejection may be removed by majority vote of the TAC.
* Projects may reapply for Sandbox status if previously removed for any reason.


#### Requirements to become a Sandbox project:

1. The project must complete an application in the form of a `.yml` file in this directory, and open a PR against the TAC repo with the `tac-meeting` and `sandbox-application` labels.
1. The project must join a TAC meeting to present its proposal.
1. TAC must approve the application as a Sandbox project by majority vote.

When a Sandbox proposal is accepted, the PR may be landed.

### Graduated

Graduated projects are projects which have applied and been formally accepted as CHIPS Alliance projects by the TAC. Graduated projects are officially a part of CHIPS Alliance.

However, achieving Graduated status requires more than maturity and adoption. The TAC is run by and for the technical community, and it can only function with involvement from project leaders. Representatives from Graduated projects are expected to take an active role in TAC and CHIPS Alliance processes. For example, participating in TAC meetings, volunteering as a program committee member for events,chairing a CHIPS workgroup, participating in mentoring initiatives, and helping Sandbox projects prepare for their Graduated status application.


#### Benefits of becoming a Graduated project

* Project can put forward a voting representative to the CHIPS TAC
* Project may claim a formal association with CHIPS Alliance
* Project gains access to CHIPS Alliance resources, including events, the ability to request financial resources, and mentorship.


#### Expectations of Graduated projects

* Projects must adhere to open source best practices.
* Project must proactively and positively promote CHIPS Alliance.
* Project must participate actively in its workgroup meetings and governance, and any other positions held within CHIPS Alliance. At least one member from the Project should join TAC meetings, whether a voting member or non-voting attendee.
* Project will participate in reviews by the TAC to ensure it remains a fit for CHIPS Alliance.
* Project must actively work to ensure a healthy number of committers.
* Project must demonstrate ongoing and sustained involvement from contributors.
* The project must ensure that committers are diversified across organizations.
* The project must avoid actions that will lead to an unsustainable development community.
* The project must lead by example on adherence to core project policies, such as the Code of Conduct.
* The project must exemplify the values of CHIPS Alliance and be committed to diversity and inclusion.


#### Requirements to become a Graduated project

1. The project must actively work with the TAC as it does due diligence to determine fit.
1. The project must have a substantial ongoing flow of commits and merged contributions.
1. The project must use a clear versioning scheme.
1. The project must have a [draft mission statement](./MISSION_STATEMENT_TEMPLATE.md) prepared for TAC approval.
1. The project must internally pre-approve the Code of Conduct, IP Policy, and [header/footer for websites](https://github.com/chipsalliance/tsc/blob/main/README.md#website-footers) so that they are in effect upon project acceptance by the TAC.
1. The project must complete an `.yml` application in this directory, set the status in the `.yml` file to "graduated" and open a PR against the TAC repo with the `tac-meeting` and `graduation-application` labels.
1. The project must join a TAC meeting to present its proposal.
1. The TAC must approve the Graduated status application and the project's mission statement by majority vote.
1. The project must have a documented process for reporting security vulnerabilities, or accept the [default CHIPS Alliance security reporting process](https://github.com/chipsalliance/tsc/blob/main/README.md#reporting-security-vulnerabilities).
1. The project must receive a supermajority vote from TAC voting members.
1. The project must work with CHIPs To Sign Technical Charter / Participation Agreement / Assign Trademark  
1. The project must adopt and enforce the CLA
2. The project must be approved by a vote of the CHIPS Alliance Governing Board
3. The project must add ‘thelinuxfoundation’ GitHub user as an owner to all repositories

When a Graduated proposal is accepted, the PR may be landed.

### Archived

Archived projects are projects which no longer have sufficient momentum to justify an active state in CHIPS Alliance. By archiving a project, CHIPS Alliance is indicating that downstream users should not expect any updates, including security fixes or backports.

The decision to move a project to Archived is not taken lightly by the TAC, and each situation will be unique.  However, reasons which could lead to an Archived state may include:

* The project has requested the TAC move it to Archived state.
* There are no more active committers.
* There are no more active contributors.
* Another project has encompassed its functionality.

### Expectations of Archived projects

* If possible, the project should add a Linux Foundation member as organization owner.
* The project should remove all references to its former CHIPS Alliance lifecycle stage, the standard footer, and any logos.
* The project should move its repos to `Archived` state in GitHub.
* The project should add a prominant notice on its `README.md` and `CONTRIBUTING.md` that the project has been archived, and that downstream users should not expect any further development, updates, or fixes.

### Requirements to become an Archived project

1. A representative from the project or a TAC voting member should change their projects' `.yml` status to "archived" and open a PR against the TACs repo with the `tac-meeting` and `archival-application` labels.
1. A representative from the project or a TAC voting member must join a TAC meeting to present the proposal.
1. The archival proposal must receive a supermajority vote from TAC voting members.

When an Archival proposal is accepted, the PR may be landed.