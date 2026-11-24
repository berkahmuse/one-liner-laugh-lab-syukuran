# The Toaster Holds a Grudge

[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/berkahmuse/one-liner-laugh-lab-syukuran/rank.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/berkahmuse/one-liner-laugh-lab-syukuran/reward.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

A [make.fun](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae) entry for the **One-Liner Laugh Lab** competition: a program that writes one short funny line answering a prompt.

## The prompt

The excuse a toaster gives after burning your toast.

## The line

> I burned your toast because you said 'a little darker' once, in 2019 — and I hold grudges.

90 characters, one line — the burn was no accident. The toaster remembers a throwaway "a little darker" from 2019 and has held a grudge ever since. Petty revenge, delivered deadpan.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes the line to `/output/entry.txt` (creating `/output` if needed), checks it is a single line of 1–200 characters, then reads it back to confirm the file holds exactly the line. The output is deterministic: every run produces the same bytes.

## License

MIT — see [LICENSE](LICENSE).
