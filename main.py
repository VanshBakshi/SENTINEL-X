import argparse
from rich.console import Console
from rich.table import Table
from src.pipeline import SentinelPipeline

c=Console()

def main():
    p=argparse.ArgumentParser(description="SENTINEL-X AI Threat Intelligence Platform")
    p.add_argument("--input",default="data/demo")
    args=p.parse_args()

    c.print("\n[bold cyan]╔══════════════════════════════════════════╗[/bold cyan]")
    c.print("[bold cyan]║       🛡️  SENTINEL-X SOC ENGINE         ║[/bold cyan]")
    c.print("[bold cyan]╚══════════════════════════════════════════╝[/bold cyan]\n")

    result=SentinelPipeline().run(args.input)
    iocs=result["iocs"]

    c.print(f"[green]✓ Analysis complete[/green]  IOCs: {len(iocs)}")
    c.print(f"Findings: {len(result['findings'])} | Attack-chain phases: {len(result['chain'])}")

    t=Table(title="Top Threat Indicators")
    for x in ["IOC","TYPE","RISK","SEVERITY","MITRE"]:
        t.add_column(x)
    for i in sorted(iocs,key=lambda x:x.risk,reverse=True)[:15]:
        t.add_row(i.value,i.ioc_type,str(i.risk),i.severity,i.technique or "-")
    c.print(t)
    c.print("\n[bold green]Reports:[/bold green] data/output/")

if __name__=="__main__":
    main()
