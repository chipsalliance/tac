---
title: Rocket Workgroup
leader: Jiuyang Liu (@sequencer)
website:
mailing_list: https://lists.chipsalliance.org/g/rocket-wg
meeting_dates:
meeting_link:
---

The Rocket Chip Workgroup covers the “Rocket” pipelined implementation of a RISC-V core as well as a TileLink uncore and cache coherent memory hierarchy. The main rocket-chip repository that the group maintains is a meta-repository containing tools needed to generate and test RTL implementations of SoC designs. This repository contains code that is used to generate RTL using [Chisel](http://chisel.eecs.berkeley.edu/) and Diplomacy: the Rocket Chip generator itself is a Scala program that invokes the Diplomacy library and Chisel compiler in order to emit RTL describing a complete SoC.
