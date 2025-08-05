

def test_gitlab_installed_packages(host):
    # Check if the GitLab package is installed
    gitlab_packages = ["gitlab-ce"]
    for package in gitlab_packages:
         assert host.package(package).is_installed

def test_gitlab_service_running_and_enabled(host):
    # Check if the GitLab service is running and enabled
    gitlab_service = host.service("gitlab-runsvdir")
    assert gitlab_service.is_running
    assert gitlab_service.is_enabled
