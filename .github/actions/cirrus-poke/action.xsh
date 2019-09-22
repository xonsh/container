#!/usr/bin/xonsh
import gqlmod
gqlmod.enable_gql_import()

import sys
sys.path.insert(0, "/opt/action")


source /etc/xonshrc
import cirrus

owner, repo = $GITHUB_REPOSITORY.split('/', 1)


with gqlmod.with_provider('cirrus-ci', token=$INPUT['CIRRUS_TOKEN']):
    res = cirrus.get_repo_with_builds(owner=owner, name=repo)
    assert not res.errors
    repo_id = res.data['githubRepository']['id']

    res = cirrus.start_fresh_build(repo=repo_id, branch=$INPUT['branch'])
    assert not res.errors