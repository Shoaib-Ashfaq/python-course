import sys

def convert_temperature(from_scale, to_scale, value):
    from_scale = from_scale.lower()
    to_scale = to_scale.lower()

    if from_scale == 'c':
        temp_c = value
    elif from_scale == 'f':
        temp_c = (value - 32) * 5 / 9
    elif from_scale == 'k':
        temp_c = value - 273.15
    else:
        sys.exit("Error: Invalid 'from' scale. Use c, f, or k.")

    if to_scale == 'c':
        return temp_c
    elif to_scale == 'f':
        return temp_c * 9 / 5 + 32
    elif to_scale == 'k':
        return temp_c + 273.15
    else:
        sys.exit("Error: Invalid 'to' scale. Use c, f, or k.")

if len(sys.argv) != 7:
    print("Usage: python temp_converter.py --from c --to f --value 100")
    sys.exit()

try:
    from_index = sys.argv.index('--from') + 1
    to_index = sys.argv.index('--to') + 1
    value_index = sys.argv.index('--value') + 1

    from_scale = sys.argv[from_index]
    to_scale = sys.argv[to_index]
    value = float(sys.argv[value_index])

    result = convert_temperature(from_scale, to_scale, value)
    print(f"\n{value}°{from_scale.upper()} = {round(result, 2)}°{to_scale.upper()}")

except ValueError:
    print("Error: Value must be a number.")
except Exception as e:
    print("Unexpected error:", e)
