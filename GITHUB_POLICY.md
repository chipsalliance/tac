# CHIPS Alliance Github Organization Policy For Existing Projects

## Introduction

This document outlines the policies and guidelines for creating **new** repositories within the CHIPS Alliance GitHub organization. These policies are intended for projects that are already part of CHIPS Alliance and are working in the CHIPS Alliance Github Organization. 

## Repository Creation and Management

### Private Repositories

- Creation Permission: Projects are permitted to create private repositories as needed without prior approval.
- Usage: Private repositories should be used for internal development, sensitive information, or any content not yet ready for public disclosure.

### Public Repositories

#### Approval Process

- Submission Requirement: To create a new public repository or convert an existing private repository to public, 
  the project must submit an issue to [this Github Repository](https://github.com/chipsalliance/tac/issues/new/choose).
- Review Body: The Technical Advisory Committee (TAC) will review all submissions.
- Decision Criteria: The TAC will assess compliance with the policies outlined in this document.

#### Requirements for Public Repositories

1.	Contributor License Agreement (CLA) Enforcement
    - Mandatory CLA: All public repositories must have CLA enforcement enabled.
    - Assistance: CHIPS Alliance will provide support to set up CLA enforcement mechanisms.
2.	Licensing
    - LICENSE.md File: A valid LICENSE.md file must be included in the repository.
    - Compliance: The license must adhere to the [CHIPS Alliance IP Guidelines](https://participation-agreement.chipsalliance.org/), Apache 2.0 unless special exception is granted.
3.	Project Affiliation
    - Direct Operation: The repository must be directly operated by a CHIPS Alliance project.
    - Clear Identification: The project affiliation should be evident in the repository’s description and documentation.

#### Recommended Repository Naming Conventions

To maintain a clear and organized repository structure, we recommend repositories follow a consistent and descriptive naming
convention. This practice helps in grouping related repositories together when sorted alphabetically.

#####  Naming Guidelines

- Format: We recommend but do not enforece the following format for repository names:

```
[project-name]
[project-name]-[descriptor]
```

- Project Name: Use a concise and consistent identifier for your project.
- Descriptor: Use a descriptive term to indicate the repository’s purpose (e.g., website, admin, ci, mentorship).
- Separator: Use a hyphen (-) to separate the project name and descriptor.

##### Examples

* project1
* project1-website
* project1-admin
* project2
* project2-ci
* project2-mentorship
* project2-website

 #### Additional Recommendations

- Consistency: Ensure consistent use of project names and descriptors across all repositories.
- Clarity: Choose descriptors that clearly reflect the content or purpose of the repository.
- Avoid Abbreviations: Unless commonly understood, avoid using abbreviations that might confuse contributors or users.
- Ensure that your [project's .yaml file](https://github.com/chipsalliance/tac/tree/main/projects/project-data-files) is kept up to date and lists all the public repositories associated with your project. 

#### Compliance and Enforcement

- Periodic Reviews: The TAC may conduct periodic reviews of repositories to ensure ongoing compliance with these policies.
- Non-Compliance Resolution: Repositories found in violation may be subject to removal or reversion to private status until compliance is achieved.
- Feedback Mechanism: Projects will be notified of any issues and provided with guidance on how to comply.

#### Support and Resources

- Assistance with CLA: For help setting up CLA enforcement, contact [operations@chipsalliance.org](mailto:operations@chipsalliance.org).
- Questions and Clarifications: For any questions regarding these policies, reach out to the TAC or [operations@chipsalliance.org](mailto:operations@chipsalliance.org).
