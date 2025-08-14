kvm_host_ubuntu_packages = [
    "bridge-utils",
    "libvirt-clients",
    "libvirt-daemon-system",
    "virt-manager",
]
# qemu-kvm is a virtual package and cant be checked

kvm_host_ubuntu_services = ["libvirtd"]


def test_installed_packages(host):
    match host.system_info.distribution:
        case "ubuntu":
            for package in kvm_host_ubuntu_packages:
                pkg = host.package(package)
                assert pkg.is_installed
                # assert pkg.version.startswith("1:")


def test_running_services(host):
    match host.system_info.distribution:
        case "ubuntu":
            for service in kvm_host_ubuntu_services:
                svc = host.service(service)
                assert svc.is_running
                assert svc.is_enabled


def test_vagrant_user_in_libvirt_group(host):
    vagrant_user = host.user("vagrant")
    groups = vagrant_user.groups
    assert "kvm" in groups
    assert "libvirt" in groups
