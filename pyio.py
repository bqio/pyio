from struct import pack, unpack
from io import BufferedIOBase


class MemoryReader:
    """
    Simple memory reader.
    """

    def __init__(self, buffer: bytes, endian="<") -> None:
        """
        Args:
            buffer (bytes): Bytes array.
            endian (str): Bytes endian.

        Returns:
            None
        """
        self.buffer = buffer
        self.endian = endian
        self.offset = 0

    def read(self, count: int) -> bytes:
        """
        Read bytes from buffer.

        Args:
            count (int): Bytes count.
        Returns:
            bytes: Bytes array.
        """
        buf = self.buffer[self.offset:self.offset + count]
        self.offset += count
        return buf

    def read_i8(self) -> int:
        """
        Read 8-bit signed integer from buffer.

        Returns:
            int: 8-bit signed integer.
        """
        buf = self.read(1)
        return unpack(self.endian + "b", buf)[0]

    def read_i16(self) -> int:
        """
        Read 16-bit signed integer from buffer.

        Returns:
            int: 16-bit signed integer.
        """
        buf = self.read(2)
        return unpack(self.endian + "h", buf)[0]

    def read_i32(self) -> int:
        """
        Read 32-bit signed integer from buffer.

        Returns:
            int: 32-bit signed integer.
        """
        buf = self.read(4)
        return unpack(self.endian + "i", buf)[0]

    def read_i64(self) -> int:
        """
        Read 64-bit signed integer from buffer.

        Returns:
            int: 64-bit signed integer.
        """
        buf = self.read(8)
        return unpack(self.endian + "q", buf)[0]

    def read_u8(self) -> int:
        """
        Read 8-bit unsigned integer from buffer.

        Returns:
            int: 8-bit unsigned integer.
        """
        buf = self.read(1)
        return unpack(self.endian + "B", buf)[0]

    def read_u16(self) -> int:
        """
        Read 16-bit unsigned integer from buffer.

        Returns:
            int: 16-bit unsigned integer.
        """
        buf = self.read(2)
        return unpack(self.endian + "H", buf)[0]

    def read_u32(self) -> int:
        """
        Read 32-bit unsigned integer from buffer.

        Returns:
            int: 32-bit unsigned integer.
        """
        buf = self.read(4)
        return unpack(self.endian + "I", buf)[0]

    def read_u64(self) -> int:
        """
        Read 64-bit unsigned integer from buffer.

        Returns:
            int: 64-bit unsigned integer.
        """
        buf = self.read(8)
        return unpack(self.endian + "Q", buf)[0]

    def read_str(self, length: int) -> str:
        """
        Read UTF-8 string from buffer.

        Args:
            length (int): String length.

        Returns:
            str: UTF-8 string.
        """
        return self.read(length).decode('utf-8')

    def read_strz(self, terminator: int = 0) -> str:
        """
        Read UTF-8 null terminated string from buffer.

        Args:
            terminator (int): Null character.

        Returns:
            str: UTF-8 string.
        """
        str_length = 0
        pos = self.tell()
        while self.read_i8() != terminator:
            str_length += 1
        self.seek(pos)
        line = self.read_str(str_length)
        self.skip(1)
        return line

    def seek(self, offset: int):
        """
        Set offset in buffer.

        Args:
            offset (int): Offset in buffer.
        """
        self.offset = offset

    def tell(self) -> int:
        """
        Get offset in buffer.

        Returns:
            int: Offset in buffer.
        """
        return self.offset

    def skip(self, count: int):
        """
        Skip bytes in buffer.

        Args:
            count (int): Bytes count.

        Returns:
            None
        """
        self.seek(self.tell() + count)


class MemoryWriter:
    """
    Simple memory writer.
    """

    def __init__(self, endian="<"):
        """
        Args:
            endian (str): Bytes endian.

        Returns:
            None
        """
        self.endian = endian
        self.buffer = bytes()

    def write(self, data: bytes) -> None:
        """
        Write bytes into buffer.
        """
        self.buffer += data

    def write_i8(self, data: int) -> None:
        """
        Write 8-bit signed integer into buffer.
        """
        buf = pack(self.endian + "b", data)
        self.write(buf)

    def write_i16(self, data: int) -> None:
        """
        Write 16-bit signed integer into buffer.
        """
        buf = pack(self.endian + "h", data)
        self.write(buf)

    def write_i32(self, data: int) -> None:
        """
        Write 32-bit signed integer into buffer.
        """
        buf = pack(self.endian + "i", data)
        self.write(buf)

    def write_i64(self, data: int) -> None:
        """
        Write 64-bit signed integer into buffer.
        """
        buf = pack(self.endian + "q", data)
        self.write(buf)

    def write_u8(self, data: int) -> None:
        """
        Write 8-bit unsigned integer into buffer.
        """
        buf = pack(self.endian + "B", data)
        self.write(buf)

    def write_u16(self, data: int) -> None:
        """
        Write 16-bit unsigned integer into buffer.
        """
        buf = pack(self.endian + "H", data)
        self.write(buf)

    def write_u32(self, data: int) -> None:
        """
        Write 32-bit unsigned integer into buffer.
        """
        buf = pack(self.endian + "I", data)
        self.write(buf)

    def write_u64(self, data: int) -> None:
        """
        Write 64-bit unsigned integer into buffer.
        """
        buf = pack(self.endian + "Q", data)
        self.write(buf)

    def write_str(self, data: str) -> None:
        """
        Write UTF-8 string into buffer.
        """
        buf = data.encode('utf-8')
        self.write(buf)

    def write_strz(self, data: str) -> None:
        """
        Write UTF-8 string with null terminated byte into buffer.
        """
        buf = data.encode('utf-8')
        self.write(buf)
        self.write_i8(0)


