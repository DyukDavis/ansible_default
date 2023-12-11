import pytest


@pytest.mark.parametrize("pkg", [
    ("podman"),
    ("containernetworking-plugins"),
])
def test_podman_is_installed(host, pkg):
    assert host.package(pkg).is_installed

def test_podman_run(host):
    assert 'Alpine Linux' in host.run("podman run --rm alpine cat /etc/os-release").stdout
