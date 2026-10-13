# Character file format

Characters are Markdown files with a small YAML-like header. The browser demo keeps an equivalent data object in `lobby/index.html` so it can run without a build step.

```text
id: unique-slug
name: Display Name
subtitle: One-line combat identity
color: #00e5ff
max_hp: 100
max_energy: 3
passive: passive-id
bio: Short flavor text
```

## Passives

- `overclock`: Charge restores an additional energy on success.
- `echo-guard`: Guard reflects one extra point of blocked damage.
- `static-heart`: The first glitch each battle deals one less damage.
