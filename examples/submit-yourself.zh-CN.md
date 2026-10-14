# 实例：用 awesome-submit 把自己投稿到 awesome list

这不是模拟案例：awesome-submit 已向 **skillmatic-ai/awesome-agent-skills** 提交一条真实 PR。

- 项目：[LIghtJUNction/awesome-submit](https://github.com/LIghtJUNction/awesome-submit)
- 投稿：[Add awesome-submit · PR #205](https://github.com/skillmatic-ai/awesome-agent-skills/pull/205)
- 投稿提交：[`de3c456`](https://github.com/LIghtJUNction/awesome-agent-skills/commit/de3c456d36371947e2ce89d6b0d269787a394346)
- 核验时间：2026-10-14 UTC。
- 当时状态：**OPEN，非草稿，等待维护者审核。尚未合并、不能称为已收录。** 后续状态请以 PR 页面为准。

## 1. 安装与授权

在支持 Agent Skills 的 agent 中安装本技能。Skills CLI 会下载并执行安装器，需要 Node.js；这里给出安装方式，不代表本案例实测了 CLI 安装流程：

```sh
npx skills add LIghtJUNction/awesome-submit
```

也可以按你的 agent 文档，把本仓库放入其技能目录。实际投稿需要 `gh`、`git`、网络和你自己的 GitHub 登录：

```sh
gh auth status
```

不要把 token、密码、浏览器 cookies 或本地跟踪数据库传到 PR 或聊天里。

给 agent 的任务可以是：

> 把 https://github.com/LIghtJUNction/awesome-submit 提交到一个最匹配的 awesome list。先搜索 awesome-awesome 找大类，再找具体分类。按目标规则投稿，检查重复项，最后给我真实 PR 链接。

“帮我提交”允许针对所选列表进行必要的 fork、分支、提交、推送和 PR 操作。若只想看建议，请明确说“只找列表并给草稿，不提交”。本地写文件仍须遵守各自环境的安全和跟踪要求。

## 2. 从 awesome-awesome 找大类，再进入细分方向

先运行：

```sh
gh search repos 'awesome-awesome' --limit 10
```

本次搜索结果包含 [sindresorhus/awesome](https://github.com/sindresorhus/awesome)，这是按主题组织的综合索引，而不是让所有单个工具直接投稿的列表。

阅读索引后，确认相关大类是 Artificial Intelligence；再结合项目本身的形态——一个根目录带 `SKILL.md` 的 Agent Skill——细化到 Agent Skills，并搜索该方向：

```sh
gh search repos 'awesome agent skills' --limit 10
```

**如实记录路径：** 本次是“关键词搜索 → 综合索引/AI 大类 → 细分关键词搜索 → Agent Skills 列表”，不是声称综合索引直接链接了最终目标。索引不覆盖某个细分领域时，补充搜索即可，不要编造跳转关系。

不按 stars 数量机械选最大列表，也不把全部候选批量投稿。本案例只向一个目标提交。

## 3. 先检查资格，不符合就跳过

核对项目公开 README、`SKILL.md` 和许可证，确认它提供的是实际工作流：发现目标、核对资格、检查历史投稿、准备条目、提交并核验 PR。它是 MIT 许可证，不是一个自动保证收录的服务。

候选中，[JackyST0/awesome-agent-skills 的规则](https://github.com/JackyST0/awesome-agent-skills/blob/main/CONTRIBUTING.md)要求社区项目默认至少 64 GitHub stars。本次项目核验时为 0 stars，因此跳过，没有擅自请求例外。

最终选择 [skillmatic-ai/awesome-agent-skills](https://github.com/skillmatic-ai/awesome-agent-skills)：

- [CONTRIBUTING.md](https://github.com/skillmatic-ai/awesome-agent-skills/blob/main/CONTRIBUTING.md)接受直接关联 Agent Skills / `SKILL.md` 的资源。
- 要求链接有效、描述简短、无重复，并沿用 `[Title](URL) - Description.`。
- 检查时没有写 star 数量门槛。
- README 中 **Phase 3: Build and Integrate → Developer Tools** 是分发工作流的合理候选位置。PR 中说明这是单个 skill，不是合集，并允许维护者调整位置。

没有 star 门槛不等于自动满足主观质量要求，更不等于维护者已经同意收录。

## 4. 检查已列条目，以及开放和关闭的历史投稿

只查首页或开放 PR 不够：旧 URL、改名、已拒绝投稿都可能存在。

除了检索当前 README 的项目名、规范 URL 和可能的旧名，本次还读取了目标仓库的全部历史 PR 和 Issue 页面，并搜索项目名及作者名。实际使用了带分页的 API：

```sh
gh api --paginate \
  'repos/skillmatic-ai/awesome-agent-skills/pulls?state=all&per_page=100'

gh api --paginate \
  'repos/skillmatic-ai/awesome-agent-skills/issues?state=all&per_page=100'
```

GitHub 的 issues API 同时返回 Issue 和 PR 记录；单独读取 pulls 有助于核对 PR 信息。不要把同一条记录算成两次投稿。

本次没有发现重复条目或相关历史投稿。在创建 PR 前又复查了一遍，避免检查和提交之间出现新投稿。

如果已有开放 PR，返回其链接而不是重投；如果曾被拒绝，应先阅读原因，没有实质变化和重试授权就不要再次提交。

## 5. 只新增一条符合格式的资源

按目标规范 fork，从上游当前 `main` 建立分支，而不是直接相信 fork 的默认分支足够新。本次基线为上游提交 `cdf5ae3ff506e6f3737122bb9d24ac7d727cb6a0`；本次分支为 `add-awesome-submit-20261014`，重做案例时应重新读取当前上游并使用新的分支名。

新增条目如下：

```markdown
- [awesome-submit](https://github.com/LIghtJUNction/awesome-submit) - Skill: Submit projects to relevant awesome lists with eligibility checks, duplicate detection, and verified GitHub pull requests.
```

没有改动其他条目、重排整个文件、增加广告段落或修改工作流。PR 正文说明项目用途、分类依据、检查内容，并披露作者与项目的关系和 AI 辅助。

在干净的目标 checkout 中检查：

```sh
git diff --check
git diff --stat
git diff
```

目标仓库只有文档和静态资源，没有配置本地构建/测试工作流。本项目另运行了 `python3 scripts/validate.py`，通过元数据、文件链接和七个场景定义的结构检查。**这不是七次 agent 行为测试，也不是独立模型评测。**

提交、推送后，显式指定上游与 base/head 创建 PR，避免误向自己的 fork 投稿。本案例运行的是：

```sh
gh pr create \
  --repo skillmatic-ai/awesome-agent-skills \
  --base main \
  --head LIghtJUNction:add-awesome-submit-20261014 \
  --title 'Add awesome-submit' \
  --body-file PATH_TO_REVIEWED_PR_BODY
```

`PATH_TO_REVIEWED_PR_BODY` 是占位符，必须替换为你已审阅的正文文件。本教程记录的是已经发生的投稿，不要直接重新执行写操作制造重复 PR。

## 6. 从远端验证，不只相信命令成功

创建 PR 后读取其状态和真正的远端 diff：

```sh
gh pr view 205 --repo skillmatic-ai/awesome-agent-skills \
  --json url,state,isDraft,mergedAt,baseRefName,headRefName,headRepositoryOwner,files

gh pr diff 205 --repo skillmatic-ai/awesome-agent-skills
```

本次确认：

- 目标仓库正确：`skillmatic-ai/awesome-agent-skills`，base 为 `main`。
- head 为作者 fork 的 `add-awesome-submit-20261014`。
- 仅修改 `README.md`，新增 1 行，删除 0 行。
- 状态为 `OPEN`、`isDraft=false`、`mergedAt=null`。

所以正确表述是：**已提交 PR #205，等待维护者审核。** 不是“已经被 awesome list 收录”。即便后来合并，也应检查上游默认分支的实际条目；生成的网站是否上线又是另一个状态。

## 7. 把过程分享出去时，不扩大结果

适合分享的是：真实任务、搜索路径、被跳过的门槛、最终一行 diff、PR 链接和当前状态。不要把“发出投稿”包装成“获得官方背书”。

本次随后实际使用 Playwright 扩展连接用户授权的现有 Chrome，在 `@LIghtJUNction_x` 发布了 5 条连续回复。没有重启 Chrome、创建新的浏览器窗口或复制登录资料。

本环境使用的 Playwright CLI 支持以下入口（不同版本应先检查 `--help attach`）：

```sh
playwright-cli -s=awesome-submit-x attach --extension=chrome
```

扩展需要授权连接；本次使用用户提供的 `PLAYWRIGHT_MCP_EXTENSION_TOKEN` 环境变量完成连接。**不要将令牌值写入命令示例、仓库或教程；扩展连接 URL、快照和本地日志也可能包含该值，应按敏感材料处理，分享前检查并脱敏。** 发帖不要求额外开放 Chrome 的 TCP 调试端口。

实际操作路径：

1. 打开 X，读取当前账号的个人页链接，确认是用户自己的账号；检查最近帖子，避免重复推广。
2. 在首页编辑器填写首帖，核对文本长度、链接和发布按钮状态；本次未使用加载异常的独立撰写弹窗。
3. 点击发布后读取页面中的已发布正文和 `/status/…` 链接，不把点击成功当成发布成功。
4. 依次打开上一条的永久链接，在其回复编辑器发布下一条；必要时将该标签页带到前台，避免后台页面的稳定性检查超时。
5. 遇到超时先检查已发布帖子、编辑器和页面状态，不盲目重试发布动作；本次没有把首帖超时包装成成功。

实际发布结果：

- [1/5：项目介绍](https://x.com/LIghtJUNction_x/status/2110439146447876528)
- [2/5：从大类到细分类](https://x.com/LIghtJUNction_x/status/2110439328623259893)
- [3/5：资格筛选](https://x.com/LIghtJUNction_x/status/2110439556491387145)
- [4/5：真实 PR，仍待审核](https://x.com/LIghtJUNction_x/status/2110439666969440280)
- [5/5：教程链接与安装方式](https://x.com/LIghtJUNction_x/status/2110439779901063233)

[发布文案与链接记录](x-thread.zh-CN.md)保留了这次串的全文。GitHub 投稿、X 发帖和维护者接受投稿是三个独立结果：前两项已实际完成，最后一项仍以 PR 当前状态为准。

## 可复用的结束检查

- 资格与许可证来自当前证据，硬性门槛不满足就跳过。
- 查看现有条目及开放、关闭的历史投稿。
- 最小 diff、准确描述、必要披露。
- 从当前上游建立分支，显式选择 PR 目标。
- 本地检查与远端状态都验证；超时先检查远端再重试。
- 分清草稿、已提交、已合并、已收录、网站已上线。
- 保留交付物和必要证据；本地临时 checkout 不等于获准自动删除。
