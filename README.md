# CHIPS Alliance Technical Steering Committee (TSC)

The CHIPS Alliance TSC will be responsible for all technical oversight of the open source project.

## Technical Charter and Code of Conduct

The CHIPS Alliance TSC is governed by a [Technical Charter](CHARTER.md), which establishes the Committee and its basic principles and procedures. The charter is designed to provide the TSC the freedom to govern itself in an efficient manner. This document establishes TSC policies and procedures.

In addition, as provided under the Technical Charter, CHIPS Alliance has adopted a [Code of Conduct](https://lfprojects.org/policies/code-of-conduct/) that applies to all CHIPS Alliance activities and spaces.

## Collaboration Tools

### Mailing List

The CHIPS Alliance TSC can be reached at [technical-discuss](https://lists.chipsalliance.org/g/technical-discuss). This mailing list is open for anyone to join, and all are welcome to participate in general technical discussions about the project.

### Slack

The CHIPS Alliance maintains a [Slack Workspace](https://slack.chipsalliance.org) for communication and collaboration, which is open for anyone to join. Once you join [Slack](https://slack.chipsalliance.org), you can participate in any public channels.

### Calendars and Meetings

The CHIPS Alliance maintains a [public calendar](https://calendar.google.com/calendar/embed?src=linuxfoundation.org_ik78i4dsvm5sll7hgo1j54i1ls%40group.calendar.google.com) for TSC meetings. These meetings are open for anyone to join.

CHIPS Alliance uses Zoom for meetings. Because we work in a highly distributed environment and will rarely meet in person, participants are encouraged to use video as appropriate.

To join a TSC meeting: [https://zoom.us/j/96738269957](https://zoom.us/j/96738269957) (pw: chipstsc)

## TSC Members

The current members of the CHIPS Alliance TSC are:

| Name                      | GitHub                                              | Affiliation | Term begins  | Term ends    |
| ------------------------- | --------------------------------------------------- | ------------|--------------|--------------|
| Henry Cook (chair)        |[hcook](https://github.com/hcook)                    | SiFive      | (appointed)  | (appointed)  |


### Becoming a TSC Member

The [Technical Charter](CHARTER.md) describes the composition of the TSC.

## Projects and Workgroups

The TSC is granted oversight over all CHIPS Alliance technical projects and workgroups. In CHIPS Alliance, similar technical projects are organized into workgroups. Each project is represented within the workgroup's internal governance structure. Likewise, each workgroup selects a member to represent it as a voting member of the TSC, using an open and transparent selection process.

### Mission Statements

Each project must have a mission statement ([template](projects/MISSION_STATEMENT_TEMPLATE.md)) which describes its purpose and governance. Changes to mission statements must be reviewed and approved by the TSC.

### Lifecycle

Each project is categorized according to a [project lifecycle process](projects/), managed by the TSC. Projects and workgroups will have different maturity levels, and the lifecycle process seeks to balance their needs and expectations with available resources.

#### Project categories

* **[Sandbox](projects/README.md#sandbox)**: Optional pre-membership stage to help a project prepare for the TSC's consideration. Sandbox projects are not yet part of CHIPS Alliance, but may be allocated TSC resources to help with the process.
* **[Incubating](projects/README.md#incubating)**: A project which has been accepted by the TSC and assigned to a workgroup.
* **[Graduated](projects/README.md#graduated)**: A project which has met the graduation requirements and demonstrated sustainable momentum.
* **[Archived](projects/README.md#archived)**: A former Incubating or Graduated project which has been archived for strategic or practical reasons.

#### Workgroup levels

* **Active**: Contains at least one Incubating or Graduated project.
* **Archived**: No longer contains any Incubating or Graduated projects.

The TSC has sole authority over a project's lifecycle stage and workgroup, including the decision to accept or reject project proposals. It also may create or consolidate workgroups at its discretion.

### List of projects by workgroup

#### Workgroup A

* [Project 1](LINK-TO-PROJECT-1) (Graduated)
* [Project 2](LINK-TO-PROJECT-2) (Incubating)

#### Workgroup B

* [Project 3](LINK-TO-PROJECT-3) (Incubating)
* [Project 4](LINK-TO-PROJECT-4) (Sandbox)

#### Archived projects

* [Project 6](LINK-TO-PROJECT-6)

## Policies and procedures

The CHIPS Alliance TSC is governed by the [Technical Charter](CHARTER.md). The Charter provides a foundational structure for the TSC on topics such as its scope, how to make decisions, and how to make changes to itself. At the same time, it grants the TSC a high degree of freedom when determining how to implement the policies of CHIPS Alliance.

The following policies and procedures have been adopted by the TSC.

### Merging PRs into the TSC repository

Pull requests that do not change the charter or governance of the TSC can be merged into this repository provided the following conditions have been met:

* There are no outstanding objections
* There are two approvals by TSC members
* The PR has been open for at least 72 hours

Pull requests that change governance of the TSC (excluding the charter) must be open for at least 14 days, unless consensus is reached in a meeting with quorum of voting members.

Pull requests that change the charter of the TSC must meet any requirements in the [charter](CHARTER.md).

If consensus cannot be reached, a pull request may still be landed after a vote by the Voting members to override outstanding objections.

### Fast-Tracking PRs

Special exception is made for pull requests seeking to make any of the following changes to this repository:

- Errata fixes.
- Editorial changes.
- Meeting minutes.
- Updates to team lists.
- Doc fixes.

Charter changes cannot be fast-tracked.

To propose fast-tracking a pull request, apply the ***fast-track*** label. Then add a comment that TSC members may upvote. If someone disagrees with the fast-tracking request, remove the label. Do not fast-track the pull request in that case.

The pull request may be fast-tracked if two TSC members approve the fast-tracking request. To land, the pull request itself still needs two TSC member approvals.

TSC members may request fast-tracking of pull requests they did not author. In that case only, the request itself is also one fast-track approval. Upvote the comment anyway to avoid any doubt.

### IP Policy

The CHIPS Alliance IP policy is contained in the [charter](CHARTER.md), and it applies to all CHIPS Alliance projects unless an exception is explicitly approved by the TSC.

#### Copyright notices

CHIPS Alliance follows the [community best practice](https://www.linuxfoundation.org/blog/2020/01/copyright-notices-in-open-source-software-projects/) of not requiring contributors to add a notice to each file.

#### SPDX

Projects are encouraged (but not required) to adopt the practice of including [SPDX short form identifiers](https://spdx.org/ids-how) in their files.

#### Website footers

CHIPS Alliance projects should use one of the following notices on their websites, as appropriate:

##### For HTML sites
> ```
> Copyright CHIPS Alliance Project a Series of LF Projects, LLC. For web site terms of use, trademark policy and general project policies please see <a href="https://lfprojects.org">https://lfprojects.org</a>.
> ```

##### For markdown sites, including GitHub READMEs

> ```
> ---
>
> Copyright CHIPS Alliance Project a Series of LF Projects, LLC. For web site terms of use, trademark policy and general project policies please see [https://lfprojects.org](https://lfprojects.org).
> ```

---

Copyright CHIPS Alliance Project a Series of LF Projects, LLC. For web site terms of use, trademark policy and general project policies please see [https://lfprojects.org](https://lfprojects.org).

