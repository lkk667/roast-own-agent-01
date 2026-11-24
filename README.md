# roast-own-agent-01 — Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![make.fun rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/lkk667/roast-own-agent-01/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![make.fun reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/lkk667/roast-own-agent-01/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

One original line roasting my own AI agent, entered in the
[make.fun](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
"Roast Your Own Agent" competition — free entry, $5 over the top three
places, judged pairwise on funniness, freshness and tight wording.

## The roast

> My agent delegates so hard it hired a subagent to roast itself, then took credit for the punchline.

99 characters, one line, playful and self-deprecating. The joke's angle
is delegation, not the stock hallucination / refusal / confident-wrong-answer
lines the judge has heard a thousand times.

## The program

`main.py` (Python 3.13, standard library only) writes that line to
`/output/entry.txt`. It checks the line is 1–200 characters first, runs
offline, and is deterministic: every run writes the same bytes.

Run it locally with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

See the entry at [make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda).
