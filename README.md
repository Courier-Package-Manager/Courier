<div align="center">
<h1>Courier </h1>
Package manager for Python
<h3></h3>
</div>

<div align="center">
<a href="https://codecov.io/gh/JoshuaDRose/Courier"><img src="https://img.shields.io/codecov/c/github/JoshuaDRose/courier?style=for-the-badge&token=EX3AAYPPUQ" alt="Coverage"></img></a>
<a href="https://codecov.io/gh/JoshuaDRose/Courier"><img src="https://img.shields.io/scrutinizer/quality/g/JoshuaDRose/Courier/master?style=for-the-badge&label=scrutinizer" alt="Quality"></img></a>
<a href="https://github.com/JoshuaDRose/Courier/releases/latest"><img src="https://img.shields.io/github/v/tag/JoshuaDRose/Courier?include_prereleases&label=release&sort=semver&style=for-the-badge" alt="Version"></img></a>
<a href="https://github.com/JoshuaDRose/Courier/actions"><img src="https://img.shields.io/github/checks-status/JoshuaDRose/Courier/stable?style=for-the-badge" alt="Checks"></img></a>
</div>




## About
Courier is a package manager that automatically detects new dependencies in your project, whilst
having the capability to manually specify requireements, requirements files etc. With the ability
to automatically request the latest version as per a schedule or to be called manually, managing
dependenies comes at little to no time cost with this tool. Courier boasts high docility with effective and efficient code. 

## Coverage
![coverage-sunburst](https://codecov.io/gh/JoshuaDRose/Courier/branch/stable/graphs/sunburst.svg?token=EX3AAYPPUQ)
![coverage-grid](https://codecov.io/gh/JoshuaDRose/Courier/branch/stable/graphs/tree.svg?token=EX3AAYPPUQ)
![coverage-icicle](https://codecov.io/gh/JoshuaDRose/Courier/branch/stable/graphs/icicle.svg?token=EX3AAYPPUQ)

## Installation
Note before installing: the `stable` branch is very unstable and may not work. For a working
installation, download the last listed release.

```
git clone https://github.com/JoshuaDRose/Courier
```
 > Download via https or ssh (or gh)
```
git checkout stable
```
 > Navigate to the stable branch if downloading from a seperate branch
```
make install
```
 > Install dependencies and required files

## Features
As seen in [Trakr](https://github.com/JoshuaDRose/Trakr), a package management system
was introduced which assisted the installation and maintance of Trakr's dependencies.
This project hopes to extend upon that package management system, and develop further
features in the hope that it will assist with the local dependency maintaince of future
projects.

Tox is planning to make an entrance sooner or later in this project once enough code 
is written and enough substantial unit tests are introduced. The process of automating
testing will also greatly help me test less because everything is being automated. More
on this to come once unit tests are introduced.
## Contributing
When making commits in a forked repository (with the intent of a pr) please ensure that
you read the [commits](commits.md) syntax file. Note that this file also generally applies
to pull requests as well. There are plans to make a contributing file in the future, however
that is nor needed or relevant right now but will be introduced if there is good reason for 
doing so. Contributions are always encouraged and appreciated.

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
