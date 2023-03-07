<div align="center">
<h1>Courier </h1>
</div>

<div align="center">
<a href="https://codecov.io/gh/JoshuaDRose/Courier"><img src="https://img.shields.io/codecov/c/github/JoshuaDRose/courier?style=for-the-badge&token=EX3AAYPPUQ" alt="Coverage"></img></a>
<a href="https://github.com/JoshuaDRose/Courier/releases/latest"><img src="https://img.shields.io/github/v/tag/JoshuaDRose/Courier?include_prereleases&label=release&sort=semver&style=for-the-badge" alt="Version"></img></a>
<a href="https://github.com/JoshuaDRose/Courier/actions"><img src="https://img.shields.io/github/checks-status/JoshuaDRose/Courier/stable?style=for-the-badge" alt="Checks"></img></a>
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
 > Navigate to the stable branch if downloading from a separate branch
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

~~Tox is planning to make an entrance sooner or later in this project once enough code 
is written and enough substantial unit tests are introduced. The process of automating
testing will also greatly help me test less because everything is being automated. More
on this to come once unit tests are introduced.~~

Currently unit testing is in full force, with a decline in coverage since release `0.2.3`.
This is to go on for the foreseable future. There have been several changes to the 
Actions component of this project, mainly that being un-needed dependencies such as 
scrutinizer (provided coverage however codecov already provides coverage).

In relation to how these tests are impelemented in contribution or pull requests,
please see the contributing section below.


## Contributing
Please clone the 'development' branch if making changes to the code with the intent
to contribute. Alternatively you can work on 'stable' however that will not be cutting
edge and you may have to (very likely) remerge 'dev' and possibly overwrite some of the code.

Note: If you do choose to work on the stable branch (not-recommended), it is advised you at
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

## License

```
The MIT License (MIT)
Copyright (c) Joshua Rose <joshuarose099@gmail.com> 
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sub-license, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be
included install copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANT ABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
