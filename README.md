<div align="center">
<a href="https://github.com/JoshuaDRose/Courier/"><img alt="github-header-image" src="https://user-images.githubusercontent.com/101031214/223869242-ac1234cf-1450-426e-baa9-69955ccc28ca.png"></a>
<br>
</div>

<div align="center">
<a href="https://codecov.io/gh/JoshuaDRose/Courier" > <img src="https://codecov.io/gh/JoshuaDRose/Courier/branch/stable/graph/badge.svg?token=EX3AAYPPUQ"/> </a>
<a href="https://github.com/JoshuaDRose/Courier/actions/workflows/flake.yml"><img src="https://github.com/JoshuaDRose/Courier/actions/workflows/flake.yml/badge.svg?branch=stable"></a>
<img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/JoshuaDRose/Courier?color=teal&display_name=tag&include_prereleases&logo=github">
</div>


## About
Courier is a package manager that automatically detects new dependencies in your project, whilst
having the capability to manually specify requirements, requirements files etc. With the ability
to automatically request the latest version as per a schedule or to be called manually, managing
dependencies comes at little to no time cost with this tool. Courier boasts high docility with effective and efficient code. 

## Installation
Note before installing: the `dev` branch is very unstable and may not work. For a working
installation, download the last listed release or install from the `stable` branch.

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
Please clone the `development` branch if making changes to the code with the intent
to contribute. Alternatively you can work on `stable` however that will not be cutting
edge and you may have to (very likely) remerge `dev` and possibly overwrite some of the code.

Note: If you do choose to work on the `stable` branch (not-recommended), it is advised you at
least change the `level` key in [config.ini](config.ini) for keys `logger_root` and 
`handler_stream_handler`

When making commits in a forked repository (with the intent of a pr) please ensure that
you read the [`commits`](commits.md) syntax file. Note that this file also generally applies
to pull requests as well. There are plans to make a contributing file in the future, however
that is nor needed or relevant right now but will be introduced if there is good reason for 
doing so. Contributions are always encouraged and appreciated.

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

