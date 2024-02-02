from rich.console import Console
from rich.table import Table


def calculate_tax(annual_income, tax_relief=0.0):
    adjusted_income = annual_income - tax_relief
    tax_slabs = [
        (0, 250000, 0),
        (250001, 500000, 0.10),
        (500001, 1000000, 0.20),
        (1000001, float('inf'), 0.30)
    ]

    total_tax = 0
    local_console = Console()
    local_console.print("[bold magenta]TAX CALCULATION[/bold magenta]", justify="center")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Slab", style="dim")
    table.add_column("Rate", style="dim")
    table.add_column("Tax Amount", justify="right")

    for lower_limit, upper_limit, tax_rate in tax_slabs:
        if adjusted_income > lower_limit:
            taxable_income = min(adjusted_income, upper_limit) - lower_limit
            tax_for_slab = taxable_income * tax_rate
            total_tax += tax_for_slab

            slab_range = f"INR {lower_limit:,.2f} to INR {upper_limit:,.2f}"
            table.add_row(slab_range, f"{tax_rate * 100}%", f"INR {tax_for_slab:,.2f}")

            if adjusted_income <= upper_limit:
                break

    local_console.print(table, justify="center")
    local_console.print(f"[bold red]Annual Tax Liability: INR {total_tax:,.2f}[/bold red]", justify="center")
    local_console.print(f"[bold green]Annual Credit Salary: INR {annual_income - total_tax:,.2f}[/bold green]",
                        justify="center")
    local_console.print(f"[bold red]Monthly Tax Liability: INR {total_tax / 12:,.2f}[/bold red]", justify="center")
    local_console.print(f"[bold green]Monthly Credit Salary: INR {(annual_income - total_tax) / 12:,.2f}[/bold green]",
                        justify="center")


if __name__ == "__main__":
    main_console = Console()
    try:
        annual_net_income = float(main_console.input("[bold]Enter your annual net income (in INR): [/bold]"))
        input_tax_relief = main_console.input("[bold]Enter tax relief amount (if any, otherwise enter 0): [/bold]")

        input_tax_relief = float(input_tax_relief) if input_tax_relief.strip() else 0.0

        calculate_tax(annual_net_income, input_tax_relief)
    except ValueError:
        main_console.print(
            "[bold red]Please enter a valid numerical value for your income and tax relief amount.[/bold red]")
