import pytest


def test_pip_installed(host):
    assert host.package("python3-pip").is_installed

@pytest.mark.parametrize("pkg", [
    ("cryptography"),
    ("boto"),
])
def test_pip_packages(host, pkg):
    pkgs = host.pip.get_packages()
    assert pkg in host.pip.get_packages()

@pytest.mark.parametrize("pkg", [
    ("ca-certificates"),
    ("python3-pip"),
    ("nano"),
    ("curl"),
    ("smartmontools"),
    ("git"),
])
def test_apt_packages(host, pkg):
    assert host.package(pkg).is_installed
