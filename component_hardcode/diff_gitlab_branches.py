"""
对比功能分支与主分支的文件差异
官网文档: https://docs.gitlab.com/ce/api/repositories.html#compare-branches-tags-or-commits
"""

# /api/v4/projects/43/repository/compare?from=1.3.9.20201026&to=master
import requests


def compare_gitlab_branches(url_prefix, branches_from, branches_to):
    req = requests.get(
        url_prefix + "/api/v4/projects/%s/repository/compare?from=%s&to=%s" % (url_prefix, branches_from, branches_to))
    return req.json()


if __name__ == '__main__':
    print(compare_gitlab_branches("http://git.wjh.com", "1.3.9.20201026", "master"))
