#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║           MailMultiply — Email Alias Generator               ║
║                  Developed by Mr_ofcodyx                     ║
╚══════════════════════════════════════════════════════════════╝
"""

import sys
import os
import re
import random
import itertools
import argparse
from pathlib import Path

# ─── ANSI Colors ───────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[1;91m"
    GREEN   = "\033[1;92m"
    YELLOW  = "\033[1;93m"
    CYAN    = "\033[1;96m"
    WHITE   = "\033[1;97m"
    BLUE    = "\033[1;94m"
    MAGENTA = "\033[1;95m"
    DIM     = "\033[2m"

def supports_color() -> bool:
    """Check if the terminal supports color output."""
    return sys.stdout.isatty() and os.environ.get("TERM") != "dumb"

if not supports_color():
    for attr in vars(C):
        if not attr.startswith("__"):
            setattr(C, attr, "")

# ─── Banner ────────────────────────────────────────────────────
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""
{C.CYAN}╔{'═'*62}╗
║{C.WHITE}                                                              {C.CYAN}║
║{C.YELLOW}   ███╗   ███╗ █████╗ ██╗██╗     ███╗   ███╗██╗   ██╗         {C.CYAN}║
║{C.YELLOW}   ████╗ ████║██╔══██╗██║██║     ████╗ ████║██║   ██║         {C.CYAN}║
║{C.WHITE}   ██╔████╔██║███████║██║██║     ██╔████╔██║██║   ██║         {C.CYAN}║
║{C.WHITE}   ██║╚██╔╝██║██╔══██║██║██║     ██║╚██╔╝██║██║   ██║         {C.CYAN}║
║{C.RED}   ██║ ╚═╝ ██║██║  ██║██║███████╗██║ ╚═╝ ██║╚██████╔╝         {C.CYAN}║
║{C.RED}   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝          {C.CYAN}║
║{C.WHITE}                                                              {C.CYAN}║
║{C.CYAN}   ✉  {C.GREEN}M U L T I P L Y{C.WHITE}  —  Email Alias Generator               {C.CYAN}║
║{C.WHITE}                                                              {C.CYAN}║
║{C.DIM}               ┌─────────────────────────────┐                {C.CYAN}║
║{C.DIM}               │  you@gmail.com              │                {C.CYAN}║
║{C.DIM}               │  y.ou@gmail.com             │                {C.CYAN}║
║{C.DIM}               │  you+alias@gmail.com  ✓     │                {C.CYAN}║
║{C.DIM}               └─────────────────────────────┘                {C.CYAN}║
║{C.WHITE}                                                              {C.CYAN}║
║{C.YELLOW}            Developed by: {C.RED}Mr_ofcodyx                          {C.CYAN}║
╚{'═'*62}╝{C.RESET}
""")

# ─── Email Validation ──────────────────────────────────────────
EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$"
)

def validate_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))

# ─── Alias Generation (dot-trick) ─────────────────────────────
def dot_variants(name: str) -> list[str]:
    """
    Generates all dot-insertion variants for a username.
    E.g. 'abc' → ['abc', 'a.bc', 'ab.c', 'a.b.c']
    Uses itertools for correctness and performance.
    """
    if len(name) <= 1:
        return [name]

    # Every position between characters can have a dot or not
    gaps = len(name) - 1
    variants = []
    for mask in range(1 << gaps):
        parts = [name[0]]
        for i in range(gaps):
            if mask & (1 << i):
                parts.append(".")
            parts.append(name[i + 1])
        variants.append("".join(parts))
    return variants

# ─── Plus-alias Generation ────────────────────────────────────
PLUS_ALIASES = [
    "work", "home", "news", "shop", "spam", "social",
    "promo", "alerts", "noreply", "info", "test", "dev",
    "signup", "login", "orders", "support", "newsletter",
    "updates", "offers", "deals", "inbox", "primary",
    "school", "gaming", "finance", "travel", "health",
    "music", "movies", "sports", "tech", "lists",
]

