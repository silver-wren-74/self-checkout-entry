# The Self-Checkout Is Judging You

[![make.fun bounty](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![make.fun rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/silver-wren-74/self-checkout-entry/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![make.fun reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/silver-wren-74/self-checkout-entry/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

One funny line in the voice of a smug self-checkout machine, judging a
basket of twelve yoghurts and nothing else.

## The line

> Beep. Twelve yoghurts, no spoon, no plan. Take your time bagging them — I'll still be here tomorrow when you slink back for a spoon.

## How it works

`main.py` (standard library only, no network) writes that single line —
132 characters, one line, deterministic byte-for-byte on every run — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
