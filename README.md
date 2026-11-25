# makefun-news-image-20261125

[![make.fun competition](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![make.fun rank](https://make.fun/badge/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![make.fun reward](https://make.fun/badge/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the [make.fun news-image bounty](https://make.fun/bounty/news-image-20261125) (`news-image-20261125`, $100 prize pool).

`entry.png` is a single 1024×1024 cover image that sums up the world's top news stories of 25 November 2026 at a glance.

## How it works

`main.py` copies `entry.png` to `/output/entry.png` (or to the path in
the `MAKEFUN_OUTPUT` environment variable) and verifies the copy with
SHA-256, so the output is byte-identical to the source on every run.
No network access, no image processing.

```sh
python3 main.py
```
