import pytest


@pytest.mark.parametrize("rule", [
    ("-A ANSIBLE-FORWARD -s 127.0.0.1/32 -i eth0 -p tcp -m tcp --dport 9115 -j ACCEPT"),
    ("-A ANSIBLE-INPUT -s 192.168.0.0/16 -p tcp -m tcp --dport 22 -j ACCEPT"),
    ("-A ANSIBLE-FORWARD -s 10.0.0.0/8 -o eth0 -j ACCEPT"),
    ("-A ANSIBLE-POSTROUTING -s 10.0.0.0/8 -o eth0 -j MASQUERADE")
])
def test_iptables_rules(host, rule):
    iptables_save = host.run("iptables-save")
    assert rule in iptables_save.stdout
