workflow "Test and upload on tag" {
  on = "push"
  resolves = ["Uploads to Docker Hub"]
}

action "Filter tag" {
  uses = "actions/bin/filter@master"
  args = "tag"
}

action "Test 3.5" {
  uses = "orangutangaming/actions/pytest-install-35@master"
  needs = ["Filter tag"]
}

action "Test 3.6" {
  uses = "orangutangaming/actions/pytest-install-36@master"
  needs = ["Filter tag"]
}

action "Test 3.7" {
  uses = "orangutangaming/actions/pytest-install-37@master"
  needs = ["Filter tag"]
}

action "Twine upload" {
  uses = "orangutangaming/actions/twine-upload@master"
  secrets = ["TWINE_USERNAME", "TWINE_PASSWORD"]
  needs = ["Test 3.5", "Test 3.6", "Test 3.7"]
}

action "Uploads to Docker Hub" {
  uses = "pangzineng/Github-Action-One-Click-Docker@master"
  needs = ["Twine upload"]
  env = {
    DOCKER_USERNAME = "orangutan"
    DOCKER_IMAGE_NAME = "pma"
    DOCKER_NAMESPACE = "orangutan"
  }
  secrets = ["DOCKER_PASSWORD"]
}
