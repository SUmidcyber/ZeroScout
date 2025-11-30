import argparse
import sys
import time
import random
import os
from datetime import datetime
from zeroscout.client import ZeroScoutCore
from zeroscout.models import Report 
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.align import Align
from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.tree import Tree
from rich.progress import track

console = Console()

WORLD_MAP_ASCII = """
   . . . . . . . . . . . . . . . . . .
 . . : : : : : : : : : : : : : : : : . .
. : : : : : : : : : : : : : : : : : : : .
. : : : : : : : : : : : : : : : : : : : .
 . . : : : : : : : : : : : : : : : : . .
   . . . . . . . . . . . . . . . . . .
"""

def generate_live_map(step, real_ips):
    map_text = Text(WORLD_MAP_ASCII, style="dim green")
    status = Text()
    status.append("\n📡 ZEROSCOUT GLOBAL SENSORS:\n", style="bold white")
    if not real_ips or (len(real_ips) == 1 and "No External" in real_ips[0]['ip']):
        status.append("● SCANNING ARTIFACTS...\n", style="dim white")
    else:
        for i, net in enumerate(real_ips[:3]):
            color = "bold red" if step % 2 == 0 else "dim red"
            status.append(f"● [INTERCEPTED] {net.get('proto')} -> {net['ip']}\n", style=color)
    return Panel(Align.center(Text.assemble(map_text, "\n", status)), title="[bold blue]🌍 ZEROSCOUT WAR ROOM[/bold blue]", border_style="blue")

def generate_packet_log(log_history):
    table = Table(box=None, show_header=False, expand=True)
    table.add_column("T", style="dim white"); table.add_column("S", style="green"); table.add_column("D", style="red"); table.add_column("P", style="cyan")
    for log in log_history[-6:]: table.add_row(log["time"], log["src"], log["dst"], log["proto"])
    return Panel(table, title="[blink bold red]📡 LIVE TRAFFIC[/blink bold red]", border_style="red")

def run_live_simulation(real_ips):
    layout = Layout(); layout.split_row(Layout(name="map", ratio=6), Layout(name="logs", ratio=4))
    pool_ips = [n['ip'] for n in real_ips if "No External" not in n['ip']] if real_ips else ["127.0.0.1"]
    with Live(layout, refresh_per_second=4) as live:
        for i in range(20):
            target = random.choice(pool_ips) if pool_ips else "Analyzing..."
            new_log = {"time": datetime.now().strftime("%H:%M:%S"), "src": "ZEROSCOUT", "dst": target, "proto": "TCP"}
            log_history = [new_log] 
            layout["map"].update(generate_live_map(i, real_ips))
            layout["logs"].update(generate_packet_log(log_history))
            time.sleep(0.2)

def create_final_dashboard(report):
    layout = Layout()
    layout.split_column(Layout(name="top", ratio=2), Layout(name="middle", ratio=4), Layout(name="bottom", ratio=4))
    layout["top"].split_row(Layout(name="info"), Layout(name="attribution"))
    
    t_info = Table(show_header=False, box=None, expand=True)
    t_info.add_row("VERDICT", f"[bold red]{report.verdict}[/bold red]")
    t_info.add_row("SCORE", f"[bold yellow]{report.score}/10[/bold yellow]")
    layout["info"].update(Panel(t_info, title="🛡️ ZEROSCOUT REPORT", border_style="red"))

    confidence = report.attribution_confidence
    bar = "█" * int(confidence/10) + "░" * (10 - int(confidence/10))
    attr_text = f"**ACTOR:** {report.apt_group}\n**CONF:** {confidence}% [{bar}]\n\n[italic cyan]{report.genetic_analysis_summary[:100]}...[/italic cyan]"
    layout["attribution"].update(Panel(Markdown(attr_text), title="🧬 DNA ATTRIBUTION", border_style="magenta"))

    layout["middle"].split_row(Layout(name="tree", ratio=5), Layout(name="intel", ratio=5))
    root = Tree(f"💀 [bold red]{report.md5[:8]}...[/bold red]")
    if report.tags:
        for tag in report.tags[:5]: root.add(f"⚠️ {tag}")
    else: root.add("✅ Clean")
    
    intel_text = "No Artifacts."
    intel_data = report.behavior.get("intelligence", {})
    if intel_data and intel_data.get("wallets"): intel_text = f"💰 **Wallet:** {intel_data['wallets'][0][:20]}..."
    layout["tree"].update(Panel(root, title="⚡ FINDINGS", border_style="green"))
    layout["intel"].update(Panel(Markdown(intel_text), title="🕵️ INTEL", border_style="blue"))

    layout["bottom"].split_row(
        Layout(Panel(Syntax(report.generate_yara_rule(), "java", theme="monokai", line_numbers=True), title="🚀 AUTO-DEFENSE (YARA)")),
        Layout(Panel(Syntax(report.generate_sigma_rule(), "yaml", theme="monokai"), title="⚡ SIEM RULE (SIGMA)"))
    )
    return layout

def main():
    parser = argparse.ArgumentParser(description="ZeroScout - The Autonomous Threat Hunter")
    subparsers = parser.add_subparsers(dest="command")
    scan_p = subparsers.add_parser("scan"); scan_p.add_argument("target")
    result_p = subparsers.add_parser("result"); result_p.add_argument("uuid")
    
    args = parser.parse_args()
    if len(sys.argv) == 1: parser.print_help(); sys.exit(1)

    if args.command == "scan":
        client = ZeroScoutCore()
        target = args.target

        if os.path.isdir(target):
            console.print(Panel.fit(f"[bold white]ZEROSCOUT[/bold white] [cyan]MASS HUNT MODE[/cyan]", style="on black"))
            files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(target) for f in filenames if f.endswith(('.exe', '.dll', '.ps1'))]
            found = []
            for f in track(files, description="ZeroScout Hunting..."):
                res = client.scan_file(f)
                data = client.get_result(res.get('uuid'))
                if data.get('score', 0) >= 5: found.append((os.path.basename(f), data))
            
            if found:
                t = Table(header_style="bold red", title=f"🚨 {len(found)} THREATS DETECTED")
                t.add_column("File"); t.add_column("Score"); t.add_column("Reason")
                for name, d in found: t.add_row(name, str(d.get('score')), d.get('tags')[0] if d.get('tags') else "-")
                console.print(t)
            else: console.print("[bold green]✅ SYSTEM CLEAN[/bold green]")

        elif os.path.isfile(target):
            console.print(Panel.fit(f"[bold white]ZEROSCOUT[/bold white] [cyan]AUTONOMOUS HUNTER[/cyan]\nTarget: {os.path.basename(target)}", style="on black"))
            res = client.scan_file(target)
            console.print(f"[yellow]⚡ ZeroScout Engine Activated...[/yellow]")
            time.sleep(1)
            try:
                raw = client.get_result(res.get('uuid'))
                report = Report(uuid=res.get('uuid'), status=raw.get("status"), verdict=raw.get("verdict"), score=raw.get("score"), family=raw.get("family"), tags=raw.get("tags"), behavior=raw.get("behavior", {}), apt_group=raw.get("apt_group"), imphash=raw.get("imphash"), attribution_confidence=raw.get("attribution_confidence", 0), md5=raw.get("md5"))
                run_live_simulation(raw.get("behavior", {}).get("network", []))
                console.print(create_final_dashboard(report))
            except Exception as e: console.print(f"[bold red]Error: {e}[/bold red]")

if __name__ == "__main__":
    main()