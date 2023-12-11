import pytest


@pytest.mark.parametrize("pkg", [
    ("docker-ce"),
    ("docker-ce-cli"),
])
def test_docker_is_installed(host, pkg):
    assert host.package(pkg).is_installed

def test_docker_compose_installed(host):
    assert 'docker-compose version' in host.run("docker-compose --version").stdout

def test_docker_service_enabled(host):
    assert host.service("docker").is_enabled

def test_docker_service_running(host):
    assert host.service("docker").is_running

def test_docker_run(host):
    assert 'Alpine Linux' in host.run("docker run --rm alpine cat /etc/os-release").stdout
