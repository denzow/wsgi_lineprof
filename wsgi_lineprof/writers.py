from io import TextIOWrapper  # noqa: F401
from queue import Queue
from threading import Thread
from typing import TextIO, Union  # noqa: F401

from wsgi_lineprof.stats import LineProfilerStats  # noqa: F401


class SyncWriter(object):
    def __init__(self,
                 stream,  # type: Union[TextIO, TextIOWrapper]
                 ):
        # type: (...) -> None
        self.stream = stream

    def write(self, stats):
        # type: (LineProfilerStats) -> None
        stats.write_text(self.stream)


class AsyncWriter(object):
    def __init__(self,
                 stream,  # type: Union[TextIO, TextIOWrapper]
                 ):
        # type: (...) -> None
        self.stream = stream
        self.queue = Queue()  # type: Queue
        self.writer_thread = Thread(target=self._write)
        self.writer_thread.setDaemon(True)
        self.writer_thread.start()

    def write(self, stats):
        # type: (LineProfilerStats) -> None
        self.queue.put(stats)

    def _write(self):
        # type: () -> None
        while True:
            stats = self.queue.get()
            stats.write_text(self.stream)