class Writer:
    """
    Simple writer class.
    """

    def __init__(self, buffer, endian="<") -> None:
        self.buffer = buffer
        self.endian = endian

    def write(self, buf: bytes) -> None:
        """
        Write bytes into buffer.
        """
        self.buffer.write(buf)

    def write_i8(self, data: int) -> None:
        """
        Write 8-bit signed integer into buffer.
        """
        buf = pack(self.endian + "b", data)
        self.write(buf)

    def write_i16(self, data: int) -> None:
        """
        Write 16-bit signed integer into buffer.
        """
        buf = pack(self.endian + "h", data)
        self.write(buf)

    def write_i32(self, data: int) -> None:
        """
        Write 32-bit signed integer into buffer.
        """
        buf = pack(self.endian + "i", data)
        self.write(buf)

    def write_i64(self, data: int) -> None:
        """
        Write 64-bit signed integer into buffer.
        """
        buf = pack(self.endian + "q", data)
        self.write(buf)

    def write_u8(self, data: int) -> None:
        """
        Write 8-bit unsigned integer into buffer.
        """
        buf = pack(self.endian + "B", data)
        self.write(buf)

    def write_u16(self, data: int) -> None:
        """
        Write 16-bit unsigned integer into buffer.
        """
        buf = pack(self.endian + "H", data)
        self.write(buf)

    def write_u32(self, data: int) -> None:
        """
        Write 32-bit unsigned integer into buffer.
        """
        buf = pack(self.endian + "I", data)
        self.write(buf)

    def write_u64(self, data: int) -> None:
        """
        Write 64-bit unsigned integer into buffer.
        """
        buf = pack(self.endian + "Q", data)
        self.write(buf)

    def write_str(self, data: str) -> None:
        """
        Write UTF-8 string into buffer.
        """
        buf = data.encode('utf-8')
        self.write(buf)

    def write_strz(self, data: str) -> None:
        """
        Write UTF-8 string with null terminated byte into buffer.
        """
        buf = data.encode('utf-8')
        self.write(buf)
        self.write_i8(0)

    def skip(self, count: int) -> None:
        """
        Skip (fill) bytes in buffer.
        """
        for _ in range(count):
            self.write_i8(0)

    def seek(self, offset: int) -> None:
        """
        Set offset in buffer.
        """
        self.buffer.seek(offset)

    def tell(self) -> int:
        """
        Get offset from buffer.
        """
        return self.buffer.tell()

    def close(self) -> None:
        """
        Close writer.
        """
        self.buffer.close()

    @staticmethod
    def into_file(filename, buffer: bytes) -> None:
        """
        Write buffer into file.
        """
        with open(filename, "wb") as f:
            f.write(buffer)


class Reader:
    """
    Simple memory reader.
    """

    def __init__(self, buffer: BufferedIOBase, endian="<") -> None:
        self.buffer = buffer
        self.endian = endian

    def close(self) -> None:
        """
        Close reader.
        """
        self.buffer.close()

    def read(self, count: int) -> bytes:
        """
        Read bytes from buffer.

        Args:
            count (int): Bytes count.

        Returns:
            bytes: Bytes array.
        """
        return self.buffer.read(count)

    def read_i8(self) -> int:
        """
        Read 8-bit signed integer from buffer.
        """
        buf = self.read(1)
        return unpack(self.endian + "b", buf)[0]

    def read_i16(self) -> int:
        """
        Read 16-bit signed integer from buffer.
        """
        buf = self.read(2)
        return unpack(self.endian + "h", buf)[0]

    def read_i32(self) -> int:
        """
        Read 32-bit signed integer from buffer.
        """
        buf = self.read(4)
        return unpack(self.endian + "i", buf)[0]

    def read_i64(self) -> int:
        """
        Read 64-bit signed integer from buffer.
        """
        buf = self.read(8)
        return unpack(self.endian + "q", buf)[0]

    def read_u8(self) -> int:
        """
        Read 8-bit unsigned integer from buffer.
        """
        buf = self.read(1)
        return unpack(self.endian + "B", buf)[0]

    def read_u16(self) -> int:
        """
        Read 16-bit unsigned integer from buffer.
        """
        buf = self.read(2)
        return unpack(self.endian + "H", buf)[0]

    def read_u32(self) -> int:
        """
        Read 32-bit unsigned integer from buffer.
        """
        buf = self.read(4)
        return unpack(self.endian + "I", buf)[0]

    def read_u64(self) -> int:
        """
        Read 64-bit unsigned integer from buffer.
        """
        buf = self.read(8)
        return unpack(self.endian + "Q", buf)[0]

    def read_str(self, size: int) -> str:
        """
        Read UTF-8 string from buffer.
        """
        return self.read(size).decode('utf-8')

    def read_str_xor(self, size: int, xor: int) -> str:
        """
        Read UTF-8 XOR string from buffer.
        """
        return bytes(list(map(lambda n: n ^ xor, list(self.read(size))))).decode('utf-8')

    def read_strz(self, terminator: int = 0) -> str:
        """
        Read UTF-8 null terminated string from buffer.
        """
        str_length = 0
        pos = self.tell()
        while self.read_i8() != terminator:
            str_length += 1
        self.seek(pos)
        line = self.read_str(str_length)
        self.skip(1)
        return line

    def seek(self, offset: int) -> None:
        """
        Set offset in buffer.
        """
        self.buffer.seek(offset)

    def tell(self) -> int:
        """
        Get offset from buffer.
        """
        return self.buffer.tell()

    def skip(self, count: int) -> None:
        """
        Skip bytes in buffer.
        """
        self.seek(self.tell() + count)