def plus_variants(name: str, domain: str, count: int) -> list[str]:
    """Generate plus-trick aliases like name+alias@domain."""
    chosen = random.sample(PLUS_ALIASES, min(count, len(PLUS_ALIASES)))
    return [f"{name}+{alias}@{domain}" for alias in chosen]

# ─── Core Generator ───────────────────────────────────────────
def generate_aliases(email: str, count: int) -> list[str]:
    """
    Generate `count` unique email aliases for the given email.
    Mixes dot-trick variants and plus-trick aliases.
    """
    name, domain = email.rsplit("@", 1)

    all_dot = dot_variants(name)
    all_dot_emails = [f"{v}@{domain}" for v in all_dot]

    max_dot = len(all_dot_emails)
    dot_count = min(count, max_dot)
    plus_count = max(0, count - dot_count)

    # Pick random dot variants (always include the original)
    chosen_dot = random.sample(all_dot_emails, dot_count)
    if email not in chosen_dot:
        chosen_dot[0] = email

    chosen_plus = plus_variants(name, domain, plus_count)

    result = list(dict.fromkeys(chosen_dot + chosen_plus))  # deduplicate, preserve order
    random.shuffle(result)
    return result[:count]

# ─── Display ──────────────────────────────────────────────────
def display_results(aliases: list[str], email: str):
    name = email.split("@")[0]
    print(f"\n{C.CYAN}┌{'─'*56}┐")
    print(f"│{C.WHITE}  ✉  Generated Aliases for {C.YELLOW}{email:<28}{C.CYAN}│")
    print(f"├{'─'*56}┤{C.RESET}")
    for i, alias in enumerate(aliases, 1):
        marker = f"{C.GREEN}✓{C.RESET}"
        num = f"{C.DIM}{i:>3}.{C.RESET}"
        print(f"{C.CYAN}│{C.RESET} {num} {marker} {C.WHITE}{alias:<48}{C.CYAN}│{C.RESET}")
    print(f"{C.CYAN}└{'─'*56}┘{C.RESET}")
    print(f"\n{C.GREEN}  Total: {len(aliases)} aliases generated.{C.RESET}")

# ─── Save Output ──────────────────────────────────────────────
def save_output(aliases: list[str], name: str) -> Path:
    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f"{name}.lst"
    out_file.write_text("\n".join(aliases) + "\n", encoding="utf-8")
    return out_file

# ─── Interactive Mode ─────────────────────────────────────────
def prompt(msg: str) -> str:
    try:
        return input(f"{C.WHITE}[{C.GREEN}*{C.WHITE}]{C.GREEN} {msg}: {C.WHITE}").strip()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{C.RED}\n  [!] Interrupted. Exiting.{C.RESET}\n")
        sys.exit(0)

def interactive():
    banner()

    while True:
        email = prompt("Enter email address")
        if not validate_email(email):
            print(f"{C.WHITE}[{C.RED}!{C.WHITE}]{C.RED} Invalid email address. Try again.{C.RESET}\n")
            continue
        break

    while True:
        raw = prompt("Number of aliases to generate")
        if raw.isdigit() and int(raw) > 0:
            count = int(raw)
            break
        print(f"{C.WHITE}[{C.RED}!{C.WHITE}]{C.RED} Please enter a positive integer.{C.RESET}\n")

    print(f"\n{C.WHITE}[{C.RED}!{C.WHITE}]{C.RED} Generating...{C.RESET}")
    aliases = generate_aliases(email, count)
    display_results(aliases, email)

    save = prompt("\nSave output to file? (y/n)").lower()
    if save == "y":
        name = email.split("@")[0]
        path = save_output(aliases, name)
        print(f"{C.WHITE}[{C.YELLOW}*{C.WHITE}]{C.YELLOW} Output saved at: {C.WHITE}{path}{C.RESET}")

    print(f"{C.WHITE}[{C.RED}!{C.WHITE}]{C.RED} Done.\n{C.RESET}")

# ─── Custom Help ──────────────────────────────────────────────
def print_help():
    w = C.WHITE; g = C.GREEN; y = C.YELLOW; c = C.CYAN
    r = C.RED;   d = C.DIM;   R = C.RESET; m = C.MAGENTA

    print(f"""
{c}╔{'═'*62}╗
║{w}  ✉  MailMul — Email Alias Generator                          {c}║
║{d}  Developed by: {r}Mr_ofcodyx{d}                                    {c}║
╠{'═'*62}╣
║{w}                                                              {c}║
║{y}  USAGE{w}                                                       {c}║
║{d}  ──────────────────────────────────────────────────────────  {c}║
║{g}    python mailmul.py {w}[OPTIONS]                               {c}║
║{w}                                                              {c}║
╠{'═'*62}╣
║{w}                                                              {c}║
║{y}  OPTIONS{w}                                                     {c}║
║{d}  ──────────────────────────────────────────────────────────  {c}║
║{w}                                                              {c}║
║  {g}-e{w}, {g}--email   {m}<addr>{w}   Target email address                 {c}║
║{d}                       e.g. user@gmail.com                    {c}║
║{w}                                                              {c}║
║  {g}-n{w}, {g}--number  {m}<int> {w}   Aliases to generate  {d}(default: 10)   {c}║
║{d}                       e.g. -n 50                             {c}║
║{w}                                                              {c}║
║  {g}-s{w}, {g}--save         {w}   Save output to {d}output/<name>.lst      {c}║
║{w}                                                              {c}║
║  {g}-q{w}, {g}--quiet        {w}   Suppress banner {d}(pipe-friendly)       {c}║
║{w}                                                              {c}║
║  {g}-h{w}, {g}--help         {w}   Show this help message                {c}║
║{w}                                                              {c}║
╠{'═'*62}╣
║{w}                                                              {c}║
║{y}  EXAMPLES{w}                                                    {c}║
║{d}  ──────────────────────────────────────────────────────────  {c}║
║{w}                                                              {c}║
║  {d}# Interactive mode (no args){w}                                {c}║
║  {g}python mailmul.py{w}                                           {c}║
║{w}                                                              {c}║
║  {d}# Generate 20 aliases and save to file{w}                      {c}║
║  {g}python mailmul.py {w}-e {m}user@gmail.com {w}-n {m}20 {w}-s                {c}║
║{w}                                                              {c}║
║  {d}# Pipe output to another tool{w}                               {c}║
║  {g}python mailmul.py {w}-e {m}user@gmail.com {w}-n {m}30 {w}-q {w}> out.txt      {c}║
║{w}                                                              {c}║
║  {d}# Generate 100 aliases quietly{w}                              {c}║
║  {g}python mailmul.py {w}-e {m}user@domain.com {w}-n {m}100 {w}-q -s           {c}║
║{w}                                                              {c}║
╠{'═'*62}╣
║{w}                                                              {c}║
║{y}  HOW IT WORKS{w}                                                {c}║
║{d}  ──────────────────────────────────────────────────────────  {c}║
║{w}                                                              {c}║
║  {c}✦ {w}Dot-trick  {d}u.ser@gmail.com == user@gmail.com              {c}║
║  {c}✦ {w}Plus-trick {d}user+tag@gmail.com → same inbox                {c}║
║{w}                                                              {c}║
╚{'═'*62}╝{R}
""")

# ─── CLI Mode ─────────────────────────────────────────────────
def cli():
    # Manual pre-parse for -h / --help to use our custom output
    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()
        sys.exit(0)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-e", "--email")
    parser.add_argument("-n", "--number", type=int, default=10)
    parser.add_argument("-s", "--save",  action="store_true")
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()

    if not args.quiet:
        banner()

    if not args.email:
        interactive()
        return

    if not validate_email(args.email):
        print(f"{C.RED}[!] Invalid email address: {args.email}{C.RESET}")
        sys.exit(1)

    aliases = generate_aliases(args.email, args.number)

    if args.quiet:
        print("\n".join(aliases))
    else:
        display_results(aliases, args.email)

    if args.save:
        name = args.email.split("@")[0]
        path = save_output(aliases, name)
        if not args.quiet:
            print(f"{C.YELLOW}[*] Saved: {path}{C.RESET}")

# ─── Entry Point ──────────────────────────────────────────────
if __name__ == "__main__":
    cli()