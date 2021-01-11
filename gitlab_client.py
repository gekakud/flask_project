import gitlab
import common


class GitLabClient:

    def get_all_commits_for_branch(self, since_date="2020-01-01T00:00:00Z"):
        cms = self.project.commits.list(all=True, query_parameters={'ref_name': self.branch_name, 'since': since_date})
        # branch = self.project.branches.get(self.branch_name)
        return cms

    def get_commit_by_sha(self, sha):
        commits = self.get_all_commits_for_branch()
        for commit in commits:
            if commit.id == sha:
                return commit

        return None

    def __init__(self, gitlab_url, gitlab_token, branch):
        self.gl = gitlab.Gitlab(gitlab_url, private_token=gitlab_token, api_version=4)
        self.gl.auth()

        self.project = self.gl.projects.get(common.project_id)
        self.branch_name = branch


gl_client = GitLabClient(common.gl_url, common.gl_token, common.branch_name)

# commits = gl_client.get_all_commits_for_branch()
my_commit = gl_client.get_commit_by_sha("d2055702cd4cfce33231c72c5886d1cca62a1345")
# cms[0].id, title, message, author_name, created_at
my_commit_title = my_commit.title
my_commit_message = my_commit.message
my_commit_created_at = my_commit.created_at
my_commit_author = my_commit.author_name

print("haha")