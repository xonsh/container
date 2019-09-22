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
    assert not res.errors, repr(res.errors)
    repo_id = res.data['githubRepository']['id']

    res = cirrus.start_fresh_build(
        repo=repo_id, branch=$INPUT['BRANCH'], mut=f"rebuild-{repo_id}",
    )
    assert not res.errors, repr(res.errors)

    print(f"Started build https://cirrus-ci.com/build/{res.data['createBuild']['build']['id']}")
