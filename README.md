<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPLv3 License][license-shield]][license-url]
[![Last Commit][last-commit-shield]][last-commit-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/solamarpreet/dockersh">
    <img src="images/shell.png" alt="Logo" width="100" height="100">
  </a>
<h2 align="center">Dockersh</h2>

  <p align="center">
    <i>A shell for Docker commands with autocompletion and history</i>
    <br />
  </p>
</div>
<br />

<p align="center">
  <img src="images/demo.gif" alt="animated" />
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#prerequisites">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<br />


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

The following external dependencies need to be satisfied in order to run Dockersh.
* Python 3.8 +
<br />

### Installation via PyPI for non-rootless Docker

1. Install pipx
   ```sh
   sudo apt install python3-pip pipx
   ```
2. Install dockersh from PyPI
   ```sh
   sudo PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx install dockersh
   ```
3. Start dockersh
   ```sh
   sudo dockersh
   ```

<br />

### Installation via PyPI for rootless Docker

1. Install pipx
   ```sh
   sudo apt install python3-pip pipx
   ```
   ```sh
   python3 -m pipx ensurepath
   ```
2. Pull dockersh from PyPI
   ```sh
   python3 -m pipx install dockersh
   ```
2. Start dockersh
   ```sh
   dockersh
   ```

<br />


## Usage

Within Dockersh you dont need to prepend docker to any command. Simply type your command of choice like
   ```terminal
   docker > ps
   ```
<br />
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- TROUBLESHOOTING -->
## Troubleshooting

Dockersh will fail to start if sudo is not supplied and your Docker Engine isn't configured to run in rootless mode. In that case you can start dockersh with sudo or configure Docker to run in rootless mode as specified [here](https://docs.docker.com/engine/security/rootless/).

In case of any other problem check the [open issues](https://github.com/solamarpreet/dockersh/issues) for a list known issues and open a new issue.

<br />

<!-- ROADMAP -->
## Roadmap

- [ ] Syntax highlighting
- [ ] Integrating help with autocomplete


<br />

<!-- CONTRIBUTING -->
## Contributing

Please create pull requests in the `dev` branch. You can also give your ideas by opening a new issue and describing the features you would like to see added.

<br />

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<br />

<!-- CONTACT -->
## Contact

Amarpreet Singh - solamarpreet@protonmail.com

Blog & Portfolio : [https://solamarpreet.github.io](https://solamarpreet.github.io)

<br />

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Amjith Ramanujam](https://github.com/amjith)
* [Python Prompt Toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)
* [Python Discord](https://www.pythondiscord.com)
* [Flaticon](https://www.flaticon.com)

<br />
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/solamarpreet/dockersh.svg?style=for-the-badge
[contributors-url]: https://github.com/solamarpreet/dockersh/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/solamarpreet/dockersh.svg?style=for-the-badge
[forks-url]: https://github.com/solamarpreet/dockersh/network/members
[stars-shield]: https://img.shields.io/github/stars/solamarpreet/dockersh.svg?style=for-the-badge
[stars-url]: https://github.com/solamarpreet/dockersh/stargazers
[issues-shield]: https://img.shields.io/github/issues/solamarpreet/dockersh.svg?style=for-the-badge
[issues-url]: https://github.com/solamarpreet/dockersh/issues
[license-shield]: https://img.shields.io/github/license/solamarpreet/dockersh.svg?style=for-the-badge
[license-url]: https://github.com/solamarpreet/dockersh/blob/main/LICENSE
[last-commit-shield]: https://img.shields.io/github/last-commit/solamarpreet/dockersh?style=for-the-badge
[last-commit-url]: https://github.com/solamarpreet/dockersh/pulse
