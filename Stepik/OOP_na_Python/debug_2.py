
def from_hex_to_rgb(color: str) -> tuple[int, int, int]:
    return tuple(int(color[i:i+2], 16) for i in (1, 3, 5))


def convert_to_rgb(values: list[str]) -> list[tuple[int, int, int]]:
    return list(map(from_hex_to_rgb, values))



colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50']
print(convert_to_rgb(colors))
