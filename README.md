# awesome-submit

An agent skill for submitting your projects to relevant awesome lists with verified, policy-compliant GitHub pull requests.

把自己的项目推荐到合适的 awesome list：先核对资格和重复投稿，再按目标规范提交 PR，并验证远端结果。**已提交不等于已收录。**

## Install

Using the Skills CLI (requires Node.js; downloads and runs the CLI):

```sh
npx skills add LIghtJUNction/awesome-submit
```

Or clone this repository into a skill directory supported by your agent. For agents that support `~/.agents/skills`:

```sh
git clone https://github.com/LIghtJUNction/awesome-submit.git ~/.agents/skills/awesome-submit
```

The repository root contains `SKILL.md`. Other agents may use a different skill directory; follow their documentation. Restart or refresh skill discovery if necessary.

## Use

Ask your agent, for example:

- “把我的 https://github.com/OWNER/PROJECT 提交到最合适的 awesome list。”
- “把 cpyref 和 AgentGC 推荐到这个列表：https://github.com/OWNER/LIST。”
- “先找 3 个适合我的项目的 awesome list，只给草稿，不提交。”
- “检查上次的投稿，已经有 PR 就不要重复提交。”

The agent needs authenticated `gh`, `git`, and network access. It uses your existing GitHub identity; this skill does not collect credentials or run a hosted service. Actual submission creates public GitHub contributions under your account. Requests for discovery or drafts do not authorize those writes.

## Workflow

1. Identify the public project and verify its documented capabilities and license.
2. Use the supplied target, or shortlist up to five relevant lists and select one eligible target by default.
3. Read contribution rules, templates, category conventions and eligibility requirements.
4. Search existing entries and open/closed nominations.
5. Prepare the smallest valid change and run relevant local checks.
6. Fork, branch, commit, push and submit once; fetch the remote PR and diff to verify the result.

Hard eligibility failures, closed submissions and prohibitions on self-promotion or automation stop submission to that target. Private projects are not made public. No mass posting, fabricated claims, maintainer spam, auto-merging, CI reruns or automatic cleanup.

This is an instruction skill, not an unattended daemon or a guarantee of acceptance. It does not add a scheduled task. List maintainers decide whether to accept a contribution.

## Files and validation

- [`SKILL.md`](SKILL.md): portable workflow and safety boundaries.
- [`evals/evals.json`](evals/evals.json): scenario prompts and expected outcomes; test with fixtures or read-only/dry-run tools, not live unsolicited PRs.
- [`scripts/validate.py`](scripts/validate.py): dependency-free structural and scenario checks.

Run local structural validation:

```sh
python3 scripts/validate.py
```

These checks validate the package structure and test-case coverage, not model behavior or live GitHub submissions. No independent agent benchmark is claimed.

## License

MIT. See [LICENSE](LICENSE).
