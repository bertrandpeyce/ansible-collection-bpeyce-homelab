msoft_azure_dev_packages = ["azure-cli"]

def test_msoft_azure_dev_installed_packages(host):
    for package in msoft_azure_dev_packages:
        assert host.package(package).is_installed

def test_msoft_azure_dev_command_available(host):
    az_cmd = host.run("az --version")
    assert az_cmd.rc == 0
    assert "azure-cli" in az_cmd.stdout
