import argparse
from .core import how_much_bigger, smart_unit
from colorama import Fore, Style


def main():
    parser = argparse.ArgumentParser(description="Compare magnitudes of values like '40ms' and '100ns'")
    parser.add_argument("value1", help="First value (e.g. 40ms)")
    parser.add_argument("value2", help="Second value (e.g. 100ns)")
    parser.add_argument("--precision", type=int, default=2, help="Decimal precision for the ratio (default: 2)")
    parser.add_argument("--smart", action="store_true", help="Show values in smart human-readable units")
    parser.add_argument(
            "--unit-type",
            choices=["time", "data", "length", "mass", "energy", "auto"],
            default="auto",
            help="Unit type for smart formatting (default: auto)"
        )

    args = parser.parse_args()

    try:
        result = how_much_bigger(args.value1, args.value2, precision=args.precision)

        print(f"{Fore.GREEN}{args.value1}{Style.RESET_ALL} vs {Fore.CYAN}{args.value2}{Style.RESET_ALL} → {Fore.YELLOW}{result}{Style.RESET_ALL}")

        if args.smart:
            from .core import parse_value
            a_val = parse_value(args.value1)
            b_val = parse_value(args.value2)
            print("Smart view:",
                f"{smart_unit(a_val, args.unit_type)} vs {smart_unit(b_val, args.unit_type)}")
        

    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        exit(1)
