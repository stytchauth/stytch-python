import time
from typing import Awaitable, Callable, Generic, Optional, TypeVar

T = TypeVar("T")


ReloadFunc = Callable[[Optional[T]], T]
AsyncReloadFunc = Callable[[Optional[T]], Awaitable[T]]


class LazyCache(Generic[T]):
    def __init__(
        self,
        reload_func: ReloadFunc[T],
        async_reload_func: AsyncReloadFunc[T],
        refresh_interval_seconds: int,
    ) -> None:
        self.reload_func = reload_func
        self.async_reload_func = async_reload_func
        self.refresh_interval_seconds = refresh_interval_seconds
        self.obj: Optional[T] = None
        # Something in the past where we'd need to refresh immediately
        self.last_refresh_time = time.time() - refresh_interval_seconds - 1

    def get(self) -> T:
        if (
            self.obj is None
            or time.time() - self.last_refresh_time > self.refresh_interval_seconds
        ):
            self.obj = self.reload_func(self.obj)
            self.last_refresh_time = time.time()
        assert self.obj is not None
        return self.obj

    async def get_async(self) -> T:
        if (
            self.obj is None
            or time.time() - self.last_refresh_time > self.refresh_interval_seconds
        ):
            self.obj = await self.async_reload_func(self.obj)
            self.last_refresh_time = time.time()
        assert self.obj is not None
        return self.obj
