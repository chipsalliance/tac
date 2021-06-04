# Project application: Espresso Logic Minimizer

## Application

### Sandbox application

* Project name: Espresso Logic Minimizer
* Project repo(s): https://github.com/chipsalliance/espresso/
* Brief summary of the project: Logic Minimizer Tool, rehost&remaintain under Chips Alliance.
* Project's open source license: [Init commit](https://github.com/chipsalliance/espresso/commit/52a94dde27426a6d17af90904264c8491b7c6534) is licensed via "Oct Tools Distribution 3.0", which needs to be relicensed to "BSD-2-Clause" since it is most similar. Commits after init commit(which are known as modifications) will be licensed via "Apache 2.0".
* Link to issue tracker: https://github.com/chipsalliance/espresso/issues
* Link to website: N/A
* Links to social media accounts: N/A
* Who uses this project, and at what scale: Chisel3 uses it as a backend of the Decoder Backend since Chisel 3.5. It is commonly depended by CPU projects, for example [SweRV-EL2](https://github.com/chipsalliance/Cores-SweRV-EL2/blob/master/design/ifu/el2_ifu_compress_ctl.sv) and [SweRV-EH2](https://github.com/chipsalliance/Cores-SweRV-EH2/blob/master/design/ifu/eh2_ifu_compress_ctl.sv) in Chips Aliiance.
* Why does the project want to join CHIPS Alliance: Espresso Logic is not maintained by [UCB](https://ptolemy.berkeley.edu/projects/embedded/pubs/downloads/espresso/README) anymore, but it's a necessary dependency for digital logic design. After this rehost, it will be documented, ported, and finally refactored to mordern C/C++/Rust.
* Primary contact from the project during the Sandbox application process:
  * Name: Jiuyang Liu
  * Email: liu@jiuyang.me
  * GitHub handle: sequencer
  * Role within the project: Maintainer

*Projects applying for Sandbox status may stop here.*

### Graduation application

* Total number of active committers:
* Brief description of release methodology and mechanics:
* Link to draft mission statement:
* Link to logo in .svg format
* Confirmation that the project adopts the [CHIPS Alliance Code of Conduct](https://lfprojects.org/policies/code-of-conduct/) upon acceptance:
* Confirmation that the project will adopt the [CHIPS Alliance IP policy](https://technical-charter.chipsalliance.org) upon acceptance:
* Confirmation that the project will add CHIPS Alliance header or footer text and links to its websites upon acceptance:
* Confirmation that the project will transfer any registered trademarks and domain names to the Linux Foundation upon acceptance:
* Link to documented process for reporting security vulnerabilities:
* **For specifications** Confirmation there is at least one public reference implementation:
* Primary contact from the project during the Graduation process:
  * Name:
  * Email:
  * GitHub handle:
  * Role within the project:
