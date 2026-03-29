#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║           MailMul — Email Alias Generator                    ║
║                  Developed by Mr_ofcodyx                     ║
╚══════════════════════════════════════════════════════════════╝
"""

import sys
import os
import re
import random
import time
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
    HIDE    = "\033[?25l"   # hide cursor
    SHOW    = "\033[?25h"   # show cursor
    UP      = "\033[1A"
    CLR     = "\033[2K"

def supports_color() -> bool:
    return sys.stdout.isatty() and os.environ.get("TERM") != "dumb"

if not supports_color():
    for attr in vars(C):
        if not attr.startswith("__"):
            setattr(C, attr, "")

# ─── Glitch chars ──────────────────────────────────────────────
GLITCH_CHARS = "!@#$%^&*<>?/\\|~`░▒▓█▄▀■□▪▫"

def glitch_text(text: str, intensity: int = 3) -> str:
    """Replace random chars with glitch characters."""
    chars = list(text)
    indices = [i for i, c in enumerate(chars) if c not in (" ", "║", "╔", "╚", "═")]
    sample = random.sample(indices, min(intensity, len(indices)))
    for i in sample:
        chars[i] = random.choice(GLITCH_CHARS)
    return "".join(chars)

# ─── Flash Banner ──────────────────────────────────────────────
BANNER_LINES = [
    f"╔{'═'*62}╗",
    f"║{'':62}║",
    f"║   ███╗   ███╗ █████╗ ██╗██╗     ███╗   ███╗██╗   ██╗         ║",
    f"║   ████╗ ████║██╔══██╗██║██║     ████╗ ████║██║   ██║         ║",
    f"║   ██╔████╔██║███████║██║██║     ██╔████╔██║██║   ██║         ║",
    f"║   ██║╚██╔╝██║██╔══██║██║██║     ██║╚██╔╝██║██║   ██║         ║",
    f"║   ██║ ╚═╝ ██║██║  ██║██║███████╗██║ ╚═╝ ██║╚██████╔╝         ║",
    f"║   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝          ║",
    f"║{'':62}║",
    f"║   ✉  M U L T I P L Y  —  Email Alias Generator               ║",
    f"║{'':62}║",
    f"║               ┌─────────────────────────────┐                ║",
    f"║               │  you@gmail.com              │                ║",
    f"║               │  y.ou@gmail.com             │                ║",
    f"║               │  you+alias@gmail.com  ✓     │                ║",
    f"║               └─────────────────────────────┘                ║",
    f"║{'':62}║",
    f"║            Developed by: Mr_ofcodyx                          ║",
    f"╚{'═'*62}╝",
]

FLASH_COLORS = [C.RED, C.CYAN, C.YELLOW, C.MAGENTA, C.GREEN, C.WHITE]

def _print_banner(color: str, glitch: bool = False):
    """Print banner in a single color, optionally with glitch."""
    sys.stdout.write("\033[H")  # move cursor to top-left
    for i, line in enumerate(BANNER_LINES):
        txt = glitch_text(line, intensity=random.randint(2, 5)) if glitch else line
        sys.stdout.write(f"{color}{txt}{C.RESET}\n")
    sys.stdout.flush()

def banner(quiet: bool = False):
    os.system("cls" if os.name == "nt" else "clear")

    if quiet:
        # No animation in quiet/pipe mode
        _print_banner(C.CYAN)
        print()
        return

    sys.stdout.write(C.HIDE)
    try:
        # Phase 1 — glitch flash (rapid color cycling)
        for _ in range(10):
            color = random.choice(FLASH_COLORS)
            _print_banner(color, glitch=True)
            time.sleep(0.04)

        # Phase 2 — settle into cyan
        for color in [C.WHITE, C.CYAN, C.WHITE, C.CYAN]:
            _print_banner(color, glitch=False)
            time.sleep(0.07)

        # Final clean render with proper coloring
        sys.stdout.write("\033[H")
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
    finally:
        sys.stdout.write(C.SHOW)
        sys.stdout.flush()

# ─── Animated Loading Bar ──────────────────────────────────────
def loading_bar(label: str, total: int, delay: float = 0.03):
    """Render an animated progress bar."""
    bar_width = 40
    sys.stdout.write(C.HIDE)
    try:
        for i in range(total + 1):
            filled = int(bar_width * i / total)
            bar = f"{C.GREEN}{'█' * filled}{C.DIM}{'░' * (bar_width - filled)}{C.RESET}"
            pct = f"{C.YELLOW}{i * 100 // total:>3}%{C.RESET}"
            sys.stdout.write(f"\r  {C.CYAN}{label}{C.RESET} [{bar}{C.CYAN}] {pct} ")
            sys.stdout.flush()
            time.sleep(delay)
        print()
    finally:
        sys.stdout.write(C.SHOW)

# ─── Spinner ───────────────────────────────────────────────────
def spinner(label: str, duration: float = 1.2):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end = time.time() + duration
    sys.stdout.write(C.HIDE)
    try:
        i = 0
        while time.time() < end:
            sys.stdout.write(f"\r  {C.CYAN}{frames[i % len(frames)]}{C.RESET}  {C.WHITE}{label}{C.RESET}  ")
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
        sys.stdout.write(f"\r  {C.GREEN}✓{C.RESET}  {C.WHITE}{label}{C.RESET}        \n")
        sys.stdout.flush()
    finally:
        sys.stdout.write(C.SHOW)

# ─── Typewriter print ──────────────────────────────────────────
def typewrite(text: str, delay: float = 0.018):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ─── Email Validation ──────────────────────────────────────────
EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$"
)

def validate_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))

# ─── Alias Generation (dot-trick) ─────────────────────────────
def dot_variants(name: str) -> list[str]:
    if len(name) <= 1:
        return [name]
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
    chosen = random.sample(PLUS_ALIASES, min(count, len(PLUS_ALIASES)))
    return [f"{name}+{alias}@{domain}" for alias in chosen]

# ─── Core Generator ───────────────────────────────────────────
def generate_aliases(email: str, count: int) -> list[str]:
    name, domain = email.rsplit("@", 1)
    all_dot = dot_variants(name)
    all_dot_emails = [f"{v}@{domain}" for v in all_dot]
    max_dot = len(all_dot_emails)
    dot_count = min(count, max_dot)
    plus_count = max(0, count - dot_count)
    chosen_dot = random.sample(all_dot_emails, dot_count)
    if email not in chosen_dot:
        chosen_dot[0] = email
    chosen_plus = plus_variants(name, domain, plus_count)
    result = list(dict.fromkeys(chosen_dot + chosen_plus))
    random.shuffle(result)
    return result[:count]

# ─── Display Results (animated) ───────────────────────────────
def display_results(aliases: list[str], email: str, animated: bool = True):
    print(f"\n{C.CYAN}┌{'─'*56}┐")
    print(f"│{C.WHITE}  ✉  Generated Aliases for {C.YELLOW}{email:<28}{C.CYAN}│")
    print(f"├{'─'*56}┤{C.RESET}")

    for i, alias in enumerate(aliases, 1):
        # Alternate row tint for readability
        row_color = C.WHITE if i % 2 == 0 else C.CYAN
        marker = f"{C.GREEN}✓{C.RESET}"
        num = f"{C.DIM}{i:>3}.{C.RESET}"
        line = f"{C.CYAN}│{C.RESET} {num} {marker} {row_color}{alias:<48}{C.CYAN}│{C.RESET}"
        if animated:
            print(line)
            time.sleep(0.04)
        else:
            print(line)

    print(f"{C.CYAN}└{'─'*56}┘{C.RESET}")
    # Flash the total count
    total_str = f"  Total: {len(aliases)} aliases generated."
    if animated:
        for color in [C.WHITE, C.GREEN, C.YELLOW, C.GREEN]:
            sys.stdout.write(f"\r{color}{total_str}{C.RESET}  ")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
    else:
        print(f"\n{C.GREEN}{total_str}{C.RESET}")

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
            # Shake-style error flash
            for color in [C.RED, C.YELLOW, C.RED]:
                sys.stdout.write(f"\r{color}  [!] Invalid email address. Try again.{C.RESET}   ")
                sys.stdout.flush()
                time.sleep(0.12)
            print()
            continue
        break

    while True:
        raw = prompt("Number of aliases to generate")
        if raw.isdigit() and int(raw) > 0:
            count = int(raw)
            break
        for color in [C.RED, C.YELLOW, C.RED]:
            sys.stdout.write(f"\r{color}  [!] Please enter a positive integer.{C.RESET}   ")
            sys.stdout.flush()
            time.sleep(0.12)
        print()

    print()
    spinner("Initializing engine...", duration=0.6)
    loading_bar("Generating aliases", count, delay=max(0.01, min(0.05, 1.5 / count)))

    aliases = generate_aliases(email, count)
    display_results(aliases, email, animated=True)

    save = prompt("\nSave output to file? (y/n)").lower()
    if save == "y":
        name = email.split("@")[0]
        spinner("Writing to disk...", duration=0.5)
        path = save_output(aliases, name)
        typewrite(f"  {C.YELLOW}Output saved at: {C.WHITE}{path}{C.RESET}", delay=0.015)

    print(f"\n{C.GREEN}  Done.{C.RESET}\n")

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
    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()
        sys.exit(0)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-e", "--email")
    parser.add_argument("-n", "--number", type=int, default=10)
    parser.add_argument("-s", "--save",  action="store_true")
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()

    if not args.email:
        # Always run full interactive (includes banner with animation)
        interactive()
        return

    if not args.quiet:
        banner()

    if not validate_email(args.email):
        print(f"{C.RED}[!] Invalid email address: {args.email}{C.RESET}")
        sys.exit(1)

    if args.quiet:
        aliases = generate_aliases(args.email, args.number)
        print("\n".join(aliases))
    else:
        spinner("Initializing engine...", duration=0.6)
        loading_bar("Generating aliases", args.number, delay=max(0.01, min(0.05, 1.5 / args.number)))
        aliases = generate_aliases(args.email, args.number)
        display_results(aliases, args.email, animated=True)

    if args.save:
        name = args.email.split("@")[0]
        if not args.quiet:
            spinner("Writing to disk...", duration=0.4)
        path = save_output(aliases, name)
        if not args.quiet:
            typewrite(f"  {C.YELLOW}Saved: {C.WHITE}{path}{C.RESET}", delay=0.015)

# ─── Entry Point ──────────────────────────────────────────────
if __name__ == "__main__":
    cli()
