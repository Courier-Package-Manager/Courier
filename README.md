<div align="center">
<a href="https://github.com/JoshuaDRose/Courier/"><img alt="github-header-image" src="https://user-images.githubusercontent.com/101031214/223869242-ac1234cf-1450-426e-baa9-69955ccc28ca.png"></a>
<br>
</div>
<br>
<br>
<br>

[![tests](https://github.com/Courier-Package-Manager/Courier/actions/workflows/tests.yml/badge.svg?branch=stable)](https://github.com/Courier-Package-Manager/Courier/actions/workflows/tests.yml)


## About
Courier is a package manager that automatically detects new dependencies in your project, whilst
having the capability to manually specify requirements, requirements files etc. With the ability
to automatically request the latest version as per a schedule or to be called manually, managing
dependencies comes at little to no time cost with this tool. Courier boasts high docility with effective and efficient code. 
Please see the wiki for extensively documented details and instructions.

## Installation
The stable branch is now the main branch, if it's not a critical error (meaning it stops the functionality of a program)
then it will be worked on in `stable`. If it is _critical_, then an `issue` will be created with the
appropriate labels and a branch will be created from that issue.
See the [wiki](https://github.com/JoshuaDRose/Courier/wiki/Branches#why-delete-dev) for more
info on branches / why this change was made.


```
git clone https://github.com/JoshuaDRose/Courier
```
 > Download via https or ssh (or gh)
```
git checkout stable
```
 > Navigate to the `stable` branch if downloading from a separate branch
```
make install
```
 > Install dependencies and required files

## Features
As seen in [Trakr](https://github.com/JoshuaDRose/Trakr), a package management system
was introduced which assisted the installation and maintenance of Trakr's dependencies.
This project hopes to extend upon that package management system, and develop further
features in the hope that it will assist with the local dependency maintenance of future
projects.

Currently unit testing is in full force, with a decline in coverage since release `0.2.3`.
This is to go on for the foreseable future. There have been several changes to the 
Actions component of this project, mainly that being un-needed dependencies such as 
scrutinizer (provided coverage however codecov already provides coverage).

In relation to how these tests are impelemented in contribution or pull requests,
please see the contributing section below.


## Contributing
To contribute to a feature or bug, please clone the relative branch. If you want to lodge a
bug report or feature report, please create an issue. 

An important note: by default, logs will not show as `stable` is production-ready. It is recommended
to change the `level` key in [config.ini](config.ini) for keys `logger_root` and 
`handler_stream_handler`.

When making commits in a forked repository (with the intent of a pr) please ensure that
you read the [`commits`](commits.md) syntax file. Note that this file also generally applies
to pull requests as well. There are plans to make a contributing file in the future, however
that is nor needed or relevant right now but will be introduced if there is good reason for 
doing so. Contributions are always appreciated.

As this project is using TDD it is advisable to create test cases at the same time
as developing any feature or fixing any bug. This is only recommended, and I'll still
be accepting any PR's that pass tests, but it's preferred that they have coverage in the 
PR as well.


<!-- License + Copyright -->
<p  align="center">
  <i>© <a href="https://github.com/JoshuaDRose">Joshua Rose</a> 2023 - 2023</i><br>
  <i>Licensed under <a href="https://github.com/JoshuaDRose/Courier/blob/stable/LICENSE">MIT</a></i><br>
  <a href="https://github.com/JoshuaDRose"><img src="https://i.ibb.co/4KtpYxb/octocat-clean-mini.png" /></a><br>
  <sup>Thanks for visiting :)</sup>
</p>

