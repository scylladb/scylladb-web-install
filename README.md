# ScyllaDB Web Install

installation Welcome to ScyllaDB Web Install repository!  

ScyllaDB Web Install is a platform-agnostic script that allows an easy installation of [ScyllaDB](https://www.scylladb.com/) on different Operating System and architectures.  
For more information, ScyllaDB Web Install user doc can be found [here](https://opensource.docs.scylladb.com/stable/getting-started/installation-common/scylla-web-installer.html).

## Usage
To install the latest stable open source version, run:
```shell
curl -sSf https://get.scylladb.com/server | sudo bash
```
The script will automatically detect your operating system and will install all the required packages / dependencies.  
At the end of the successful installation, the message `Scylla installation done!` will be displayed.

#### Additional options:
- `[--scylla-version <version>]` to install a specific ScyllaDB version.
In `<version>`, specify `(x.y)` version to install the latest patch for this version or `(x.y.z)` to install a specific patch release. In addition, there is an option to install the latest nightly version by specify `nightly-<version>`.
- `[--scylla-product <scylla|scylla-enterprise>]` to install specific ScyllaDB product. Default is ScyllaDB OSS.
- `[--scylla-repo-file-url <url>]` allow to download and install ScyllaDB product from a custom `scylla.list` or `scylla.repo` file.
- `[--verbose]` to get more information during the installation run.
- `[--dry-run]` prints only the commands and the installation flow without actually installing it, useful for verification.

#### Examples:
Installing ScyllaDB Open Source version 5.4.8:
```shell
curl -sSf get.scylladb.com/server | sudo bash -s -- --scylla-version 5.4.8
```
Installing ScyllaDB Enterprise latest patch of version 2024.1:
```shell
curl -sSf get.scylladb.com/server | sudo bash -s -- --scylla-product scylla-enterprise --scylla-version 2024.1
```
Running an installation of nightly version 6.0 in dry-run:
```shell
curl -sSf get.scylladb.com/server | sudo bash -s -- --scylla-version nightly-6.0 --dry-run
```

## Supported OSs by Platform and Version
Ensure your platform is supported by ScyllaDB version you want to install.
* For ScyllaDB Open Source - see [OS Support by Platform and Version for OSS](https://opensource.docs.scylladb.com/stable/getting-started/os-support.html).
* For ScyllaDB Enterprise - see [OS Support by Platform and Version for Enterprise](https://enterprise.docs.scylladb.com/stable/getting-started/os-support.html).

## Contributing
We welcome public/internal contributions into this repository via pull requests.  
Please note that before we merge your pull request, you must validate your changes locally by
running the script and in addition, it must pass all the internal [CI Tests](.github/workflows/test.yml).

## License
This project is distributed under the Apache 2.0 license. For more details, see the [LICENSE](LICENSE) file.

testing. Do not merge this.
