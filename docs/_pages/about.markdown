---
layout: page
title: About
permalink: about/
---

This repository ([rdapy](https://github.com/dra2020/rdapy)) re-implements 
the main analytics used in [Dave's Redistricting](https://davesredistricting.org/) (DRA),
ignoring a few DRA-specific aspects (in particular, the five [0-100] ratings).
Unlike the analytics used in the app ([dra-analytics](https://github.com/dra2020/dra-analytics))
which are implememented in TypeScript, these are implemented in Python to make them easier to use outside of DRA.

There are both a PyPi package and a command-line interface. 