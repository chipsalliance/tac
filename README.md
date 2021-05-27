# CHIPS Alliance Technical Steering Committee (TSC)

The CHIPS Alliance TSC will be responsible for all technical oversight of the open source project.

## Technical Charter and Code of Conduct

The CHIPS Alliance TSC is governed by a [Technical Charter](https://technical-charter.chipsalliance.org), which establishes the Committee and its basic principles and procedures. The charter is designed to provide the TSC the freedom to govern itself in an efficient manner. This document establishes TSC policies and procedures.

In addition, as provided under the Technical Charter, CHIPS Alliance has adopted a [Code of Conduct](https://lfprojects.org/policies/code-of-conduct/) that applies to all CHIPS Alliance activities and spaces.

## TSC Voting Members,Projects and Working Groups

Per the Technical Charter, on top of any members appointed in the initial bootstrap phase, the TSC will be comprised of one representative from each graduated Project. 

The current members of the CHIPS Alliance TSC are:

| Name                      | GitHub                                              | Affiliation | Project | Term begins  | Term ends    |
| ------------------------- | --------------------------------------------------- | ------------|---------|--------------|--------------|
| Henry Cook (chair)        | [hcook](https://github.com/hcook)                   | SiFive      | (chair) | (appointed)  | (appointed)  |
| Michael Gielda            | [mgielda](https://github.com/mgielda)               | Antmicro    | (mktg)  | (appointed)  | (appointed)  |
| Henner Zeller             | [hzeller](https://github.com/hzeller)               | Google      | Verible | (appointed)  | (appointed)  |

The [Technical Charter](https://technical-charter.chipsalliance.org) describes the composition of the TSC.

### Sandbox projects

* See [Sandbox projects](./projects/sandbox) for a list of projects currently in Sandbox.

### Working Groups

Projects are organized into Working Groups for the purpose of e.g. organizing meetings which aggregate related projects and topical areas.

Currently, the following working groups have been established:

* [Analog](https://github.com/chipsalliance/tsc/blob/HEAD/working_groups/analog/README.md)
* [Tools](https://github.com/chipsalliance/tsc/blob/HEAD/working_groups/tools/README.md)
* Chisel
* Rocket
* Interconnects
* Cores

(the descriptions for Chisel, Rocket, Interconnects, Cores need to be added via separate PRs)

## Getting Oriented

This repo documents the day-to-day policies and procedures of the CHIPS Alliance TSC. It provides a framework for self-governance, and addresses topics too granular for the [Technical Charter](https://technical-charter.chipsalliance.org).

This repository has the following structure:

- [drafts](./drafts) - drafts of our internal documents
- [meetings](./meetings) - our meeting agendas and minutes
- [projects](./projects) - list of projects in different lifecycle stages
- [proposals](./proposals) - policy proposals under consideration

Here are some other links to help you find your way:

* [An introduction to our collaboration tools](#collaboration-tools)
* [Our policies and procedures](#policies-and-procedures)
* [The current voting members of the TSC](#tsc-members) (please note anyone can participate in our [meetings](#calendars-and-meetings) as a non-voting attendee)
* [Projects and Workgroups of the CHIPS Alliance](#projects-and-workgroups)

Finally, if you need help, please [reach out and ask](#getting-help).

## Collaboration Tools

### Mailing List

The CHIPS Alliance TSC can be reached at [technical-discuss](https://lists.chipsalliance.org/g/technical-discuss). This mailing list is open for anyone to join, and all are welcome to participate in general technical discussions about the project.

### Slack

The CHIPS Alliance maintains a [Slack Workspace](https://slack.chipsalliance.org) for communication and collaboration, which is open for anyone to join. Once you join [Slack](https://slack.chipsalliance.org), you can participate in any public channels.

### Calendars and Meetings

The CHIPS Alliance maintains a [public calendar](https://calendar.chipsalliance.org) for TSC meetings. These meetings are open for anyone to join.

CHIPS Alliance uses Zoom for meetings. Because we work in a highly distributed environment and will rarely meet in person, participants are encouraged to use video as appropriate.

To join a TSC meeting: [https://zoom.us/j/96738269957](https://zoom.us/j/96738269957) (pw: chipstsc)

## Projects and Workgroups

The TSC is granted oversight over all CHIPS Alliance technical projects and workgroups. In CHIPS Alliance, similar technical projects are organized into workgroups. Each project is represented within the workgroup's internal governance structure. Likewise, each workgroup selects a member to represent it as a voting member of the TSC, using an open and transparent selection process.

### Mission Statements

Each project must have a mission statement ([template](./projects/MISSION_STATEMENT_TEMPLATE.md)) which describes its purpose and governance. Changes to mission statements must be reviewed and approved by the TSC.

### Lifecycle

Each project is categorized according to a [project lifecycle process](./projects/), managed by the TSC. Projects and workgroups will have different maturity levels, and the lifecycle process seeks to balance their needs and expectations with available resources.

#### Project categories

* **[Sandbox](projects/README.md#sandbox)**: Optional pre-membership stage to help a project prepare for the TSC's consideration. Sandbox projects are not yet part of CHIPS Alliance, but may be allocated TSC resources to help with the process.
* **[Graduated](projects/README.md#graduated)**: A project which has been accepted by the TSC, assigned to a workgroup, met the graduation requirements, and demonstrated sustainable momentum.
* **[Archived](projects/README.md#archived)**: A former Graduated project which has been archived for strategic or practical reasons.

#### Workgroup levels

* **Active**: Contains at least one Graduated project, or a majority of the TSC has voted to create the workgroup to collaborate on future projects.
* **Archived**: No longer contains any Graduated projects.

The TSC has sole authority over a project's lifecycle stage and workgroup, including the decision to accept or reject project proposals. It also may create or consolidate workgroups at its discretion.

#### Instantiating projects

All projects will go through the onboarding process. At a high level, this includes:

* Completing a mission statement, which will be hosted in the [projects](./projects) directory.
* Completing a [project application template](./projects/PROJECT_APPLICATION_TEMPLATE.md) through Graduated stage, at least.
* Adding core collaborators to a GitHub team in the CHIPS Alliance organization under [Project Leadership](https://github.com/orgs/chipsalliance/teams/project-leadership/teams).
* Transferring repositories to the CHIPS Alliance.
* Setting up a project mailing list on the CHIPS Alliance domain.
* Adding CHIPS Alliance footers and notices to project websites.
* Designating a representative to the project's workgroup.
* Designating a representative to attend TSC meetings (as a voting member or participant).

Linux Foundation staff are able to help with this process.

### Resources

All Graduated projects and Active workgroups can make use of the CHIPS Alliance collaboration resourcs, including:

* Access to the shared Zoom account
* Meetings listed on the public [CHIPS Alliance calendar](https://calendar.chipsalliance.org)
* Mailing lists on [lists.chipsalliance.org](https://lists.chipsalliance.org)
* Credential storage and sharing through LastPass
* GitHub repos and teams in the [`chipsalliance` GitHub org](https://github.com/chipsalliance)

### The CHIPS Alliance Commons: Related projects and initiatives

The CHIPS Alliance exists within a rich ecosystem of interrelated projects. While the TSC's first objective is to support the success of CHIPS Alliance projects, it also acknowledges the critical strategic roles played by external open source projects. Collectively, we refer to these projects as "The CHIPS Alliance Commons".

Although these projects remain outside of the CHIPS Alliance organization and its policies, the TSC may recognize these projects in various ways. For example, the TSC can maintain a list of strategic open source projects, or make an effort to include their participants and maintainers in relevant TSC discussions.

The CHIPS Alliance TSC is grateful to the broader open source ecosystem, and is looking forward to healthy collaboration within and external to the Alliance.

## Policies and procedures

The CHIPS Alliance TSC is governed by the [Technical Charter](https://technical-charter.chipsalliance.org). The Charter provides a foundational structure for the TSC on topics such as its scope, how to make decisions, and how to make changes to itself. At the same time, it grants the TSC a high degree of freedom when determining how to implement the policies of CHIPS Alliance.

The following policies and procedures have been adopted by the TSC.

### Reporting security vulnerabilities

All CHIPS Alliance projects **must** have a process for receiving security vulnerability reports. If a project does not have its own process, the default policy is to send a detailed disclosure to [security@lists.chipsalliance.org](mailto:security@lists.chipsalliance.org). This is a confidential mailing list, and the TSC chair and a small group of trusted individuals will review and act upon the report as appropriate.

### Voting procedures

The TSC will use voting to make decisions when required by the charter, or when consensus cannot be reached.

Votes may be initiated by any [TSC voting member](#tsc-voting-members) or CHIPS Alliance staff. Except when required otherwise by the charter, votes are decided by a simple majority of all eligible voting members. Unless withdrawn, votes remain open until they meet their acceptance or rejection threshold.

Email votes are strongly preferred because they provide a clear history, although alternate voting systems may be used if they better serve the need of the situation (e.g., OpaVote, CIVS, etc.). Voting outcomes should be recorded in the minutes of the next TSC meeting. It is sufficient to publish the outcome; it is not necesssary to publish how each member voted unless there is unanimous agreement among voting members.

Template for initiating an email vote:

```
To: technical-internal@lists.chipsalliance.org
Subject: Please vote: [summary of vote]

[2-4 sentences describing the topic of the vote, concluding with the actual vote]

Voting members, please vote by replying "Approve", "Reject", or "Abstain".
```

When a vote is related to a PR or issue, apply the labels [vote-required](https://github.com/chipsalliance/tsc/labels/vote-required), [vote-in-progress](https://github.com/chipsalliance/tsc/labels/vote-in-progress), [vote-passed](https://github.com/chipsalliance/tsc/labels/vote-passed), or [vote-rejected](https://github.com/chipsalliance/tsc/labels/vote-rejected) as appropriate.

### Merging PRs into the TSC repository

Pull requests that do not change the charter or governance of the TSC can be merged into this repository provided the following conditions have been met:

* There are no outstanding objections
* There are two approvals by TSC members
* The PR has been open for at least 72 hours

Pull requests that change governance of the TSC (excluding the charter) must be open for at least 14 days, unless consensus is reached in a meeting with quorum of voting members, or an email vote has been passed in favor of the PR, as signified by the [vote-passed](https://github.com/chipsalliance/tsc/labels/vote-passed) label (see [Voting procedures](#voting-procedures) above).

Pull requests that change the charter of the TSC must meet any requirements in the [charter](https://technical-charter.chipsalliance.org).

If consensus cannot be reached, a pull request may still be landed after a vote by the Voting members to override outstanding objections.

### Fast-Tracking PRs

Special exception is made for pull requests seeking to make any of the following changes to this repository:

- Meeting minutes.
- Doc fixes.

Charter changes cannot be fast-tracked.

To propose fast-tracking a pull request, apply the ***fast-track*** label. Then add a comment that TSC members may upvote. If someone disagrees with the fast-tracking request, remove the label. Do not fast-track the pull request in that case.

The pull request may be fast-tracked if two TSC members approve the fast-tracking request. To land, the pull request itself still needs two TSC member approvals.

TSC members may request fast-tracking of pull requests they did not author. In that case only, the request itself is also one fast-track approval. Upvote the comment anyway to avoid any doubt.

### Trivial PRs

Trivial PRs that update factual situations can be merged immediately. When opening the PR, please note that the change is trivial and that it will be merged directly. Examples include:

- Errata fixes.
- Editorial changes.
- Updates to team lists.

If a TSC member does not believe the change was trivial, it can be reverted and proposed through the normal PR process.

### IP Policy

The CHIPS Alliance IP policy is contained in the [charter](https://technical-charter.chipsalliance.org), and it applies to all CHIPS Alliance projects unless an exception is explicitly approved by the TSC.

#### Copyright notices

CHIPS Alliance follows the [community best practice](https://www.linuxfoundation.org/blog/2020/01/copyright-notices-in-open-source-software-projects/) of not requiring contributors to add a notice to each file.

#### SPDX

Projects are encouraged (but not required) to adopt the practice of including [SPDX short form identifiers](https://spdx.org/ids-how) in their files.

#### Website footers

CHIPS Alliance projects should use one of the following notices on their websites, as appropriate:

##### For HTML sites
> ```
> Copyright CHIPS Alliance Project a Series of LF Projects, LLC.<br>For web site terms of use, trademark policy and general project policies please see <a href="https://lfprojects.org">https://lfprojects.org</a>.
> ```

##### For markdown sites, including GitHub READMEs

> ```
> ---
>
> **Copyright CHIPS Alliance Project a Series of LF Projects, LLC.**  
> For web site terms of use, trademark policy and general project policies please see [https://lfprojects.org](https://lfprojects.org).
> ```

### Creating and managing GitHub repos in the CHIPS Alliance organization

CHIPS Alliance projects are welcomed and encouraged to host their repositories within the [CHIPS Alliance organization](https://github.com/chipsalliance).

#### Adding repositories to the organization

Repositories may be transferred into or created under the CHIPS Alliance organization so long as:

* They adhere to the CHIPS Alliance IP policy.
* They are directly operated by a CHIPS Alliance project.
* The TSC achieves rough consensus about adding the repository.

Sometimes projects will rely upon other external repositories (e.g., tooling or dependencies). While it is a best practice to work upstream whenever possible, there may be situations where a downstream fork is required. In this situation, rough consensus on the TSC is sufficient to create a new fork.

Finally, non-technical repositories may be needed for admin purposes, and may be created by staff from time to time.

#### Keeping the organization tidy

Because CHIPS Alliance contains multiple projects, please use a consistent and descriptive naming convention that will group all related repositories together when sorted alphabetically. For example:

* project1
* project1-website
* project1-admin
* project2
* project2-ci
* project2-mentorship
* project2-website
* ...

The best time to rename a repo is when it is transferred into the CHIPS Alliance organization. GitHub ensures that [all links to the prior repository are automatically redirected to the new location](https://help.github.com/en/github/administering-a-repository/transferring-a-repository), and [links to the repository are preserved when a repository is renamed](https://help.github.com/en/github/administering-a-repository/renaming-a-repository). This means that `git clone`, `git fetch`, `git pull`, and `git push` will function without requiring any changes from existing users.

#### Repository configuration and management

All CHIPS Alliance repositories containing technical information must be set to public.

To help ensure effective repo management, each project should manage a GitHub team of its committers within the CHIPS Alliance org. That team should be added to any repository to which they should have commit rights.

#### Archiving repositories

The TSC may choose to move repositories to an archived state, at its own discretion. Most often this will occur if there are concerns about a repository being unmaintained, but may also happen if two efforts are consolidating and one codebase is being kept for archival purposes.

## Getting Help

### Help with project infrastructure

Membership in the CHIPS Alliance helps to fund collaborative infrastructure used by our projects.

For help with project infrastructure please contact [operations@chipsalliance.org](mailto:operations@chipsalliance.org). Examples of ways the Linux Foundation can help include:

* Adding and removing members from GitHub teams
* Creating and archiving repositories
* Creating and managing mailing lists on the lists.chipsalliance.org domain
* Managing DNS (for projects which host their nameserver with the LF)
* Creating and managing email aliases (for projects which host their nameserver with the LF)

### Help with membership

#### New members

CHIPS Alliance welcomes new members, and we would be happy to help answer any questions you may have. To learn more about membership, please visit [https://chipsalliance.org/join](https://chipsalliance.org/join) or email [membership@chipsalliance.org](mailto:membership@chipsalliance.org).

#### Existing members

CHIPS Alliance members can get help with anything related to their membership by emailing [operations@chipsalliance.org](mailto:operations@chipsalliance.org).

### Help with press and media

For help with press and media inquiries, or to let the CHIPS Alliance marketing committee know about something exciting happening in your project (releases, major milestones, ecosystem events, etc.) please email [pr@chipsalliance.org](mailto:pr@chipsalliance.org).

### All other topics

For any other topics which aren't covered above, please email [operations@chipsalliance.org](mailto:operations@chipsalliance.org).

---

**Copyright CHIPS Alliance Project a Series of LF Projects, LLC.**  
For web site terms of use, trademark policy and general project policies please see [https://lfprojects.org](https://lfprojects.org).

https://technical-charter.chipsalliance.org
