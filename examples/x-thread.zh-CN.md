# X 推广与实战教程串（待发布草稿）

状态：尚未通过 X 帖子永久链接验证发布。下面每段为一条帖子；按顺序组成一个串，不要全部塞进单条。发布后应核实账号、正文和各条永久链接，再另行记录结果。

## 1/5 — 项目

做了个 Agent Skill：awesome-submit。让 agent 帮自己的项目找合适的 awesome list、查规则与重复投稿，再创建并核验 PR。
不是群发器，也不保证收录。
这次让它给自己投稿，记录了真实过程👇
https://github.com/LIghtJUNction/awesome-submit

## 2/5 — 发现

第一步不是盲投最大列表。
先搜 awesome-awesome，找综合索引和大类，再按项目形态细化到 Agent Skills。
索引没直接链接目标，就补细分搜索，不编造跳转路径。
这条“大类 → 细分类”的方法已写进技能。

## 3/5 — 资格

查规则比写推荐语更重要。
一个候选列表要求社区项目默认至少 64 stars；我的新项目当时 0 stars，直接跳过，没有擅自求例外。
最终选了相关且未写 star 门槛的列表，再检查现有条目及全部开放、关闭的历史投稿。

## 4/5 — 真实投稿

只加一行 README，披露作者身份与 AI 辅助，并从远端核验 diff。
真实 PR：
https://github.com/skillmatic-ai/awesome-agent-skills/pull/205
本次核验时是 OPEN、等待审核。已提交 ≠ 已收录，更不等于维护者背书。

## 5/5 — 教程

完整教程含发现路径、跳过原因、实际条目、检查命令和 PR 状态验证。
安装：npx skills add LIghtJUNction/awesome-submit
教程：
https://github.com/LIghtJUNction/awesome-submit/blob/main/examples/submit-yourself.zh-CN.md
