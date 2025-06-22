"""
PACKING & UNPACKING NEIGHBORHOOD DATA
"""

from typing import List, Dict

import array, base64, json


def index_geoids(geoids: List[str]) -> Dict[str, int]:
    """Create a mapping of geoids to their indices in a canonical list."""

    return {geoid: idx for idx, geoid in enumerate(geoids)}


def reverse_index(geoid_to_index: Dict[str, int]) -> Dict[int, str]:
    """Create a back mapping of indices to their geoids."""

    return {idx: geoid for geoid, idx in geoid_to_index.items()}


def init_bit_array(size: int) -> array.array:
    bits = array.array("B", [0] * ((size + 7) // 8))

    return bits


def set_bit(array, index, value):
    byte_index = index // 8
    bit_index = index % 8
    if value:
        array[byte_index] |= 1 << bit_index
    else:
        array[byte_index] &= ~(1 << bit_index)


def get_bit(arr, index):
    byte_index = index // 8
    bit_index = index % 8
    return bool(arr[byte_index] & (1 << bit_index))


def serialize_bits(bit_array, size: int):
    byte_data = bit_array.tobytes()
    base64_str = base64.b64encode(byte_data).decode("ascii")

    # Create a JSON object with metadata
    json_data = {
        "encoding": "base64",
        "type": "bit_array",
        "length": size,
        "data": base64_str,
    }
    return json.dumps(json_data)


def deserialize_bits(json_string):
    json_data = json.loads(json_string)
    byte_data = base64.b64decode(json_data["data"])
    # size: int = json_data["length"]

    # Create new array from bytes
    bit_array = array.array("B")
    bit_array.frombytes(byte_data)
    return bit_array


### END ###
